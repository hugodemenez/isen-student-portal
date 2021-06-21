<?php
    header('Cache-Control: no-cache, no-store, must-revalidate');
    header('Pragma: no-cache');
    header('Expires: 0');
?>

<html>
    <head>
        <meta charset="utf-8">
        <meta name = "viewport" content = "width=device-width, minimum-scale=1.0, maximum-scale = 1.0, user-scalable = no">
        <link rel="stylesheet" href="../styles/waiting_screen.css" media="screen" type="text/css"/>
        <meta charset="utf-8">
        <title>IsenInfo - waiting screen</title>
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
    <body>
    <div class="waiting">
    <img src="../assets/spinner.svg">
    <br>
    <a href="principale.php">Veuillez attendre 2 minutes le temps que vos données soient chargées, sinon cliquez ici</a>
    </div>
    </body>
    <script>
        setTimeout(function(){location.href = "principale.php";},120000); // 120 seconds
    </script>
</html>


