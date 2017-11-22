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
echo "<p>Attempting: ";
foreach ($_GET['breachSelector'] as $selectedOption) {
    echo "<strong>" . $selectedOption . "</strong>\n";
    $sites = $sites . " " . $selectedOption;
}
echo "</p>";

// Call the command
$cmd = "python ../Authentication/Authenticator.py " . $user . " " . $pass . " " . $sites;
$output = shell_exec($cmd);
echo $cmd;
//echo "output:" . $output;
//$o = shell_exec("sudo python ../Authentication/Authenticate.py ikualloveryou 2609drag facebook");
//echo "o:" . $o;
//$e =  shell_exec("/usr/bin/python /var/www/html/EthicalHackingTeam2/Authentication/Authenticate.py 2>&1");
//echo "e:" . $e;
//echo shell_exec("pip install mechanize"); 
echo shell_exec("sudo -u ubuntu whoami 2>&1");
echo shell_exec("/var/www/html/EthicalHackingTeam2/Authentication/./Authenticate.py 2>&1");

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
