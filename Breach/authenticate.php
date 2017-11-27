<?php 

// Add syle
echo "<style>
table {
 font-family: arial, sans-serif;
    border-collapse: collapse;
    width: 50%;
}
td, th {
    border: 1px solid black;
    text-align: left;
    padding: 8px;
}  
tr:nth-child(even) {
    background-color: #dddddd;
}
</style>";   

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

// Call authentication script on the selected values
$user = $_GET['username'];
$pass = $_GET['password'];
echo "<h3>Authentication:</h3>";

 
echo "<p>Username: <strong>" . $user . "</strong>, Password: <strong>" . $pass . "</strong></p>";

$sites = "";
echo "<p>Attempting on: ";
foreach ($_GET['breachSelector'] as $selectedOption) {
    echo "<strong>" . $selectedOption . ",</strong>\n";
    $sites = $sites . " " . $selectedOption;
}
echo "</p>";

// Call command
$cmd = "/var/www/html/EthicalHackingTeam2/Authentication/./Authenticate.py '" . $user . "' '" . $pass . "' " . $sites . " 2>&1";
// echo $cmd;
$output = shell_exec($cmd);
echo $output;

// Display the breach statistics - all of the users
echo "<h3>Overall Breach Statistics:</h3>";
$all = "SELECT * FROM " . $db;
$result = mysqli_query($conn, $all);

if (!$result) {
    die("Grabbing the entire table failed " . mysqli_error($conn)); 
}

// Format bool that is given from MySQL
function displayBool($value) {
    return $value != 0 ? "Success" : "Failed";
}

// Create table to display statistics
echo "<table>
	<tr>
	    <th>Username</th>
	    <th>Password</th>
        <th>Facebook</th>
 	    <th>Zipcar</th>
 	    <th>Ebay</th>
 	    <th>Tumblr</th>
 	    <th>Netflix</th>
 	</tr>";

while ($row = mysqli_fetch_array($result)) {
    echo "<tr>
          <td>" . $row['username'] . "</td>
 	      <td>" . $row['password'] . "</td>
 	      <td>" . displayBool($row['sites_breached_facebook']) . "</td>
 	      <td>" . displayBool($row['sites_breached_zipcar']) . "</td>
 	      <td>" . displayBool($row['sites_breached_ebay']) . "</td>
   	      <td>" . displayBool($row['sites_breached_tumblr']) . "</td>
   	      <td>" . displayBool($row['sites_breached_netflix']) . "</td>
  	  </tr>";
} 

echo "</table>";

mysqli_close();
?>
