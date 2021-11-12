<?php
    session_start();
    $id = $_SESSION["id"];
    $bookNames = $_POST["bookNames"];
    $rentalDates = $_POST["rentalDates"];
    $rentList = [];
    $bookList = [];
    $file = fopen("data/rentList.json", "r");
    while(!feof($file)) {
        $temp = trim(fgets($file));
        if($temp) $rentList[] = $temp;
    }
    fclose($file);
    $file = fopen("data/bookList.json", "r");
    while(!feof($file)) {
        $temp = trim(fgets($file));
        if($temp) $bookList[] = $temp;
    }
    fclose($file);
    for($i=0; $i<count($bookNames); $i++) {
        $rent = new stdClass();
        $rent->id = $id;
        $rent->bookName = $bookNames[$i];
        $rent->rental = $rentalDates[$i];
        $rentList[] = json_encode($rent, JSON_UNESCAPED_UNICODE);
    }
    for($i=0; $i<count($bookList); $i++) {
        $temp = json_decode($bookList[$i]);
        foreach($bookNames as $bookName) {
            if($temp->title===$bookName) {
                $temp->rental = "rented";
                $bookList[$i] = json_encode($temp, JSON_UNESCAPED_UNICODE);
                break;
            }
        }
    }
    print_r($rentList);
    $file = fopen("data/rentList.json", "w");
    fwrite($file, implode("\n", $rentList));
    fclose($file);
    $file = fopen("data/bookList.json", "w");
    fwrite($file, implode("\n", $bookList));
    fclose($file);
?>