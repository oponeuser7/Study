<?php
include("../config/session.php");
if(!isset($_SESSION['uid'])||!isset($_SESSION['pwd'])||!isset($_SESSION['name'])||!isset($_SESSION['email'])||!isset($_SESSION['title'])) {
  //로그인 하지 않고 이 페이지에 접근했다면 로그인 페이지로 퇴출시킨다.
  header("Location: login.php");
}
else {
  include "PHPMailer.php";
  include "SMTP.php";
  $mail = new PHPMailer(); //PHPMailer 인스턴스 생성
  $mail->CharSet = "UTF-8"; //UTF-8 인코딩을 사용해야 한글이 깨지지 않는다.
  $mail->isSMTP(); 
  $mail->SMTPDebug = SMTP::DEBUG_SERVER;
  $mail->Host = 'smtp.gmail.com';
  $mail->Port = 465;
  $mail->SMTPSecure = "ssl";
  $mail->SMTPAuth = true; 
  $mail->Username = 'oponeuser7@gmail.com'; //관리자 이메일
  $mail->Password = 'lavgin0801@'; //비밀번호는 제 프라이버시를 위해 생략하겠습니다.
  $mail->setFrom('oponeuser7@gmail.com', 'CNU Library'); //송신자 이메일 주소, 이름
  $mail->addAddress($_SESSION['email'], $_SESSION['name']); //수신자 이메일 주소, 이름
  $mail->Subject = '[CNU Library]예약 하신 도서가 반납되었습니다.'; //이메일의 제목
  //이메일의 내용
  $mail->AltBody = $_SESSION['name']."님이 예약하신 ".$_SESSION['title']."의 대출이 현재 가능합니다. 당일 자정까지 대출하지 않으면 예약 우선권이 사라집니다.";
  $mail->msgHTML($mail->AltBody);
  $mail->send();//전송
  unset($_SESSION['name']);
  unset($_SESSION['email']);
  unset($_SESSION['title']);
}
?>
