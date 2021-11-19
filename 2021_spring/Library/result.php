<?php
include("config/session.php");
if(!isset($_SESSION['uid'])||!isset($_SESSION['pwd'])) {
  //로그인 하지 않고 이 페이지에 접근했다면 로그인 페이지로 퇴출시킨다.
  header("Location: login.php");
}
else {
    require('db_connect.php');
    ?>
  <!DOCTYPE html>
  <html lang="kr">
    <head>
      <meta charset="utf-8">
      <link rel="stylesheet" href="style.css">
      <title>Result_Page</title>
    </head>
    <body>
      <?php
      //process.php에서 처리를 하고 난 후 'result' 세션 변수를 세팅한 뒤 마이페이지로 돌아온다.
      //result 페이지에서는 'result' 세션 변수의 값을 확인하여 알맞은 알림 창을 띄운다.
      if(isset($_SESSION['result'])) {
        switch($_SESSION['result']) {
        case 'alreadyRented': //대출 하려 했으나 해당 도서가 이미 대출 중인 경우
            echo "<script>alert('This book is already rented by someone!');</script>";
            break;
        case 'alreadyReserved': //대출 하려 했으나 해당 도서가 이미 예약된 경우
            echo "<script>alert('This book is already reserved by someone!');</script>";
            break;
        case '3rents': //이미 3권 까지 대출한 경우
            echo  "<script>alert('You alreay have 3 books in rents.');</script>";
            break;
        case 'rentSuccess': // 대출에 성공한 경우
            echo "<script>alert('Rent successful.');</script>";
            break;
        case 'whywontyourent': //예약 하려 했으나 해당 도서가 현재 대출 중이 아닌 경우
            echo "<script>alert('This book belongs to no one by now! try rent.');</script>";
            break;
        case 'youRented': //자신이 대출한 책을 다시 예약하려고 하는 경우
            echo "<script>alert('You have already rented this book.');</script>";
              break;
        case 'iReserved': //자신이 예약한 책을 다시 예약하려고 하는 경우
            echo "<script>alert('You have already reserved this book.');</script>";
            break;
        case '3reserves': //이미 3권 까지 예약한 경우
            echo  "<script>alert('You already have 3 books in reservations.');</script>";
            break;
        case 'reserveSuccess': //예약에 성공한 경우
            echo "<script>alert('Reserved!');</script>";
            break;
          }
          unset($_SESSION['result']);//세션 변수의 값이 남아있기 때문에 unset()을 사용하여 지운다.
      }
      ?>
      <button type="button" id='butt' onclick="document.location.href='main.php'">Main Page</button><!--메인으로 돌아가는 버튼-->
      <!--여기부터 도서를 조회하는 테이블 구현-->
        <h2 id='texts' style='font-size:40px'>Search Results</h2>
          <table>
            <thread>
              <tr id='texts'>
                <th>Title</th>
                <th>Authors</th>
                <th>Publisher</th>
                <th>Year</th>
              </tr>
            <thread>
          <tbody>
            <?php
              //메인페이지에서 전송한 요소들을 가져온다.
              if(isset($_GET['title'])&&isset($_GET['op1'])&&isset($_GET['op2'])&&isset($_GET['op3'])&&isset($_GET['op4'])&&isset($_GET['op5'])&&isset($_GET['op6'])&&isset($_GET['op7'])
              &&isset($_GET['title'])&&isset($_GET['author'])&&isset($_GET['publisher'])&&isset($_GET['publisher'])&&isset($_GET['from'])&&isset($_GET['to'])) {
                $op[0]=$_GET['op1'];
                $op[1]=$_GET['op2'];
                $op[2]=$_GET['op3'];
                $op[3]=$_GET['op4'];
                $op[4]=$_GET['op5'];
                $op[5]=$_GET['op6'];
                $op[6]=$_GET['op7'];
                $title=$_GET['title'];
                $author=$_GET['author'];
                $publisher=$_GET['publisher'];
                $from=$_GET['from'];
                $to=$_GET['to'];
                //사용자의 검색과 동일한 형태의 질의문을 작성해 문자열 변수로 저장.
                //and, or, not 등의 인자는 php의 문자열 덧셈을 통해 삽입한다.
                $statement = "SELECT E.ISBN, E.TITLE, A.AUTHOR, E.PUBLISHER, E.YEAR
                              FROM EBOOK E JOIN AUTHORS A
                              ON(E.ISBN = A.ISBN)
                              WHERE
                              TITLE ".$op[0]."=NVL(?,' ') ".$op[1]."
                              AUTHOR ".$op[2]."=NVL(?,' ') ".$op[3]."
                              PUBLISHER ".$op[4]."=NVL(?,' ') ".$op[5]."
                              YEAR ".$op[6]." BETWEEN ? AND ?";
                //응용 사용자는 말 그대로 공백을 생각했을 수 있지만 데이터베이스는 null로 생각하여 공백이 있을 시
                //아무런 결과가 나타나지 않게 되므로 공백은 ' '로 치환해주겠습니다.
                $stmt = $conn -> prepare($statement);
                $stmt -> execute(array($title,$author,$publisher,$from,$to));//질의 실행
                $arr = [];//질의 결과를 담을 연관배열. ISBN을 키로 가지고 나머지 행을 값으로 가진다.
                while($row = $stmt -> fetch(PDO::FETCH_ASSOC)) {//질의 결과를 한 행씩 가져온다.
                  if(array_key_exists($row['ISBN'],$arr))//만약 작가만 다르고 중복된 행이면
                    $arr[$row['ISBN']][1][sizeof($arr[$row['ISBN']][1])] = $row['AUTHOR'];//기존의 행에다가 작가만 더해준다.
                  else//중복이 없다면 연관배열에 새로운 행으로 추가한다.
                    $arr[$row['ISBN']] = array($row['TITLE'],array($row['AUTHOR']),$row['PUBLISHER'],$row['YEAR']);
                }
                foreach($arr as $key => $value) {
                  $_SESSION['mode'] = 'rent';
                  $_SESSION['isbn'] = $key;
                  include('check.php');
                  $_SESSION['mode'] = 'reserve';
                  include('check.php');
                  //이제 질의 결과들을 차례로 출력한다.
                  ?>
                  <tr id='inputbox'>
                    <td><?= $value[0] ?></td><!--TITLE-->
                    <td>
                      <select id='inputbox'><?php /*AUTHORS, 여러명 이니까 콤보박스로 구현한다.*/
                        foreach($value[1] as $val) { ?><!--foreach문으로 저장한 작가들 전부 출력-->
                          <option><?php echo($val); ?></option>
                          <?php
                        }
                        ?>
                      </select>
                    </td>
                    <td><?= $value[2] ?></td><!--PUBLISHER-->
                    <td><?= $value[3] ?></td><!--YEAR-->
                    <td>
                      <form action="process.php" method="get"><!--mode값과 isbn을 챙겨서 process.php로 이동한다-->
                        <input type="hidden" name = mode value = "rent">
                        <input type="hidden" name = isbn value = <?php echo $key;?>>
                        <input type="submit" id='butt'
                        <?php 
                        if(isset($_SESSION['rent_available'])) {?> style="background-color:#81B214; color:white" <?php }
                        else {?> style="background-color:#D32626; color:white" <?php }
                        unset($_SESSION['rent_available']);
                        ?>
                        value="Rent"><!--대출 버튼-->
                      </form>
                    </td>
                    <td>
                      <form action="process.php" method="get"><!--mode값과 isbn을 챙겨서 process.php로 이동한다-->
                        <input type="hidden" name = mode value = "reserve">
                        <input type="hidden" name = isbn value = <?php echo $key;?>>
                        <input type="submit" id='butt'
                        <?php 
                        if(isset($_SESSION['reserve_available'])) {?> style="background-color:#81B214; color:white" <?php }
                        else {?> style="background-color:#D32626; color:white" <?php }
                        unset($_SESSION['reserve_available']);
                        ?>
                        value="Reserve"><!--예약 버튼-->
                      </form>
                    </td>
                  </tr>
                  <?php
              }
            }
            unset($_SESSION['mode']);
            unset($_SESSION['isbn']);
            ?>
          </tbody>
        </table>
    </body>
  <html>
<?php } ?>
