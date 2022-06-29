import ReactDOM from 'react-dom/client';
import { useState, useEffect } from 'react';
import './style.css';

const Square = props => {
  return (
    <button className="square" onClick={props.onClick}>
      {props.value}
    </button>
  );
}

const Board = props =>  {

  const renderSquare = i => {
    return ( 
      <Square  
        value={props.squares[i]} 
        onClick={() => props.onClick(i)}
      />
    );
  }
  
  return (
    <div>
      <div className="board-row">
        {renderSquare(0)}
        {renderSquare(1)}
        {renderSquare(2)}
      </div>
      <div className="board-row">
        {renderSquare(3)}
        {renderSquare(4)}
        {renderSquare(5)}
      </div>
      <div className="board-row">
        {renderSquare(6)}
        {renderSquare(7)}
        {renderSquare(8)}
      </div>
    </div>
  );
}

const Game = props => {

  let current;
  let status;
  let moves;

  const[history, setHistory] = useState([{squares: Array(9).fill(null)}]);
  const[xIsNext, setxIsNext] = useState(true);
  const[stepNumber, setStepNumber] = useState(0);

  const handleClick = i => {
    const newHistory = history.slice(0, stepNumber+1);
    setHistory(newHistory);
    const squares = history[history.length-1].squares.slice();
    if(calculateWinner(squares)||squares[i]) {
      return;
    }
    squares[i] = xIsNext ? 'X' : 'O';
    setHistory(history.concat([{squares: squares}]));
    setStepNumber(history.length);
    setxIsNext(!xIsNext);
  }

  const jumpTo = step => {
    setStepNumber(step);
    setxIsNext((step % 2) === 0);
  }

  useEffect(() => {
    return () => {
      current = history[stepNumber];
      const winner = calculateWinner(current.squares);
      if(winner) {
        status = 'Winner: '+winner;
      }
      else {
        status = 'Next Player: '+(xIsNext ? 'X' : 'O');
      }

      moves = history.map((step, move) => {
        const desc = move ? 'Go to move #'+move : 'Go to game start';
        return (
          <li key={move}>
            <button onClick={() => jumpTo(move)}>{desc}</button>
          </li>
        );
      });
    }
  }, [history, xIsNext, stepNumber]);

  return (
    <div className="game">
      <div className="game-board">
        <Board 
          squares={current.squares}
          onClick={(i) => handleClick(i)}
        />
      </div>
      <div className="game-info">
        <div>{status}</div>
        <ol>{moves}</ol>
      </div>
    </div>
  );
}

const calculateWinner = squares => {
  const lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ];
  for (let i = 0; i < lines.length; i++) {
    const [a, b, c] = lines[i];
    if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
      return squares[a];
    }
  }
  return null;
}

// ========================================

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Game />);
