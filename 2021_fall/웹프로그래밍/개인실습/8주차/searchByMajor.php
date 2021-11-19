<?php
    if(isset($_GET["major"])) {
        $major = $_GET["major"];
        $result = new stdClass();
        $index = 0;
        $file = fopen("data.json", "r");
        while(!feof($file)) {
            $line = trim(fgets($file));
            $temp = json_decode($line);
            if($temp->major===$major) {
                $result->$index = $temp;
                $index++;
            }
        }
        fclose($file);
        echo json_encode($result);
    }
?>
