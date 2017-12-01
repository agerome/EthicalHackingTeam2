<?php
//we won't get here  unless the user agrees
$user = trim($_POST['username']);
$pass = trim($_POST['password']);





/* if we're using checkboxes...
	we should make it where only if the user agrees we work their credentials on the site
	if they disagree, how about we just try their password only on the breach statistics website?*/


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
