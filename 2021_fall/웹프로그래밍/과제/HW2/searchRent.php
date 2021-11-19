<?php
    session_start();
    $id = $_SESSION["id"];
    $result = new stdClass();
    $index = 0;
    $file = fopen("data/rentList.json", "r");
    while(!feof($file)) {
        $rent = json_decode(trim(fgets($file)));
        if($rent->id===$id) {
            $result->$index = $rent;
            $index++;
        }
    }
    fclose($file);
    echo json_encode($result, JSON_UNESCAPED_UNICODE);
?>
