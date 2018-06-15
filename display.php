<?php
include("headfoot.html")
?>		
<?php
 header('Content-type: text/html; charset=utf-8');
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
		$construct1= "SELECT * FROM doaj WHERE (Title LIKE '%$input%' OR ISSN LIKE '%$input%' OR EISSN LIKE '%$input%' OR Keywords LIKE '%$input%' OR Subjects LIKE '%$input%' OR Publisher LIKE '%$input%')";

		$res=mysqli_query($conn, $construct);
		$res1=mysqli_query($conn, $construct1);
		$num=mysqli_num_rows($res);
		if($num==0)
		{
			echo "No Article Availabe For $input <br>";
		}
		else
		{
			echo "$num results found for articles <br><br>";
			while($rows=mysqli_fetch_assoc($res))
			{
				$title=$rows ['title'];
				$link=$rows ['link'];
				$jlink=$rows ['j_link'];
				$jtitle=$rows ['j_title'];
				$author=$rows ['author'];
				$sum=$rows ['summary'];
				$vol=$rows ['volume'];
				$iss=$rows ['issue'];
				$pdf=$rows ['pdf_link'];
				$lim=substr($sum, 0, 250);
				if($pdf=="")
				{
					echo "<a href='$link'> <b> $title </b> </a>  <br><a href='$jlink'><b>Journal:- $jtitle </b></a> <br>Author:- $author &nbsp&nbsp&nbsp Volume:- $vol &nbsp&nbsp&nbsp Issue:- $iss<br>Summary:- $lim....<br> PDF link not available <br><br><br>";
				}
				else{
					echo "<a href='$link'> <b> $title </b> </a>  <br><a href='$jlink'><b>Journal:- $jtitle </b></a> <br>Author:- $author &nbsp&nbsp&nbsp Volume:- $vol &nbsp&nbsp&nbsp Issue:- $iss<br>Summary:- $lim....<br><a href='$pdf'>Click here</a>for PDF <br><br><br>";
				}
			}
				
		}
		$num1=mysqli_num_rows($res1);
		if($num1==0)
		{
			echo "No Journals Availabe For $input";
		}
		else
		{
			echo "$num1 results found journals <br><br>";
			while($rows1=mysqli_fetch_assoc($res1))
			{
				$title=$rows1 ['Title'];
				$url=$rows1 ['URL'];
				$issn=$rows1 ['ISSN'];
				$eissn=$rows1 ['EISSN'];
				$date=$rows1 ['Add_Date'];
				$sub=$rows1 ['Subjects'];
				$pub=$rows1 ['Publisher'];
				$key=$rows1 ['Keywords'];
				echo "<a href='$url'> <b> $title </b> </a> <br> <a href='$url'> $url </a> <br>keywords:- $key <br>ISSN:- $issn <br>EISSN:- $eissn <br>Subject:- $sub <br>Publisher:- $pub<br><br>";
				#printf("%s %s", $rows["Title"],$rows["URL"]);
			}
		}
	}
}
#mysqli_close($conn);
?>
