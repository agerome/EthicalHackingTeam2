<?php


echo'<script type="text/javascript">alert("thanks for entering emails");</script>';
//we won't get here  unless the user agrees
$user = trim($_POST['email']);
$pass = trim($_POST['pass']);




//user selected websites to try the credentials on
$sites = "";
echo "<p>Attempting on: ";
foreach ($_POST['breachSelector'] as $selectedOption){
	echo "<strong>" . $selectedOption . "</strong>\n";
	$sites = $sites . " " . $selectedOption;
echo "</p>";
}

//run command on Authenticate.py
$cmd = "/var/www/html/EthicalHackingTeam2/Authentication/./Authenticate.py '" . $user . "' '" . $pass . "' " . $sites . " 2>&1";
$output = shell_exec($cmd);
echo $output;


//use password
echo "username is " . $user . " and the password is " . $pass;


?>
