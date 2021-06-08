<html>
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="styles/style.css" media="screen" type="text/css" />
        <script src="https://kit.fontawesome.com/ed342dc3ca.js" crossorigin="anonymous"></script>
    </head>
    <body>
        
    <div class="form-box">
        <div class="button-box">
            <button type="button" class="toggle-btn" onclick="connexion()">Connexion</button>
            <button type="button" class="toggle-btn" onclick="inscription()">Inscription</button>
            
        </div>
        <form id="connexion" class="input-group" action="view/login_verification.php" method="POST">
    
            <i class="fas fa-user input-field">
            <input type="text" class="input-field" placeholder="username" name="username" required>
            </i>
            <i class="fas fa-lock input-field">
            <input id="password" type="password" class="input-field" placeholder="password" name="password" required>
            <i id="eye" class="fas fa-eye" onclick="reveal_password()"></i>
            </i>
            <button type="submit" class="submit-btn">Se connecter</button>
            <?php
            if(isset($_GET['erreur'])){
                $err = $_GET['erreur'];
                if($err==1 || $err==2)
                    echo "<p style='color:red'>Utilisateur ou mot de passe incorrect</p>";
            }
            ?>
        </form>
        <form id="inscription" class="input-group" action="view/register_verification.php" method="POST">
            <i class="fas fa-envelope input-field">
                <input type="email" class="input-field" placeholder="email" name="email_register" required>
            </i>
            <i class="fas fa-user input-field">
                <input type="text" class="input-field" placeholder="username" name="username_register" required>
            </i>
            <i class="fas fa-lock input-field">
                <input id="password" type="password" class="input-field" placeholder="password" name="password_register" required>
                <i id="eye" class="fas fa-eye" onclick="reveal_password()"></i>
            </i>
            <button type="submit" class="submit-btn">S'inscrire</button>
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
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320" style = "position:absolute; right:0px; bottom:0px;z-index:-1;"><path fill="#00BFA6" fill-opacity="1" d="M0,128L30,117.3C60,107,120,85,180,85.3C240,85,300,107,360,133.3C420,160,480,192,540,186.7C600,181,660,139,720,144C780,149,840,203,900,234.7C960,267,1020,277,1080,261.3C1140,245,1200,203,1260,192C1320,181,1380,203,1410,213.3L1440,224L1440,320L1410,320C1380,320,1320,320,1260,320C1200,320,1140,320,1080,320C1020,320,960,320,900,320C840,320,780,320,720,320C660,320,600,320,540,320C480,320,420,320,360,320C300,320,240,320,180,320C120,320,60,320,30,320L0,320Z"></path></svg>
 
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
    </script>
</html>


