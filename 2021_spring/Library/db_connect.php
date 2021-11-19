<?php
/*데이터베이스 접속*/
$tns = "(DESCRIPTION= (ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))
      (CONNECT_DATA= (SERVICE_NAME=XE))
)";
$dsn = "oci:dbname=".$tns.";charset=utf8";
$username = 'd201702007';
$password = '180502';
try {
$conn = new PDO($dsn, $username, $password);
}
catch (PDOException $e) {
  echo("에러 내용: ".$e -> getMessage());
}
?>
