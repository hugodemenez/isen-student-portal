<?php
ini_set('display_errors', 'on');
session_start();
if(isset($_POST['username']) && isset($_POST['password'])){
   $username = $_POST['username'];
   $password = $_POST['password'];
   $db = new SQLite3('db/database.db');
   $results = $db->query("SELECT * FROM user WHERE username = '$username'");
   $row = $results->fetcharray();
   if($row[1]==$password){
      header('Location: principale.php');
   }
   else
   {
      header('Location: login.php?erreur=1'); // utilisateur ou mot de passe incorrect
   }
}
?>
