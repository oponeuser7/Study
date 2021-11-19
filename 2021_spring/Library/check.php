<?php
if(isset($_SESSION['mode'])&&isset($_SESSION['isbn'])) {//'mode'와 'isbn'이 정상적으로 수신 되었다면
	$isbn = $_SESSION['isbn']; //isbn 저장
	$cno = $_SESSION['uid']; //cno 저장
	switch($_SESSION['mode']) { //switch문을 통해 'mode'값에 따라 분기한다.
			case 'rent': //대출 버튼을 눌렀을 경우
					//한글질의문: 해당 도서가 현재 대출 중이라면 가져오라.
					$stmt = $conn -> prepare("SELECT * FROM EBOOK WHERE ISBN=? AND CNO IS NOT NULL");
					$stmt -> execute(array($isbn));
					if($result = $stmt -> fetchAll()) { //해당 도서가 이미 대출 중이므로 뒤로 돌아간다.
					break;
					}
					//한글질의문: 회원의 현재 대출 중인 도서 수를 가져오라.
					$stmt = $conn -> prepare("SELECT COUNT(*) FROM EBOOK WHERE CNO=?");
					$stmt -> execute(array($cno));
					$result = $stmt -> fetch();
					if($result[0] >= 3) {//이미 3권 까지 대출했으므로 뒤로 돌아간다.
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
						if($cno!=$temp[0]) {//해당 도서가 현재 대출 중이 아니지만 예약 우선 순위가 1순위가 아니므로 대출 불가능.
							break;
						}
					}
					$_SESSION['rent_available'] = true;
					break;

			case 'reserve':
					//한글질의문: 해당 도서가 현재 대출 중이라면 가져오라.
					$stmt = $conn -> prepare("SELECT * FROM EBOOK WHERE ISBN=? AND CNO IS NOT NULL");
					$stmt -> execute(array($isbn));
					if(!($result = $stmt -> fetchAll())) { //해당 도서가 대출 중이 아니므로 돌아간다.
						$stmt = $conn -> prepare("SELECT * FROM RESERVE WHERE ISBN=?");
						$stmt -> execute(array($isbn));
						if(!($result = $stmt -> fetchAll())) {//대출 중이 아니고 예약도 없다면
							break;
						}
					}
					//한글질의문: 회원이 해당 도서를 대출 중이라면 가져오라.
					$stmt = $conn -> prepare("SELECT * FROM EBOOK WHERE ISBN=? AND CNO=?");
					$stmt -> execute(array($isbn, $cno));
					if($result = $stmt -> fetchAll()) { //해당 도서를 이미 대출 중이므로 돌아간다.
						break;
					}
					//한글질의문: 회원이 해당 도서를 예약 중이라면 가져오라.
					$stmt = $conn -> prepare("SELECT * FROM RESERVE WHERE ISBN=? AND CNO=?");
					$stmt -> execute(array($isbn, $cno));
					if($result = $stmt -> fetchAll()) { //해당 도서를 이미 예약 중이므로 돌아간다.
						break;
					}
					//한글질의문: 회원의 현재 예약 중인 도서 수를 가져오라.
					$stmt = $conn -> prepare("SELECT COUNT(*) FROM RESERVE WHERE CNO=?");
					$stmt -> execute(array($cno));
					$result = $stmt -> fetch();
					if($result[0] >= 3) { //이미 3권 까지 예약했으므로 뒤로 돌아간다.
						break;
					}
					$_SESSION['reserve_available'] = true;
					break;
			
			case 'extend': //연장 버튼을 눌렀을 경우
				//한글질의문: 해당 도서의 대출 연장 횟수를 가져오라.
				$stmt = $conn -> prepare("SELECT EXTTIMES FROM EBOOK WHERE ISBN=?");
				$stmt -> execute(array($isbn));
				$result = $stmt -> fetch();
				if($result[0] >= 2) { //이미 2회 까지 대출 연장 했으므로 돌아간다.
					break;
				}
				//한글질의문: 해당 도서의 예약 상항을 가져오라.
				$stmt = $conn -> prepare("SELECT * FROM RESERVE WHERE ISBN=?");
				$stmt -> execute(array($isbn));
				if($result = $stmt -> fetchAll()) { //해당 도서가 예약 되있으므로 연장이 불가능하니 돌아간다.
					break;
				}
				$_SESSION['extend_available'] = true;
					break;
	}
}
?>