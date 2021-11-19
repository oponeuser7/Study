<?php
    $person = new stdClass();
    $person->id = $_POST["id"];
    $person->password = $_POST["password"];
    $file = fopen("data/person.json", "r");
    $content = [];
    while(!feof($file)) {
        $temp = trim(fgets($file));
        if($temp) $content[] = $temp;
    }
    fclose($file);
    $content[] = json_encode($person);
    $file = fopen("data/person.json", "w");
    fwrite($file, implode("\n", $content));
    fclose($file);
?>