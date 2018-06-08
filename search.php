<?php
$button=$_POST['submit'];
$input=$_POST['in'];
if(!$button)
{
	echo "you didn't submit";
}
else
{
	if(strlen($input)<=1)
	{
		echo "Search term is too short";
	}
	else
	{
		echo "you searched for <b> $input </b> <hr size='1'><br>";
		$host="192.168.0.78";
		$user="python";
		$pass="python";
		$db="journal";
		$conn=mysqli_connect($host, $user, $pass, $db);
		if (!$conn)
		{
    		die("Connection failed: " . mysqli_connect_error());
		}
		/*$search_explode=explode(" ", $input);
		$x=0;
		foreach ($search_explode as $search_each) 
		{
			$x++;
			$construct="";
			if($x==1)
			{
				$construct .="(Title LIKE '%$search_each%')";
			}
			else
			{
				$construct .="(OR ISSN LIKE '%$search_each%' OR EISSN LIKE '%$search_each%' OR Keywords LIKE '%$search_each%' OR Subjects LIKE '%$search_each%' OR Publisher LIKE '%$search_each%')";
			}
		}	*/
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
				#printf("%s %s", $rows["Title"],$rows["URL"]);
			}
		}
	}
}
#mysqli_close($conn);
?>
