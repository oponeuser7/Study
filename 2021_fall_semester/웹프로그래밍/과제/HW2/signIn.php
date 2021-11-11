<?php
    session_start();
    $id = $_POST["id"];
    $password = $_POST["password"];
    $file = fopen("data/person.json", "r");
    while(!feof($file)) {
        $person = json_decode(trim(fgets($file)));
        if($person->id===$id && $person->password===$password) {
            $_SESSION["id"] = $id;
            $_SESSION["password"] = $password;
            echo "success";
            break;
        }
    }
    fclose($file);
?>