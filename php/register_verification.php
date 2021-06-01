<?php 
ini_set('display_errors', 'on');
session_start();
$item=$_POST['username_register'];
$item2=$_POST['password_register'];
$item3=$_POST['email_register'];
$item4=$_POST['niveau_register'];
$item5=$_POST['specialite_register'];
$tmp = exec("python test.py $item $item2 $item3 $item4 $item5");
echo $tmp;
?>
