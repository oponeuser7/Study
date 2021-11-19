<?php
  include("config/session.php");
  if(!isset($_SESSION['uid'])||!isset($_SESSION['pwd'])||$_SESSION['uid']!=32594) {
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
      <title>statistics</title>
    </head>
    <body>
    <h2 id='texts' style='font-size:30px; color:#FF8C00'>Best Customer</h2>
      <table>
        <thread>
          <tr id='texts'>
            <th>Who</th>
            <th>Overall Rents</th>
          </tr>
        <thread>
        <tbody>
          <?php
          $statement = "SELECT C.NAME, COUNT(*)
                        FROM CUSTOMER C, PREVIOUSRENTAL P
                        WHERE P.CNO = C.CNO
                        GROUP BY C.NAME
                        ORDER BY COUNT(*) DESC, C.NAME FETCH FIRST 1 ROW ONLY";
          $stmt = $conn -> prepare($statement);
          $stmt -> execute();
          if($row = $stmt -> fetch()) { ?>
            <tr id='inputbox' style="text-align: center">
              <td><?=$row[0]?></td>
              <td><?=$row[1]?></td>
            <tr>
            <?php
          }
          ?>
        </tbody>
      </table>
      <h2 id='texts' style='font-size:30px; color:#008B8B'>Rollup</h2>
      <table>
        <thread>
          <tr id='texts'>
            <th>Customer</th>
            <th>Title</th>
            <th>Rent Counts</th>
          </tr>
        <thread>
        <tbody>
          <?php
          $statement = "SELECT
                        CASE GROUPING(C.NAME) WHEN 1 THEN 'Overall Customers' ELSE C.NAME END,
                        CASE GROUPING(E.TITLE) WHEN 1 THEN 'Overall Rents' ELSE E.TITLE END,
                        COUNT(*)
                        FROM PREVIOUSRENTAL P, EBOOK E, CUSTOMER C
                        WHERE P.ISBN = E.ISBN AND P.CNO = C.CNO
                        GROUP BY ROLLUP(C.NAME, E.TITLE)";
          $stmt = $conn -> prepare($statement);
          $stmt -> execute();
          while($row = $stmt -> fetch()) { ?>
            <tr id='inputbox' style="text-align: center">
              <td><?=$row[0]?></td>
              <td><?=$row[1]?></td>
              <td><?=$row[2]?></td>
            <tr>
            <?php
          }
          ?>
        </tbody>
      </table>
    <body>
    <h2 id='texts' style='font-size:30px; color:#8A2BE2'>Ratio</h2>
      <table>
        <thread>
          <tr id='texts'>
            <th>Book(ISBN)</th>
            <th>Rent Counts</th>
            <th>Ratio</th>
          </tr>
        <thread>
        <tbody>
          <?php
          $statement = "SELECT ISBN, COUNT(*),
                        ROUND(RATIO_TO_REPORT(COUNT(*)) OVER (),2)
                        FROM PREVIOUSRENTAL
                        GROUP BY ISBN";
          $stmt = $conn -> prepare($statement);
          $stmt -> execute();
          while($row = $stmt -> fetch()) { ?>
            <tr id='inputbox' style="text-align: center">
              <td><?=$row[0]?></td>
              <td><?=$row[1]?></td>
              <td><?=$row[2]?></td>
            <tr>
            <?php
          }
          ?>
        </tbody>
      </table>
  <?php
  }
  ?>
