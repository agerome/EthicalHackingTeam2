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




// Call authentication script on the selected values
$user = $_POST['email'];
$pass = $_POST['pass'];
echo "<h3>Authentication:</h3>";

 
echo "<p>Username: <strong>" . $user . "</strong>, Password: <strong>" . $pass . "</strong></p>";

$sites = "facebook dribbble github tumblr theguardian";
echo "<p>Attempting on: ";
$cmd = "/var/www/html/EthicalHackingTeam2/Authentication/./Authenticate.py '" . $user . "' '" . $pass . "' " . $sites . " 2>&1";
$output = shell_exec($cmd);
echo $output;

echo "</p>";


echo "<p> Now sending result file to </p>" . $user;



?>
