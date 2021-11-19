<?php
header('P3P: CP="ALL CURa ADMa DEVa TAIa OUR BUS IND PHY ONL UNI PUR FIN COM NAV INT DEM CNT STA POL HEA PRE LOC OTC"');
// 세션 파일을 저장할 경로 설정.
ini_set('session.save_path',$_SERVER['DOCUMENT_ROOT']."/Library/session");
//브라우저가 종료되면 쿠키는 파기
ini_set('session.cookie_lifetime', 0) ;
// 사용되지 않는 세션 파기 유효 시간 설정.(초 단위)
ini_set('session.gc_maxlifetime', 1440);
// 서버에 저장된 세션 ID 활성화 시간.(분 단위)
ini_set('session.cache_expire', 180);
// 세션 시작
session_start();
?>
