<?php


echo'<script type="text/javascript">alert("thanks for entering emails");</script>';
//we won't get here  unless the user agrees
$list = trim($_POST['list']);
echo $list;
//run command on Authenticate.py
$cmd = "'/var/www/html/EthicalHackingTeam2/Email/./emailerjaetestdonttouchplease.py '. $list. '/var/www/html/EthicalHackingTeam2/Email/./phishing-email.html'. ' 2>&1'";
$output = shell_exec($cmd);
echo $output;

?>
