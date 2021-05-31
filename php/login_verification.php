<?php
ini_set('display_errors', 'on');
if(isset($_POST['username']) && isset($_POST['password'])){
   $username = $_POST['username'];
   $password = $_POST['password'];
   $db = new SQLite3('db/database.db');
   $results = $db->query("SELECT * FROM user WHERE username = '$username'");
   $row = $results->fetcharray();
   if($row[1]==$password){
      session_start();
      $_SESSION['username'] = $username;
      $_SESSION['password'] = $password;
      header('Location: principale.php');
   }
   else
   {
      header('Location: login.php?erreur=1');
   }
}
?>
