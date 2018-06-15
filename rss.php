<?php

$button=$_POST['submit'];
$input=$_POST['link'];
echo "Please wait while uploading";
$command = "python rss_insert.py $input";
$result=exec("python rss_insert.py $input");

echo "$result";
sleep(5);
header("main.html");
?>