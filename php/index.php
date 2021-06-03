<html>
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="styles/style.css" media="screen" type="text/css" />
    </head>
    <body>
        <form action="view/login_verification.php" method="POST">
            <h1>Connexion</h1>

            <input type="text" placeholder="username" name="username" required>

            <input type="password" placeholder="password" name="password" required>

            <input type="submit" id='submit' value='✓' >
            <?php
            if(isset($_GET['erreur'])){
                $err = $_GET['erreur'];
                if($err==1 || $err==2)
                    echo "<p style='color:red'>Utilisateur ou mot de passe incorrect</p>";
            }
            ?>

        </form>

        <form action="view/register_verification.php" method="POST">
            <h1>Inscription</h1>

            <input type="text" placeholder="username" name="username_register" required>

            <input type="password" placeholder="password" name="password_register" required>
            
            <input type="text" placeholder="email" name="email_register" required>

            <input type="text" placeholder="niveau" name="niveau_register" required>

            <input type="text" placeholder="specialite" name="specialite_register" required>

 

            <input type="submit" id='submit_register' value='✓'>
            <?php
            if(isset($_GET['register_error'])){
                $err = $_GET['register_error'];
                if($err==1){
                    echo "<p style='color:red'>Utilisateur déjà inscrit</p>";
                }
                elseif($err==2){
                    echo "<p style='color:green'>Inscription réussite</p>";
                }
            }
            ?>
        </form>
    </body>
</html>


