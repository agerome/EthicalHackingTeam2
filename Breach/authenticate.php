<?php 

$servername = "localhost";
$username = "root";
$password = "ethicalhacking";
$db = "ethicalhackingteam2";

// Create connection
$conn = mysqli_connect($servername, $username, $password, $db);

// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

// Display the breach statistics - all of the users
echo "<h3>Overall Breach Statistics:</h3>";
$all = "SELECT * FROM " . $db;
$result = mysqli_query($conn, $all);

if (!$result) {
    die("Grabbing the entire table failed " . mysqli_error($conn)); 
}

// Format bool that is given from MySQL
function displayBool($value) {
    return $value != 0 ? "True" : "False";
}

// Create table to display statistics
echo "<table>
	<tr>
	    <th>Username</th>
	    <th>Password</th>
            <th>Twitch</th>
 	    <th>Amazon</th>
 	    <th>YouTube</th>
 	    <th>Facebook</th>
 	    <th>Twitter</th>
 	    <th>Pinterest</th>
 	</tr>";

while ($row = mysqli_fetch_array($result)) {
    echo "<tr>
              <td>" . $row['username'] . "</td>
 	      <td>" . $row['password'] . "</td>
 	      <td>" . displayBool($row['sites_breached_twitch']) . "</td>
 	      <td>" . displayBool($row['sites_breached_amazon']) . "</td>
 	      <td>" . displayBool($row['sites_breached_youtube']) . "</td>
   	      <td>" . displayBool($row['sites_breached_facebook']) . "</td>
   	      <td>" . displayBool($row['sites_breached_twitter']) . "</td>
 	      <td>" . displayBool($row['sites_breached_pinterest']) . "</td>
  	  </tr>";
} 

echo "</table>";

mysqli_close();
?>