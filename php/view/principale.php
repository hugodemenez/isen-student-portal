<html>
    <link rel="stylesheet" href="../styles/chatbot_style.css" media="screen" type="text/css">
    <link rel="stylesheet" type="text/css" href="../styles/jquery.convform.css">
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
            echo 'Bienvenue, '.$_SESSION['username']; 
            } else {
            echo "Vous n'êtes pas connecté";
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
            echo "<br />".$meteo->weather[0]->description . "<br />";
            echo $meteo->main->temp;

        ?>
    <!-- Chatbot -->
    <div class="chat_icon">
    <i class="fas fa-comments"></i>
    </div>

    <div class="chat_box">
        <div class="conv-form-wrapper">
        <form action="" method="GET" class="hidden">
            <input data-conv-question="Bonjour" data-pattern="^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]">
            <input data-conv-question="Type in your e-mail" data-pattern="^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$" id="email" type="email" name="email" required placeholder="What's your e-mail?">
            <select name="programmer" data-conv-question="En quoi puis-je vous aider ?">
	            <option value="planning">planning</option>
	            <option value="note">note</option>
            </select>
            <div data-conv-fork="programmer">
	            <div data-conv-case="planning">
	 	            <input type="text" data-conv-question="Votre planning est le suivant :">
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
    <footer>
    <a href="../index.php">Se déconnecter</a>
    </footer>
</html>