<html>
    <link rel="stylesheet" href="../styles/chatbot_style.css" media="screen" type="text/css">
    <link rel="stylesheet" type="text/css" href="../styles/jquery.convform.css">
    <link rel="stylesheet" type="text/css" href="../styles/principale.css">
    <link rel="stylesheet" type="text/css" href="../styles/weather.css">
    <script type="text/javascript" src="../js/jquery-3.1.1.min.js"></script>
    <script type="text/javascript" src="../js/custom.js"></script>
    <script type="text/javascript" src="../js/jquery.convform.js"></script>
    <script src="https://kit.fontawesome.com/ed342dc3ca.js" crossorigin="anonymous"></script>
    <head>
    <meta charset="utf-8">
        <link rel="stylesheet" href="../style/style.css" media="screen" type="text/css" />
    </head>
    <body class="neutral">
        <?php
            session_start();
            if (isset($_SESSION['username'])) {
            echo "<h1>".'Bienvenue, '.$_SESSION['username']."</h1>";
            } else {
            echo "<h1>Vous n'êtes pas connecté</h1>";
            }
            $apiKey = "ef7a9b79630b7257c06221b69e13fdb9";
            $cityId = "2998324";
            $googleApiUrl = "http://api.openweathermap.org/data/2.5/weather?id=" . $cityId . "&lang=fr&units=metric&APPID=" . $apiKey;
    
            $ch = curl_init();
    
            curl_setopt($ch, CURLOPT_HEADER, 0);
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
            curl_setopt($ch, CURLOPT_URL, $googleApiUrl);
            curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
            curl_setopt($ch, CURLOPT_VERBOSE, 0);
            curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
            $response = curl_exec($ch);
    
            curl_close($ch);
            $meteo = json_decode($response);
            echo "<div class='container'><div class='weatherIcon'><div class=".$meteo->weather[0]->main."><div class='inner'><div style='position: absolute; top:120%;left:50%;'>".$meteo->main->temp."°C</div></div></div></div></div>";
        ?>
    <br>
    <form action="../index.php">
    <?php
    session_destroy ();
    ?>
    <button class= "logout-btn">Se déconnecter</button>
    </form>
    <!-- Chatbot -->
    <div class="chat_icon">
    <i class="fas fa-comments"></i>
    </div>

    <div class="chat_box">
        <div class="conv-form-wrapper">
        <form action="" method="GET" class="hidden">
            <input data-conv-question="Bonjour" data-pattern="^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]" data-no-answer="true">
            <select name="programmer" data-conv-question="En quoi puis-je vous aider ?">
	            <option value="planning">planning</option>
	            <option value="note">note</option>
            </select>
            <div data-conv-fork="programmer">
	            <div data-conv-case="planning">
	 	            <input type="text" data-conv-question="Votre planning est le suivant :">
                     <?php 
                     echo "<input type="text" data-conv-question='Test'>"
                     ?>
                    
	            </div>
	            <div data-conv-case="note">
		            <select name="note" data-conv-question="Voulez-vous votre dernière note ?">
			            <option value="Oui">Oui</option>
			            <option value="Non">Non</option>
		            </select>
                    <div data-conv-fork="note">
                        <div data-conv-case="Oui">
                            <input type="text" data-conv-question="Votre note est :">
                        </div> 
                        <div data-conv-case="Non">
                            <input type="text" data-conv-question="Tant pis">
                        </div> 
	            </div>
            </div>
        </form>
    <!-- Chatbot -->
    </body>
</html>