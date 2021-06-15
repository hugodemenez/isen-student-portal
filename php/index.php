<html>
    <head>
        <meta charset="utf-8">
        <meta name = "viewport" content = "width=device-width, minimum-scale=1.0, maximum-scale = 1.0, user-scalable = no">
        <link rel="stylesheet" href="styles/style.css" media="screen" type="text/css"/>
        <script src="https://kit.fontawesome.com/ed342dc3ca.js" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/particlesjs/2.2.2/particles.min.js"></script>
    </head>
 
    <body>
        
    <!-- Fond animé -->
    <canvas class="background"></canvas>
    <script async>window.onload = function() {Particles.init({selector: '.background',maxParticles: 150,connectParticles: true,color: '#626262',speed:0.3,});};</script>
    
    <div class="form-box">
    <img src="data:image/jpeg;base64,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" alt="ISEN" >
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


