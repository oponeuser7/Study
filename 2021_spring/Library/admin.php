<?php
@set_time_limit(0);
include("config/session.php");
if(!isset($_SESSION['uid'])||!isset($_SESSION['pwd'])||$_SESSION['uid']!=32594) {
  //로그인 하지 않고 이 페이지에 접근했다면 로그인 페이지로 퇴출시킨다.
  header("Location: login.php");
}
else {
  require('db_connect.php');
  $target = strtotime("00:02");//자정 쯤의 시간을 저장.
  $count = 0;
  while(true) {
    $now = strtotime(date("H:i"));//현재시간을 불러온다.
    if($now<$target) {//자정이 되었으면
      //예약 검사
      //한글질의문: 반납이 되었지만 예약자가 대출하지 않은 책을 가져와라.
      $stmt = $conn -> prepare("SELECT ISBN, RESERVATION FROM EBOOK WHERE RESERVATION IS NOT NULL");
      $stmt -> execute();
      while($row = $stmt -> fetch()) { //반납이 되었지만 예약자가 대출하지 않은 책이 있다면
        //한글질의문: 해당 도서의 다음 순번 예약자를 가져오라.
        $stmt2 = $conn -> prepare("DELETE FROM RESERVE WHERE CNO=? AND ISBN=?");
        $stmt2 -> execute(array($row[1],$row[0]));
        $stmt2 = $conn -> prepare("SELECT NAME, EMAIL, TITLE, CNO FROM RESINFO WHERE ISBN=? ORDER BY DATETIME FETCH FIRST 1 ROW ONLY");
        $stmt2 -> execute(array($row[0]));
        $temp = $stmt2 -> fetch();
        $_SESSION['name'] = $temp[0];//메일 전송을 위하여
        $_SESSION['email'] = $temp[1];//이름과 이메일을 저장.
        $_SESSION['title'] = $temp[2];//서명을 저장.
        //한글질의문: 가장 우선순위가 높은 회원이 현재 해당 도서를 대출할 권리가 있다.
        $stmt2 = $conn -> prepare("UPDATE EBOOK SET RESERVATION=? WHERE ISBN=?");
        $stmt2 -> execute(array($temp[3], $row[0]));
        include("mail/mail.php");//메일 전송.
        $count++;//메일 전송 횟수 증가
      }
      //반납 검사
      //한글 질의문: 반납 기한이 지난 도서의 ISBN과 빌린 회원의 CNO을 가져와라.
      $stmt = $conn -> prepare("SELECT CNO, ISBN FROM EBOOK WHERE DATEDUE < SYSDATE");
      $stmt -> execute();
      while($row = $stmt -> fetch()) { //반납 기한이 지난 도서가 있다면
        $cno = $row[0];//cno 저장
        $isbn = $row[1];//isbn 저장
        $stmt2 = $conn -> prepare("INSERT INTO PREVIOUSRENTAL VALUES(?, (SELECT DATERENTED FROM EBOOK WHERE ISBN=?), SYSDATE, ?)");
        $stmt2 -> execute(array($isbn, $isbn, $cno));
        //한글질의문: 해당 도서를 대출 가능 상태로 변경(반납)한다.
        $statement = "UPDATE EBOOK SET
                      CNO = null, EXTTIMES = null,
                      DATERENTED = null, DATEDUE = null
                      WHERE ISBN =?";
        $stmt2 = $conn -> prepare($statement);
        $stmt2 -> execute(array($isbn));
        $_SESSION['mypage'] = 'returnSuccess';//반납은 성공했다. 앞으로는 메일 전송에 관련된 코드이다.
        //한글질의문: 해당 도서의 예약 상황을 가져오라.
        $stmt2 = $conn -> prepare("SELECT * FROM RESERVE WHERE ISBN=?");
        $stmt2 -> execute(array($isbn));
        if($result = $stmt2 -> fetchAll()) { //방금 반납한 도서의 예약 내용이 있다면
          //한글질의문: 해당 도서를 예약한 회원들 중 가장 우선순위가 높은 회원을 가져오라.
          $stmt2 = $conn -> prepare("SELECT NAME, EMAIL, TITLE, CNO FROM (SELECT * FROM RESINFO WHERE ISBN =? ORDER BY DATETIME) WHERE ROWNUM<=1");
          $stmt2 -> execute(array($isbn));
          $temp = $stmt -> fetch();
          $_SESSION['name'] = $temp[0];//메일 전송을 위하여
          $_SESSION['email'] = $temp[1];//이름과 이메일을 저장.
          $_SESSION['title'] = $temp[2];//서명을 저장.
          //한글질의문: 가장 우선순위가 높은 회원이 현재 해당 도서를 대출할 권리가 있다.
          $stmt2 = $conn -> prepare("UPDATE EBOOK SET RESERVATION=? WHERE ISBN=?");
          $stmt2 -> execute(array($temp[3], $isbn));
          include("mail/mail.php");//메일 전송.
          $count++;//메일 전송 횟수 증가
        }
      }
      echo $count."mails have sended."; ?><br><?php
      echo "All done!";
      break;//프로그램을 마친다.
    }
    else {
      sleep(60);//1분간 대기.
    }
  }
}
?>
