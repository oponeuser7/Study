<?php
include("config/session.php");
if(!isset($_SESSION['uid'])||!isset($_SESSION['pwd'])) {
  //로그인 하지 않고 이 페이지에 접근했다면 로그인 페이지로 퇴출시킨다.
  header("Location: login.php");
}
else {
?>
  <!DOCTYPE html>
  <html lang="kr">
    <head>
      <meta charset="utf-8">
      <link rel="stylesheet" href="style.css">
      <title>Main_Page</title>
    </head>
    <body id='texts'>
      <?php
      //관리자만 볼 수 있는 버튼이다. admin 페이지를 연다. 현재 관리자는 32594 회원이다.
      if($_SESSION['uid']==32594) { ?>
        <input type="button" id='butt' onclick="window.open('admin.php', '_blank')" value="Admin Only" />
        <input type="button" id='butt' onclick="window.open('statistics.php', '_blank')" value="Statistics" />
        <?php
      }
      ?>
      <button type="button" id='butt' onclick="document.location.href='mypage.php'">My Page</button>
      <button type="button" id='butt' onclick="document.location.href='login.php'">Logout</button>
      <br><br>
      <form action="result.php" method="get">
        <strong>Title</strong><!--서명-->
        <select id='butt' name="op1"><!--NOT 연산자-->
          <option value="" selected="selected">is</option>
          <option value="!">is NOT</option>
        </select>
        <input type="text" id='inputbox' style='font-size:25px' name="title">
        <select id='butt' name="op2"><!--AND,OR 연산자-->
          <option value="OR" selected="selected">OR</option>
          <option value="AND">AND</option>
        </select><br>
        <strong>Author</strong><!--작가-->
        <select id='butt' name="op3"><!--NOT 연산자-->
          <option value="" selected="selected">is</option>
          <option value="!">is NOT</option>
        </select>
        <input type="text" id='inputbox' style='font-size:25px' name="author">
        <select id='butt' name="op4"><!--AND,OR 연산자-->
          <option value="OR" selected="selected">OR</option>
          <option value="AND">AND</option>
        </select><br>
        <strong>Publisher</strong><!--출판사-->
        <select id='butt' name="op5"><!--NOT 연산자-->
          <option value="" selected="selected">is</option>
          <option value="!">is NOT</option>
        </select>
        <input type="text" id='inputbox' style='font-size:25px' name="publisher">
        <select id='butt' name="op6"><!--AND,OR 연산자-->
          <option value="OR" selected="selected">OR</option>
          <option value="AND">AND</option>
        </select><br>
        <strong>Year</strong><!--출판년도-->
        <select id='butt' name="op7"><!--NOT 연산자-->
          <option value="" selected="selected">is</option>
          <option value="NOT">is NOT</option>
        </select> between <!--between from to-->
        <input type="date" id='inputbox' style='font-size:25px' name="from">
         and <input type="date" id='inputbox' style='font-size:25px' name="to"><br><br>
         <input type="submit" id='butt' value="Search!"><!--검색버튼-->
      </form>
    </body>
  <html>
<?php } ?>
