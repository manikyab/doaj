<html>
	<head>
		<style>
			table,td
			{
				border-collapse: collapse;
				border: 1px solid black;
				border-spacing: 10px;
			}
			td
			{
				text-align: left;
				padding: 10px;
			}
		</style>
	</head>
	<body>
		<?php
            // for the datbase connectivity
			$mysqli=new mysqli(‘192.168.0.06’, ‘root’, ‘’, ‘journal’);
			if ($conn->connect_error) 
			{
			    die("Connection failed: " . $conn->connect_error);
			}
			//take the input from user
			$input=$_POST['in'];

			//query thatbhas to be run
			$query=SELECT * FROM doaj WHERE Author REGEXP ‘$input+’ OR Category REGEXP ‘$input+’ OR Journal_Title REGEXP ‘$input+’ OR keywords REGEXP ‘$input+’ OR Journal_ISSN REGEXP '$input+' OR Journal_EISSN REGEXP '$input+';

			//query excecuted
			$res=$mysqli->query($query);

			if($res->num_rows > 0)
			{
				echo “<table>”;

				//for fetching and display the data 
				while($row=mysqli_fetch_array($res))
				{
					echo “ <tr>”;
					echo “<td>”;
					echo $row[‘Journal_Title’] ;
					echo "<br>";
					echo "<a href= "$row['Journal_URL']"> Click for more information </a>";
					echo "<br>"; 
					echo $row['keywords'];
					echo "<br>";
					echo "print version:- " $row['Journal_ISSN']; 
					echo "online version:- " $row['Journal_EISSN'];
					echo $row['Text_formats'];
					echo "<br>";
					echo $row['Publisher'];
					echo "Added Date:-" $row['added_date'];
					echo "<br>";
					echo $row['Subjects'];
					echo “</td>”;
					echo “</tr>”
				}
				echo “</table>”;
			}
			else
			{
				echo " No Result ";
			}
			$mysqli->close();
		?>
	</body>
</html>