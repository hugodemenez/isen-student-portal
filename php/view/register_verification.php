<?php 
ini_set('display_errors', 'on');
session_start();
$username_register=$_POST['username_register'];
$password_register=$_POST['password_register'];
$email_register=$_POST['email_register'];
$niveau_register=$_POST['niveau_register'];
$specialite_register=$_POST['specialite_register'];

$db = new SQLite3('../db/database.db');
$results = $db->query("INSERT OR REPLACE INTO user VALUES ('$username_register','$password_register','$email_register')");
header('Location: ../index.php?register_error=2');
?>
