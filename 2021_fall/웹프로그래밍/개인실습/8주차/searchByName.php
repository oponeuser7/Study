<?php
    if(isset($_GET["name"])) {
        $name = $_GET["name"];
        $result = new stdClass();
        $index = 0;
        $file = fopen("data.json", "r");
        while(!feof($file)) {
            $line = trim(fgets($file));
            $temp = json_decode($line);
            if(strpos(strtolower($temp->name), strtolower($name))!==false) {
                $result->$index = $temp;
                $index++;
            }
        }
        fclose($file);
        echo json_encode($result);
    }
?>
