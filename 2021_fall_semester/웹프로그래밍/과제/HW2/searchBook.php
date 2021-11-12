<?php
    $data = $_GET["data"];
    $result = new stdClass();
    $index = 0;
    $file = fopen("data/bookList.json", "r");
    while(!feof($file)) {
        $temp = trim(fgets($file));
        if($temp) {
            $book = json_decode($temp);
            $titleMatch = strpos($book->title,$data)!==false;
            $authorsMatch = false;
            $publishDateMatch = strpos($book->publishDate,$data)!==false;
            $publisherMatch = strpos($book->publisher,$data)!==false;
            foreach($book->authors as $author) if(strpos($author,$data)!==false) $authorMatch = true;
            if($titleMatch || $authorsMatch || $publishDateMatch || $publisherMatch) {
                $result->$index = $book;
                $index++;
            }
        }
    }
    fclose($file);
    echo json_encode($result);
?>