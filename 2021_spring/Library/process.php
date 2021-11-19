<?php
include("config/session.php");
if(!isset($_SESSION['uid'])||!isset($_SESSION['pwd'])) {
  //로그인 하지 않고 이 페이지에 접근했다면 로그인 페이지로 퇴출시킨다.
  header("Location: login.php");
}
else {
  require('db_connect.php');
  if(isset($_GET['mode'])&&isset($_GET['isbn'])) {//'mode'와 'isbn'이 정상적으로 수신 되었다면
  $isbn = $_GET['isbn']; //isbn 저장
  $cno = $_SESSION['uid']; //cno 저장
  switch($_GET['mode']) { //switch문을 통해 'mode'값에 따라 분기한다.
    case 'rent': //대출 버튼을 눌렀을 경우
        //한글질의문: 해당 도서가 현재 대출 중이라면 가져오라.
        $stmt = $conn -> prepare("SELECT * FROM EBOOK WHERE ISBN=? AND CNO IS NOT NULL");
        $stmt -> execute(array($isbn));
        if($result = $stmt -> fetchAll()) { //해당 도서가 이미 대출 중이므로 뒤로 돌아간다.
          $_SESSION['result'] = 'alreadyRented';
          break;
        }
        //한글질의문: 회원의 현재 대출 중인 도서 수를 가져오라.
        $stmt = $conn -> prepare("SELECT COUNT(*) FROM EBOOK WHERE CNO=?");
        $stmt -> execute(array($cno));
        $result = $stmt -> fetch();
        if($result[0] >= 3) {//이미 3권 까지 대출했으므로 뒤로 돌아간다.
          $_SESSION['result'] = '3rents';
          break;
        }
        //한글질의문: 해당 도서의 예약 상황을 가져오라.
        $stmt = $conn -> prepare("SELECT * FROM RESERVE WHERE ISBN=?");
        $stmt -> execute(array($isbn));
        if($result = $stmt -> fetchAll()) {//해당 도서가 이미 예약된 바 있다.
          //한글 질의문: 해당 도서를 예약한 회원들 중 가장 우선순위가 높은 회원을 가져오라.
          $stmt = $conn -> prepare("SELECT CNO FROM RESINFO WHERE ISBN =? ORDER BY DATETIME FETCH FIRST 1 ROW ONLY");
          $stmt -> execute(array($isbn));
          $temp = $stmt -> fetch();
          if($cno==$temp[0]) { //해당 도서가 현재 대출 중이 아니고 예약 순위가 1순위 이므로
            //한글 질의문: 해당 도서의 예약을 취소.
            $stmt = $conn -> prepare("DELETE FROM RESERVE WHERE CNO=? AND ISBN=?");
            $stmt -> execute(array($cno,$isbn));
          }
          else { //해당 도서가 현재 대출 중이 아니지만 예약 우선 순위가 1순위가 아니므로 대출 불가능.
            $_SESSION['result'] = 'alreadyReserved';
            break;
          }
        }
        //한글질의문: 해당 도서를 대출 상태로 변경한다. 반납 일자는 당일로부터 10일 뒤 이다.
        $statement = "UPDATE EBOOK SET
                      CNO =?, EXTTIMES = 0,
                      DATERENTED = SYSDATE, DATEDUE = SYSDATE + 10, RESERVATION=NULL
                      WHERE ISBN =?";
        $stmt = $conn -> prepare($statement);
        $stmt -> execute(array($cno, $isbn));
        $_SESSION['result'] = 'rentSuccess';
        break;

    case 'reserve': //예약 버튼을 눌렀을 경우
        //한글질의문: 회원이 해당 도서를 예약 중이라면 가져오라.
        $stmt = $conn -> prepare("SELECT * FROM RESERVE WHERE ISBN=? AND CNO=?");
        $stmt -> execute(array($isbn, $cno));
        if($result = $stmt -> fetchAll()) { //해당 도서를 이미 예약 중이므로 돌아간다.
          $_SESSION['result'] = 'iReserved';
          break;
        }
        //한글질의문: 해당 도서가 현재 대출 중이라면 가져오라.
        $stmt = $conn -> prepare("SELECT * FROM EBOOK WHERE ISBN=? AND CNO IS NOT NULL");
        $stmt -> execute(array($isbn));
        if(!($result = $stmt -> fetchAll())) { //해당 도서가 대출 중이 아니므로 돌아간다.
          $stmt = $conn -> prepare("SELECT * FROM RESERVE WHERE ISBN=?");
          $stmt -> execute(array($isbn));
          if(!($result = $stmt -> fetchAll())) {//대출 중이 아니고 예약도 없다면
            $_SESSION['result'] = 'whywontyourent';
            break;
          }
        }
        //한글질의문: 회원이 해당 도서를 대출 중이라면 가져오라.
        $stmt = $conn -> prepare("SELECT * FROM EBOOK WHERE ISBN=? AND CNO=?");
        $stmt -> execute(array($isbn, $cno));
        if($result = $stmt -> fetchAll()) { //해당 도서를 이미 대출 중이므로 돌아간다.
          $_SESSION['result'] = 'youRented';
          break;
        }
        //한글질의문: 회원의 현재 예약 중인 도서 수를 가져오라.
        $stmt = $conn -> prepare("SELECT COUNT(*) FROM RESERVE WHERE CNO=?");
        $stmt -> execute(array($cno));
        $result = $stmt -> fetch();
        if($result[0] >= 3) { //이미 3권 까지 예약했으므로 뒤로 돌아간다.
          $_SESSION['result'] = '3reserves';
          break;
        }
        //한글질의문: 해당 도서의 예약 사항을 추가한다.
        $statement = "INSERT INTO RESERVE
                      VALUES(?, ?, SYSDATE)";
        $stmt = $conn -> prepare($statement);
        $stmt -> execute(array($isbn, $cno));
        $_SESSION['result'] = 'reserveSuccess';
        break;

    case 'extend': //연장 버튼을 눌렀을 경우
        //한글질의문: 해당 도서의 대출 연장 횟수를 가져오라.
        $stmt = $conn -> prepare("SELECT EXTTIMES FROM EBOOK WHERE ISBN=?");
        $stmt -> execute(array($isbn));
        $result = $stmt -> fetch();
        if($result[0] >= 2) { //이미 2회 까지 대출 연장 했으므로 돌아간다.
          $_SESSION['mypage'] ='extLimit';
          break;
        }
        //한글질의문: 해당 도서의 예약 상항을 가져오라.
        $stmt = $conn -> prepare("SELECT * FROM RESERVE WHERE ISBN=?");
        $stmt -> execute(array($isbn));
        if($result = $stmt -> fetchAll()) { //해당 도서가 예약 되있으므로 연장이 불가능하니 돌아간다.
          $_SESSION['mypage'] = 'noExtendCauseReserved';
          break;
        }
        //한글질의문: 해당 도서의 대출 연장 횟수를 1 증가하고 반납 날짜를 10일 증가시켜라.
        $stmt = $conn -> prepare("UPDATE EBOOK SET EXTTIMES=EXTTIMES+1, DATEDUE=DATEDUE+10 WHERE ISBN=?");
        $stmt -> execute(array($isbn));
        $_SESSION['mypage'] ='extSuccess';
        break;

    case 'cancel': //예약 취소 버튼을 눌렀을 경우
        //한글 질의문: 해당 도서를 예약한 회원들 중 가장 우선순위가 높은 회원을 가져오라.
        $stmt = $conn -> prepare("SELECT CNO FROM (SELECT * FROM RESINFO WHERE ISBN =? ORDER BY DATETIME) WHERE ROWNUM<=1");
        $stmt -> execute(array($isbn));
        $first = $stmt -> fetch();//변수에 저장해 놓고 취소한 사람이 예약 1순위였는지 검사하는데 사용한다.
        //한글질의문: 해당 예약 사항을 삭제하라.
        $stmt = $conn -> prepare("DELETE FROM RESERVE WHERE CNO=? AND ISBN=?");
        $stmt -> execute(array($cno,$isbn));
        $_SESSION['mypage'] ='cancelSuccess';//예약 취소는 성공했다. 앞으로는 메일 전송에 관련된 코드이다.
        //한글질의문: 해당 도서가 현재 대출 중이 아닌가?
        $stmt = $conn -> prepare("SELECT * FROM EBOOK WHERE ISBN=? AND CNO IS NULL");
        $stmt -> execute(array($isbn));
        if($result = $stmt -> fetch()) { //해당 도서가 현재 대출 중이 아니라면
          //한글질의문: 해당 도서의 예약 사항을 가져오라.
          $stmt = $conn -> prepare("SELECT * FROM RESERVE WHERE ISBN=?");
          $stmt -> execute(array($isbn));
          if($first[0]==$cno) { //취소한 사람이 1순위 였다면
            if($result = $stmt -> fetch()) { //방금 예약 취소한 도서의 예약 내용이 있다면
              //한글 질의문: 해당 도서를 예약한 회원들 중 가장 우선순위가 높은 회원을 가져오라.
              $stmt = $conn -> prepare("SELECT NAME, EMAIL, TITLE, CNO FROM (SELECT * FROM RESINFO WHERE ISBN =? ORDER BY DATETIME) WHERE ROWNUM<=1");
              $stmt -> execute(array($isbn));
              $temp = $stmt -> fetch();
              $_SESSION['name'] = $temp[0];//메일 전송을 위하여
              $_SESSION['email'] = $temp[1];//이름과 이메일
              $_SESSION['title'] = $temp[2];//서명을 저장.
              //한글질의문: 가장 우선순위가 높은 회원이 현재 해당 도서를 대출할 권리가 있다.
              $stmt = $conn -> prepare("UPDATE EBOOK SET RESERVATION=? WHERE ISBN=?");
              $stmt -> execute(array($temp[3], $isbn));
              include("mail/mail.php");//메일 전송.
            }
            else { //남은 예약 내용이 없다면
              //한글 질의문: 해당 도서의 예약 토큰을 삭제.
              $stmt = $conn -> prepare("UPDATE EBOOK SET RESERVATION=NULL WHERE ISBN=?");
              $stmt -> execute(array($isbn));
            }
          }
        }
        break;

    case 'return': //반납 버튼을 눌렀을 경우
        $stmt = $conn -> prepare("INSERT INTO PREVIOUSRENTAL VALUES(?, (SELECT DATERENTED FROM EBOOK WHERE ISBN=?), SYSDATE, ?)");
        $stmt -> execute(array($isbn, $isbn, $cno));
        //한글질의문: 해당 도서를 대출 가능 상태로 변경(반납)한다.
        $statement = "UPDATE EBOOK SET
                      CNO = null, EXTTIMES = null,
                      DATERENTED = null, DATEDUE = null
                      WHERE ISBN =?";
        $stmt = $conn -> prepare($statement);
        $stmt -> execute(array($isbn));
        $_SESSION['mypage'] = 'returnSuccess';//반납은 성공했다. 앞으로는 메일 전송에 관련된 코드이다.
        //한글질의문: 해당 도서의 예약 상황을 가져오라.
        $stmt = $conn -> prepare("SELECT * FROM RESERVE WHERE ISBN=?");
        $stmt -> execute(array($isbn));
        if($result = $stmt -> fetch()) { //방금 반납한 도서의 예약 내용이 있다면
          //한글질의문: 해당 도서를 예약한 회원들 중 가장 우선순위가 높은 회원을 가져오라.
          $stmt = $conn -> prepare("SELECT NAME, EMAIL, TITLE, CNO FROM (SELECT * FROM RESINFO WHERE ISBN =? ORDER BY DATETIME) WHERE ROWNUM<=1");
          $stmt -> execute(array($isbn));
          $temp = $stmt -> fetch();
          $_SESSION['name'] = $temp[0];//메일 전송을 위하여
          $_SESSION['email'] = $temp[1];//이름과 이메일을 저장.
          $_SESSION['title'] = $temp[2];//서명을 저장.
          //한글질의문: 가장 우선순위가 높은 회원이 현재 해당 도서를 대출할 권리가 있다.
          $stmt = $conn -> prepare("UPDATE EBOOK SET RESERVATION=? WHERE ISBN=?");
          $stmt -> execute(array($temp[3], $isbn));
          include("mail/mail.php");//메일 전송.
        }
        break;
    }
  //어떤 case에서든 break가 걸리면 이 줄로 오게 된다.
  echo "<script> window.history.back(); </script>"; //이전 페이지(검색결과 페이지 혹은 마이페이지)로 돌아간다.
  }
}
?>
