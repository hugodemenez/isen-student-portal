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
            <input type="text" class="input-field" placeholder="username" required>
            <input type="text" class="input-field" placeholder="password" required>
            <input type="checkbox" class="check-box"><span>Remember Password</span>
            <button type="submit" class="submit-btn">Connexion</button>
            <?php
            if(isset($_GET['erreur'])){
                $err = $_GET['erreur'];
                if($err==1 || $err==2)
                    echo "<p style='color:red'>Utilisateur ou mot de passe incorrect</p>";
            }
            ?>
        </form>
        <form id="inscription" class="input-group" action="view/register_verification.php" method="POST">
            <input type="text" class="input-field" placeholder="email" name="email_register" required>
            <input type="text" class="input-field" placeholder="username" name="username_register" required>
            <input type="text" class="input-field" placeholder="password" name="password_register" required>
            <input type="text" class="input-field" placeholder="niveau" name="niveau_register" required>
            <input type="text" class="input-field" placeholder="specialite" name="specialite_register" required>
            <button type="submit" class="submit-btn">Inscription</button>
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
    </div>
    </body>
    <script>
        var x = document.getElementById("connexion");
        var y = document.getElementById("inscription");
        var z = document.getElementById("btn");

        function inscription(){
            x.style.left = "-400px";
            y.style.left = "50px";
            z.style.left = "110px";
        }
        function connexion(){
            x.style.left = "50px";
            y.style.left = "450px";
            z.style.left = "0";
        }
    </script>
</html>


