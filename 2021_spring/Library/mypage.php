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
      <title>My_Page</title>
    </head>
    <body>
      <?php
      //process.php에서 처리를 하고 난 후 'mypage' 세션 변수를 세팅한 뒤 마이페이지로 돌아온다.
      //마이페이지에서는 'mypage' 세션 변수의 값을 확인하여 알맞은 알림 창을 띄운다.
      if(isset($_SESSION['mypage'])) {
        switch($_SESSION['mypage']) {
          case 'noExtendCauseReserved': //대출 연장 하려 했는데 해당 도서가 예약 중일 경우
              echo "<script>alert('This book is in reservation. Extend not available.');</script>";
              break;
          case 'extLimit': //대출 연장을 이미 2회 한 경우
              echo "<script>alert('You already Extended twice.');</script>";
              break;
          case 'extSuccess': //대출 연장에 성공한 경우
              echo "<script>alert('Extended!');</script>";
              break;
          case 'cancelSuccess': //예약 취소에 성공한 경우
              echo "<script>alert('Canceled!');</script>";
              break;
          case 'returnSuccess': //도서 반납에 성공한 경우
              echo "<script>alert('Returned!');</script>";
              break;
        }
        unset($_SESSION['mypage']); //세션 변수의 값이 남아있기 때문에 unset()을 사용하여 지운다.
      }
      ?>
      <button type="button" id='butt' onclick="document.location.href='main.php'">Main Page</button><!--메인으로 돌아가는 버튼-->
      <button type="button" id='butt' onclick="document.location.href='login.php'">Logout</button><!--로그아웃 버튼-->
      <h1 id='texts' style='font-size:40px'>My Page</h1>
      <!--여기부터 Rents 구현-->
        <h2 id='texts' style='font-size:30px'>Rents</h2>
        <table>
          <thread>
            <tr> <!--Rents에는 총 6개의 열이 존재한다.-->
              <th id='texts'>Title</th>
              <th id='texts'>Authors</th>
              <th id='texts'>Publisher</th>
              <th id='texts'>Year</th>
              <th id='texts'>DateRented</th>
              <th id='texts'>DateDue</th>
              <th id='texts'>ExtendCount</th>
            </tr>
           <thread>
          <tbody>
            <?php
            /*한글질의문: 해당 회원의 대출 서적 정보, 반납일, 연장횟수를 출력하라*/
            $statement = "SELECT E.ISBN, E.TITLE, A.AUTHOR, E.PUBLISHER, E.YEAR, E.DATERENTED, E.DATEDUE, E.EXTTIMES
                          FROM EBOOK E join AUTHORS A
                          ON(E.ISBN = A.ISBN)
                          WHERE E.CNO =?";
            $stmt = $conn -> prepare($statement);
            $stmt -> execute(array($_SESSION['uid']));
            $arr = [];//질의 결과를 담을 연관배열. ISBN을 키로 가지고 나머지 행을 값으로 가진다.
            while($row = $stmt -> fetch(PDO::FETCH_ASSOC)) {
              if(array_key_exists($row['ISBN'],$arr))//만약 작가만 다르고 중복된 행이면
                $arr[$row['ISBN']][1][sizeof($arr[$row['ISBN']][1])] = $row['AUTHOR'];//기존의 행에다가 작가만 더해준다.
              else//중복이 없다면 연관배열에 새로운 행으로 추가한다.
                $arr[$row['ISBN']] = array($row['TITLE'],array($row['AUTHOR']),$row['PUBLISHER'],$row['YEAR'],$row['DATERENTED'],$row['DATEDUE'],$row['EXTTIMES']);
            }
            foreach($arr as $key => $value) { 
              $_SESSION['mode'] = 'extend';
              $_SESSION['isbn'] = $key;
              include('check.php');
              ?><!--이제 질의 결과들을 차례로 출력한다.-->
              <tr id='inputbox' style='text-align:center'>
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
                <td><?= $value[4] ?></td><!--DATERENTED-->
                <td><?= $value[5] ?></td><!--DATEDUE-->
                <td><?= $value[6] ?></td><!--EXTTIMES-->
                <td>
                  <form action="process.php" method="get"><!--mode 값과 isbn을 챙겨서 process.php로 이동한다-->
                    <input type="hidden" name = mode value = "extend">
                    <input type="hidden" name = isbn value = <?php echo $key;?>>
                    <input type="submit" id='butt'
                    <?php 
                    if(isset($_SESSION['extend_available'])) {?> style="background-color:#81B214; color:white" <?php }
                    else {?> style="background-color:#D32626; color:white" <?php }
                    unset($_SESSION['extend_available']);
                    ?>
                    value="Extend"><!--연장 버튼-->
                  </form>
                </td>
                <td>
                  <form action="process.php" method="get"><!--mode값과 isbn을 챙겨서 process.php로 이동한다-->
                    <input type="hidden" name = mode value = "return">
                    <input type="hidden" name = isbn value = <?php echo $key;?>>
                    <input type="submit" id='butt' value="Return"><!--반납 버튼-->
                  </form>
                </td>
              </tr>
              <?php
          }
          unset($_SESSION['mode']);
          unset($_SESSION['isbn']);
          ?>
          </tbody>
        </table>
      <!--여기부터 Reservations 구현-->
        <h2 id='texts' style='font-size:30px'>Reservations</h2>
        <table>
          <thread>
            <tr id='texts'>
              <th>Title</th>
              <th>Authors</th>
              <th>Publisher</th>
              <th>Year</th>
              <th>Priority</th>
            </tr>
           <thread>
          <tbody>
            <?php
            /*한글질의문: 해당 회원의 예약 서적 정보와 예약 우선 순위를 출력하라.*/
            $statement = "SELECT E.ISBN, E.TITLE, A.AUTHOR, E.PUBLISHER, E.YEAR, R.CNO,
                          (SELECT P FROM (SELECT CNO, RANK() OVER (ORDER BY DATETIME) P FROM RESERVE WHERE ISBN = E.ISBN) WHERE CNO = R.CNO) PRIORITY
                          FROM RESERVE R JOIN EBOOK E
                          ON(R.ISBN = E.ISBN)
                          JOIN AUTHORS A
                          ON(E.ISBN = A.ISBN)
                          WHERE R.CNO =?";
            $stmt = $conn -> prepare($statement);
            $stmt -> execute(array($_SESSION['uid']));
            $arr = [];//질의 결과를 담을 연관배열. ISBN을 키로 가지고 나머지 행을 값으로 가진다.
            while($row = $stmt -> fetch(PDO::FETCH_ASSOC)) {
              if(array_key_exists($row['ISBN'],$arr))//만약 작가만 다르고 중복된 행이면
                $arr[$row['ISBN']][1][sizeof($arr[$row['ISBN']][1])] = $row['AUTHOR'];//기존의 행에다가 작가만 더해준다.
              else//중복이 없다면 연관배열에 새로운 행으로 추가한다.
                $arr[$row['ISBN']] = array($row['TITLE'],array($row['AUTHOR']),$row['PUBLISHER'],$row['YEAR'],$row['PRIORITY']);
            }
            foreach($arr as $key => $value) {
              $_SESSION['mode'] = 'cancel';
              $_SESSION['isbn'] = $key;
              include('check.php');
              ?><!--이제 질의 결과들을 차례로 출력한다.-->
              <tr id='inputbox' style='text-align:center'>
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
                <td style="text-align: center"><?= $value[4] ?></td><!--PRIORITY-->
                <td>
                  <form action="process.php" method="get"><!--mode 값과 isbn을 챙겨서 process.php로 이동한다-->
                    <input type="hidden" name = mode value = "cancel">
                    <input type="hidden" name = isbn value = <?php echo $key;?>>
                    <input type="submit" id='butt' value="Cancel"><!--취소 버튼-->
                  </form>
                </td>
              </tr>
              <?php
            }
            unset($_SESSION['mode']);
            unset($_SESSION['isbn']);
            ?>
          </tbody>
        </table>
    </body>
  <html>
<?php } ?>
