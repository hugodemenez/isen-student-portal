<!-- Script php avec les fonctions de connexion et de déconnexion à la base de données -->

<?php
function OpenCon()
 {
 $dbhost = "localhost";
 $dbuser = "hugodemenez";
 $dbpass = "password";
 $db = "database";
 $conn = new mysqli($dbhost, $dbuser, $dbpass,$db) or die("Connect failed: %s\n". $conn -> error);
 
 return $conn;
 }
 
function CloseCon($conn)
 {
 $conn -> close();
 }
   
?>