<html>
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="styles/style.css" media="screen" type="text/css" />
    </head>
    <body>
    <div class="form-box">
        <div class="button-box">
            <div id="btn"></div>
            <button type="button" class="toggle-btn" onclick="connexion()">Connexion</button>
            <button type="button" class="toggle-btn" onclick="inscription()">Inscription</button>
        </div>
        <form id="connexion" class="input-group" action="view/login_verification.php" method="POST">
            <input type="text" class="input-field" placeholder="username" name="username" required>
            <input type="password" class="input-field" placeholder="password" name="password" required>
            <button type="submit" class="submit-btn">✓</button>
            <?php
            if(isset($_GET['erreur'])){
                $err = $_GET['erreur'];
                if($err==1 || $err==2)
                    echo "<p style='color:red'>Utilisateur ou mot de passe incorrect</p>";
            }
            ?>
        </form>
        <form id="inscription" class="input-group" action="view/register_verification.php" method="POST">
            <input type="email" class="input-field" placeholder="email" name="email_register" required>
            <input type="text" class="input-field" placeholder="username" name="username_register" required>
            <input type="password" class="input-field" placeholder="password" name="password_register" required>
            <input type="text" class="input-field" placeholder="niveau" name="niveau_register" required>
            <input type="text" class="input-field" placeholder="specialite" name="specialite_register" required>
            <button type="submit" class="submit-btn">✓</button>
            <?php
            if(isset($_GET['register_error'])){
                $err = $_GET['register_error'];
                if($err==1){
                    echo "<p style='color:red'>Utilisateur déjà inscrit</p>";
                }
                elseif($err==2){
                    echo "<p style='color:green'>Inscription réussie</p>";
                }
            }
            ?>
        </form>
    </div>
    </body>
    <script>
        var x = document.getElementById("connexion");
        var y = document.getElementById("inscription");
        var z = document.getElementById("btn");

        function inscription(){
            x.style.left = "-100%";
            y.style.left = "25%";
            z.style.left = "50%";
        }
        function connexion(){
            x.style.left = "25%";
            y.style.left = "-100%";
            z.style.left = "25%";
        }
    </script>
</html>


