<?php
$button=$_POST['submit'];
$input=$_POST['in'];
if(!$button)
{
	echo "you didn't submit";
}
else
{
	echo "<center> <h1> <br><br><br><br> My Search Engine </h1> <form method="POST" action="search.php" > <input type="text" name="in"><br><br> <input type="submit" name="submit" value="Search"><br><br><br><br><br> </form> </center> <br><br>"
	if(strlen($input)<=1)
	{
		echo "Search term is too short";
	}
	else
	{
		echo "you searched for <b> $input </b> <hr size='1'><br>";
		$host="192.168.0.79";
		$user="python";
		$pass="python";
		$db="journal";
		$conn=mysqli_connect($host, $user, $pass, $db);
		if (!$conn)
		{
    		die("Connection failed: " . mysqli_connect_error());
		}
		$construct= "SELECT * FROM doaj WHERE (Title LIKE '%$input%' OR ISSN LIKE '%$input%' OR EISSN LIKE '%$input%' OR Keywords LIKE '%$input%' OR Subjects LIKE '%$input%' OR Publisher LIKE '%$input%')";
		$res=mysqli_query($conn, $construct);
		$num=mysqli_num_rows($res);
		if($num==0)
		{
			echo "There are no matching result for <b> $input </b>.<br><br> 1. Try more general words. for example: If you want to search 'how to create a website' then use general keyword like 'create' 'website' <br> 2. Try different words with similar meaning <br> 3. Please check your spelling";
		}
		else
		{
			echo "$num results found <br><br><br>";
			while($rows=mysqli_fetch_assoc($res))
			{
				$title=$rows ['Title'];
				$url=$rows ['URL'];
				$issn=$rows ['ISSN'];
				$eissn=$rows ['EISSN'];
				$date=$rows ['Add_Date'];
				$sub=$rows ['Subjects'];
				$pub=$rows ['Publisher'];
				$key=$rows ['Keywords'];
				echo "<a href='$url'> <b> $title </b> </a> <br> <a href='$url'> $url </a> <br>keywords:- $key <br>ISSN:- $issn <br>EISSN:- $eissn <br>Subject:- $sub <br>Publisher:- $pub<br><br>";
			}
		}
	}
}
#mysqli_close($conn);
?>