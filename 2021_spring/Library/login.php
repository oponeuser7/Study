<?php require('db_connect.php'); ?>
<!DOCTYPE html>
<html lang="kr">
  <head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="style.css">
    <title>Login_Page</title>
    <?php
      include("config/session.php");//로그인 후에 다시 로그인 페이지로 돌아왔다면
      session_destroy();//세션을 종료시켜 자동 로그아웃 되게 만듭니다.
      if(isset($_POST['uid'])&&isset($_POST['pwd'])){/*이 페이지로 post가 보내졌다면*/
        $username=$_POST['uid'];//아이디 저장
        $userpw=$_POST['pwd'];//비밀번호 저장
        $stmt = $conn -> prepare("SELECT * FROM CUSTOMER WHERE CNO=? AND PASSWD=?");//질의 준비
        $stmt -> execute(array($username, $userpw));//질의 실행
        if($result = $stmt -> fetchAll()) {/*아이디와 비밀번호가 데이터베이스와 일치한다면*/
          include("config/session.php");//새로운 세션을 시작
          $_SESSION['uid'] = $username;//아이디를 세션에 저장
          $_SESSION['pwd'] = $userpw;//비밀번호를 세션에 저장
          header("Location: main.php");//메인페이지로 이동
        }
        else {//아이디나 비밀번호가 틀렸을 시
          echo "<script>alert('아이디 또는 비밀번호가 틀렸습니다.');</script>";
        }
      }
    ?>
  </head>
  <body>
    <div id='center'>
      <form method="post"><!--현재 페이지로 post를 보낸다-->
        <div style='font-family: Comic Sans MS'>CUSTOMER NUMBER :</div> <input type="text" id='inputbox' name="uid" /></br><!--CNO-->
        <div style='font-family: Comic Sans MS'>PASSWORD :</div> <input type="password" id='inputbox' name="pwd" /></br></br><!--PASSWD-->
        <input type="submit" id='butt' style='position: relative; left:90px;' value="LOGIN" /><!--로그인 버튼-->
      </form>
    </div>
  </body>
</html>
