<?php
ini_set('display_errors', 'on');
$command = escapeshellcmd('/python/test.py');
session_start();
$_SESSION['output']=shell_exec($command);
header('Location: login.php?register_error=1');
?>
