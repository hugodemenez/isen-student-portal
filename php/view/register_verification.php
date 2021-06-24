<! -- Code PHP pour exiger le rafraichissement du CSS -->
<?php
    header('Cache-Control: no-cache, no-store, must-revalidate');
    header('Pragma: no-cache');
    header('Expires: 0');
?>
<! -- Definition de la page de verification de l'inscription -->
<html>
    <head>
        <meta charset="utf-8">
        <meta name = "viewport" content = "width=device-width, minimum-scale=1.0, maximum-scale = 1.0, user-scalable = no">
        <link rel="stylesheet" href="../styles/waiting_screen.css" media="screen" type="text/css"/>
        <meta charset="utf-8">
        <title>IsenInfo - waiting screen</title>
        <! -- On verifie si l'utilisateur n'existe pas encore (dans le cas contraire un message d'erreur est affiché) et on demarre une session -->
        <?php 
            session_start();
            $username_register=$_POST['username_register'];
            $password_register=$_POST['password_register'];
            $email_register=$_POST['email_register'];
            include '../db/db_connection.php';
            $conn = OpenCon();
            $results = $conn->query("SELECT * FROM user WHERE username='$username_register'");
            if (mysqli_num_rows($results)==1){
                header('Location: ../index.php?register_error=1');
            }
            else{
                $results = $conn->query("INSERT INTO user VALUES ('$username_register','$password_register','$email_register')");
                $_SESSION['username']=$username_register;
            }
            CloseCon($conn);
        ?>
    </head>
    <! -- On affiche un ecran de chargement le temps que le webscraping se fasse (30-60s max) pour que le nouvel utilisateur puisse acceder à ses données Aurion -->
    <body>
    <div class="waiting">
    <img src="../assets/spinner.svg">
    <br>
    <a>Veuillez attendre 30 secondes le temps que vos données soient chargées, vous allez automatiquement être redirigé vers la page d'accueil</a>
    </div>
    </body>
    <script>
        setTimeout(function(){location.href = "principale.php";},40000); // 40 secondes
    </script>
</html>


