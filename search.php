<html>
<head>
	<style>
		table
		{
			border-collapse: collapse;
			width: 100%;
			border: 1px solid black;
		}
		th,td
		{
			text-align: left;
			padding: 8px;
			border: 1px solid black;
		}
	</style>
</head>>
<body>

<?php

$mysqli=new mysqli(‘localhost’, ‘root’, ‘’, ‘journal’);
if ($conn->connect_error) 
{
    die("Connection failed: " . $conn->connect_error);
}


$input=$_POST['in'];

$query=SELECT * FROM doaj WHERE Author REGEXP ‘$input+’ OR Category REGEXP ‘$input+’ OR Title REGEXP ‘$input+’ OR keywords REGEXP ‘$input+’ OR ISSN REGEXP '$input+' OR EISSN REGEXP '$input+';

$res=$mysqli->query($query);

if($res->num_rows > 0)
{
echo “<table> 
<tr>
<th> Author </th>
<th> Category </th>
<th> Content </th>
<th> Link A </th>
<th> Link R </th>
<th> Summary </th>
<th> Title </th>
<th> Updated </th>
</tr>”;

while($row=mysqli_fetch_array($res))
{
echo “ <tr>”;
echo “<td>” . $row[‘............’] . “</td>”;
echo “<td>” . $row[‘............’] . “</td>”;
echo “<td>” . $row[‘............’] . “</td>”;
echo “<td>” . $row[‘............’] . “</td>”;
echo “<td>” . $row[‘............’] . “</td>”;
echo “<td>” . $row[‘............’] . “</td>”;
echo “<td>” . $row[‘............’] . “</td>”;
echo “<td>” . $row[‘............’] . “</td>”;
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