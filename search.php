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
		echo "you searched for <b> $input </b> <hr size='1'><br>"
		$host="192.168.0.78";
		$user="python";
		$pass="python";
		$db="journal";
		mysql_connect($host, $user, $pass);
		mysql_select_db($db);
		$search_explode=explode(" ", $input);
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
		}	
		$construct="SELECT * FROM doaj WHERE $construct";
		$res=mysql_query($construct);
		$num=mysql_num_rows($res);
		if($num==0)
		{
			echo "There are no matching result for <b> $input </b>.<br><br> 1. Try more general words. for example: If you want to search 'how to create a website' then use general keyword like 'create' 'website' <br> 2. Try different words with similar meaning <br> 3. Please check your spelling";
		}
		else
		{
			echo "$num results found";
			while($rows=mysql_fetch_assoc($res))
			{
				$title=$row ['Title'];
				$url=$row ['URL'];
				$iisn=$row ['IISN'];
				$eissn=$row ['EISSN'];
				$date=$row ['Add_Date'];
				$sub=$row ['Subjects'];
				$pub=$row ['Publishers'];
				$key=$row ['Keywords'];
				echo "<a href='$url'> <b> $title </b> </a> <br> <a href='$url'> $url </a> <br> $key <br> $issn <br> $eissn <br> $sub <br> $pub";
			}
		}
	}
}
?>
