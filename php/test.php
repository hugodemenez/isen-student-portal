<?php 
ini_set('display_errors', 'on');
$output = shell_exec(('python test.py'));
echo $output;
?>
