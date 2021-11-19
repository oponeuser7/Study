<?php
    session_start();
    $id = $_SESSION["id"];
    $bookNames = $_POST["bookNames"];
    $rentList = [];
    $bookList = [];
    $file = fopen("data/rentList.json", "r");
    while(!feof($file)) {
        $flag = true;
        $temp = json_decode(trim(fgets($file)));
        foreach($bookNames as $bookName) {
            if($temp->bookName===$bookName) {
                $flag = false;
                break;
            }
        }
        if($flag) $rentList[] = json_encode($temp, JSON_UNESCAPED_UNICODE);
    }
    fclose($file);
    $file = fopen("data/bookList.json", "r");
    while(!feof($file)) {
        $temp = trim(fgets($file));
        if($temp) $bookList[] = $temp;
    }
    fclose($file);
    for($i=0; $i<count($bookList); $i++) {
        $temp = json_decode($bookList[$i]);
        foreach($bookNames as $bookName) {
            if($temp->title===$bookName) {
                $temp->rental = "keep";
                $bookList[$i] = json_encode($temp, JSON_UNESCAPED_UNICODE);
                break;
            }
        }
    }
    $file = fopen("data/rentList.json", "w");
    fwrite($file, implode("\n", $rentList));
    fclose($file);
    $file = fopen("data/bookList.json", "w");
    fwrite($file, implode("\n", $bookList));
    fclose($file);
?>