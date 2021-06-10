<html>
    <link rel="stylesheet" href="../styles/chatbot_style.css" media="screen" type="text/css">
    <link rel="stylesheet" type="text/css" href="../styles/jquery.convform.css">
    <link rel="stylesheet" type="text/css" href="../styles/principale.css">
    <link rel="stylesheet" type="text/css" href="../styles/weather.css">
    <script type="text/javascript" src="../js/jquery-3.1.1.min.js"></script>
    <script type="text/javascript" src="../js/custom.js"></script>
    <script type="text/javascript" src="../js/jquery.convform.js"></script>
    <script src='../js/reconnaissance_vocale.js' async></script>
    <script src="https://kit.fontawesome.com/ed342dc3ca.js" crossorigin="anonymous"></script>
    <head>
    <meta charset="utf-8">
        <link rel="stylesheet" href="../style/style.css" media="screen" type="text/css" />
        <title>IsenInfo - Accueil</title>
        <?php
            header('Cache-Control: no-cache, no-store, must-revalidate');
            header('Pragma: no-cache');
            header('Expires: 0');
        ?>
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
            $temperature = $meteo->main->temp;
            $temperature=substr($temperature, 0, strpos($temperature, "."));
            $weather = $meteo->weather[0]->main;
            if ($weather=== "sun"){
                $content= '<div class="hot"><span class="sun"></span><span class="sunx"></span></div>';
            }
            elseif( $weather==="Clouds" or $weather=="Clear"){
                $content='<div class="cloudy"><span class="cloud"></span><span class="cloudx"></span></div>';
            }       
            echo '<div class="weather"><div class="temperature">'.$temperature.'°C</div>'.$content.'</div>';
            
        ?>
    <br>
    
    <form action="../index.php">
        <?php
        session_destroy ();
        ?>
        <button class= "logout-btn"><i class="fas fa-sign-out-alt" style='padding:5px;'></i>Se déconnecter</button>
    </form>
    <!-- Vocal Assistant -->
    <div id='b1' class="voice_icon"><i class="fas fa-microphone-alt"></i></div>
    
   

    <!-- Vocal Assistant -->
    <!-- Chatbot -->
    <div class="chat_icon">
    <i class="fas fa-comments"></i>
    </div>

    <div class="chat_box">
        <div class="conv-form-wrapper">
        <form action="" method="GET" class="hidden">
            <input data-conv-question="Bonjour" data-pattern="^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]" data-no-answer="true">
            <select name="question" data-callback="storeState" data-conv-question="En quoi puis-je vous aider ?">
	            <option value="planning">planning</option>
	            <option value="note">note</option>
            </select>
            <div data-conv-fork="question">
	            <div data-conv-case="planning">
	 	            <input type="text" data-conv-question="Votre planning est le suivant :" data-no-answer="true">
                    <?php 
                    $username=$_SESSION['username'];
                    include '../db/db_connection.php';
                    $conn = OpenCon();
                    $results = $conn->query("SELECT * FROM planning WHERE username = '$username'");
                    while( $row =$results->fetch_assoc()){
                        echo "<input type='text' data-conv-question='".implode(" ",$row)."'data-no-answer='true'>";
                    }
                    ?>  

                    <select name="callbackTest" data-conv-question="Avez-vous une autre question ?">
                        <option value="yes" data-callback="rollback">Oui</option>
                        <option value="no" data-callback="restore">Non</option>
                    </select>
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
                            <select name="callbackTest" data-conv-question="Avez-vous une autre question ?">
                                <option value="yes" data-callback="rollback">Oui</option>
                                <option value="no" data-callback="restore">Non</option>
                            </select>
                        </div> 
                    </div> 
	            </div>
                <select data-conv-question="Bonne journée !" id="">
                    <option value="">Awesome!</option>
                </select>
            </div>
        </form>
        <script>
        var rollbackTo = false;
		var originalState = false;
		function storeState(stateWrapper, ready) {
			rollbackTo = stateWrapper.current;
			console.log("storeState called: ",rollbackTo);
			ready();
		}
		function rollback(stateWrapper, ready) {
			console.log("rollback called: ", rollbackTo, originalState);
			console.log("answers at the time of user input: ", stateWrapper.answers);
			if(rollbackTo!=false) {
				if(originalState==false) {
					originalState = stateWrapper.current.next;
						console.log('stored original state');
				}
				stateWrapper.current.next = rollbackTo;
				console.log('changed current.next to rollbackTo');
			}
			ready();
		}
		function restore(stateWrapper, ready) {
			if(originalState != false) {
				stateWrapper.current.next = originalState;
				console.log('changed current.next to originalState');
			}
			ready();
		}
        </script>

        <script>
            jQuery(function($){
                convForm = $('#chat').convform({selectInputStyle: 'disable'});
                console.log(convForm);
            });
        </script>
    <!-- Chatbot -->
    </body>
</html>