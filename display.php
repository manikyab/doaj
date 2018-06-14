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
		$host="192.168.1.48";
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
		$construct= "SELECT * FROM article WHERE (title LIKE '%$input%' OR author LIKE '%$input%')";
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
				$title=$rows ['title'];
				$link=$rows ['link'];
				$jlink=$rows ['j_link'];
				$jtitle=$rows ['j_title'];
				$author=$rows ['author'];
				$sum=$rows ['summary'];
				$lim=substr($sum, 0 ,200);
				echo "<a href='$link'> <b> $title </b> </a> <br> <a href='$link'> $link </a> <br>Journal:- $jtitle &nbsp&nbsp&nbsp Author:- $author <br>Summary:- $lim...... <br><br>";
				#printf("%s %s", $rows["Title"],$rows["URL"]);
			}
		}
	}
}
#mysqli_close($conn);
?>
