<?php
ini_set('display_errors', 'on');
session_start();
if(isset($_POST['username']) && isset($_POST['password']))
   {
   // Connexion
   try {
      $dbname='database.db'; 
      if(!class_exists('SQLite3'))  die("SQLite 3 NOT supported."); 
      $base =  new SQLite3($dbname, 0666);
      echo "SQLite 3 supported."; 
   } 
   catch (SQLiteException $e) {
      die("La création ou l'ouverture de la base [$base] a échouée ".
         "pour la raison suivante: ".$e->getMessage());
}
    // on applique les deux fonctions mysqli_real_escape_string et htmlspecialchars
    // pour éliminer toute attaque de type injection SQL et XSS
    $username = $_POST['username']; 
    $password = $_POST['password'];
    if($username !== "" && $password !== "")
    {
      $query = "SELECT COUNT(*) as count FROM `user` WHERE `username` = :username AND `password` = :password"; 
      $results = $base->query($query);
      $row = $results->fetchArray(); 
       if(count($row)>0)
        { 
            header('location:principale.php'); }	
		else{
			$_SESSION['error'] = "Invalid username or password";
			header('location:login.php?erreur=1');
		}
   }
        
    
    else
    {
       header('Location: login.php?erreur=2'); // utilisateur ou mot de passe vide
    }
}
else
{
   header('Location: login.php');
}
$bd = null; // fermer la connexion
?>
