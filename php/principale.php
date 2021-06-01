<html>
    <head>
    <meta charset="utf-8">
        <link rel="stylesheet" href="style.css" media="screen" type="text/css" />
    </head>
    <body class="neutral">
        <?php
            session_start();
            if (isset($_SESSION['username'])) {
            echo 'Bienvenue, '.$_SESSION['username']; 
            } else {
            echo "Vous n'êtes pas connecté";
            }
        ?>
    </body>
    <footer>
    <a href="login.php">Se déconnecter</a>
    </footer>
</html>