<?php
    $target_dir = "uploads/";
    $target_file = $target_dir . basename($_FILES["img-file"]["name"]);
    $imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));
    if (file_exists($target_file)) {
        echo "Sorry, file already exists.";
    }
    else if($imageFileType != "jpg" && $imageFileType != "png" && $imageFileType != "jpeg" && $imageFileType != "gif" ) {
        echo "Sorry, only JPG, JPEG, PNG & GIF files are allowed.";
    }
    else {
        $book = new stdClass();
        $book->title = $_POST["title"];
        $book->authors = $_POST["authors"];
        $book->publishDate = $_POST["publish-date"];
        $book->publisher = $_POST["publisher"];
        $book->fileName = $_FILES["img-file"]["name"];
        $book->rental = "keep";
        $content = [];
        $file = fopen("data/bookList.json", "r");
        while(!feof($file)) {
            $temp = trim(fgets($file));
            if($temp) $content[] = $temp;
        }
        $content[] = json_encode($book, JSON_UNESCAPED_UNICODE);
        fclose($file);
        $file = fopen("data/bookList.json", "w");
        fwrite($file, implode("\n", $content));
        fclose($file);
        move_uploaded_file($_FILES["img-file"]["tmp_name"], $target_file);
        echo "저장되었습니다.";
    }
?>