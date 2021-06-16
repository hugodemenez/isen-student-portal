<html>
    <head>
        <meta charset="utf-8">
        <meta name = "viewport" content = "width=device-width, minimum-scale=1.0, maximum-scale = 1.0, user-scalable = no">
        <link rel="stylesheet" href="styles/style.css" media="screen" type="text/css"/>
        <script src="https://kit.fontawesome.com/ed342dc3ca.js" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/particlesjs/2.2.2/particles.min.js"></script>
        <meta charset="utf-8">
        <title>IsenInfo</title>
        <?php
            header('Cache-Control: no-cache, no-store, must-revalidate');
            header('Pragma: no-cache');
            header('Expires: 0');
        ?>
        
    </head>
 
    <body>
        <div class="form-box">
            <img src="../assets/logo.png" alt="">
            <div class="button-box">
                <button id="login_btn" type="button" class="toggle-btn" onclick="connexion()">Connexion</button>
                <button id="register_btn" type="button" class="toggle-btn" onclick="inscription()">Inscription</button>
            </div>
            <form id="connexion" class="input-group" action="view/login_verification.php" method="POST">
        
                <i class="fas fa-user field_group">
                <input type="text" class="input-field" placeholder="Identifiant" name="username" required>
                </i>
                <i class="fas fa-lock field_group">
                <input id="password" type="password" class="input-field" placeholder="Mot de passe" name="password" required>
                <i id="eye" class="fas fa-eye" onclick="reveal_password()"></i>
                </i>
                <button type="submit" class="submit-btn">Se connecter</button>
                <?php
                if(isset($_GET['erreur'])){
                    $err = $_GET['erreur'];
                    if($err==1 || $err==2)
                        echo "<h1 style='color:red;position:absolute;top:-20px;left:0px;right:0px;margin:auto;'>⚠️Utilisateur ou mot de passe incorrect</h1>";
                }
                ?>
            </form>
            
            <form id="inscription" class="input-group" action="view/register_verification.php" method="POST">
                <i class="fas fa-envelope field_group">
                    <input type="email" class="input-field" placeholder="email" name="email_register" required>
                </i>
                <i class="fas fa-user field_group">
                    <input type="text" class="input-field" placeholder="Identifiant Aurion" name="username_register" required>
                </i>
                <i class="fas fa-lock field_group">
                    <input id="password_register" type="password" class="input-field" placeholder="Mot de passe Aurion" name="password_register" required>
                    <i id="eye_register" class="fas fa-eye" onclick="reveal_password_register()"></i>
                </i>
                <button type="submit" class="submit-btn">S'inscrire</button>
                <?php
                if(isset($_GET['register_error'])){
                    $err = $_GET['register_error'];
                    if($err==1){
                        echo "<p style='color:red'>Utilisateur déjà inscrit</p>";
                        echo '<script>
                        var x = document.getElementById("connexion");
                        var y = document.getElementById("inscription");
                        var login_btn = document.getElementById("login_btn");
                        var register_btn = document.getElementById("register_btn");
                        function inscription(){
                            x.style.left = "-100%";
                            y.style.left = "25%";
                            login_btn.style.textDecoration  = "none";
                            register_btn.style.textDecoration  = "underline";
                        }
                        inscription();
                        </script>';
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
        var login_btn = document.getElementById("login_btn");
        var register_btn = document.getElementById("register_btn");
        function inscription(){
            x.style.left = "-100%";
            y.style.left = "25%";
            login_btn.style.textDecoration  = "none";
            register_btn.style.textDecoration  = "underline";
        }
        function connexion(){
            x.style.left = "25%";
            y.style.left = "-100%";
            login_btn.style.textDecoration  = "underline";
            register_btn.style.textDecoration  = "none";
        }

        function reveal_password() {
            var x = document.getElementById("password");
            var y = document.getElementById("eye");
            if (x.type === "password") {
                x.type = "text";
                y.className = "fas fa-eye-slash";
            } else {
                x.type = "password";
                y.className = "fas fa-eye";
                
            }
        }
        function reveal_password_register() {
            var x = document.getElementById("password_register");
            var y = document.getElementById("eye_register");
            if (x.type === "password") {
                x.type = "text";
                y.className = "fas fa-eye-slash";
            } else {
                x.type = "password";
                y.className = "fas fa-eye";
                
            }
        }
    </script>
</html>


