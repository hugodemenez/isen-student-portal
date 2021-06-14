<html>
    <link rel="stylesheet" href="../styles/chatbot_style.css" media="screen" type="text/css">
    <link rel="stylesheet" type="text/css" href="../styles/jquery.convform.css">
    <link rel="stylesheet" type="text/css" href="../styles/principale.css">
    <link rel="stylesheet" type="text/css" href="../styles/weather.css">
    <link rel="stylesheet" type="text/css" href="../styles/graph.css">
    <script type="text/javascript" src="../js/jquery-3.1.1.min.js"></script>
    <script type="text/javascript" src="../js/custom.js"></script>
    <script type="text/javascript" src="../js/jquery.convform.js"></script>
    <script src='../js/reconnaissance_vocale.js' async></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/particlesjs/2.2.2/particles.min.js"></script>
    <script src="https://kit.fontawesome.com/ed342dc3ca.js" crossorigin="anonymous"></script>
    
    <meta name = "viewport" content = "width=device-width, minimum-scale=1.0, maximum-scale = 1.0, user-scalable = no">
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
                $content = '<div class="hot"><span class="sun"></span><span class="sunx"></span></div>';
            }
            if( $weather==="Clouds" or $weather=="Clear"){
                $content = '<div class="cloudy"><span class="cloud"></span><span class="cloudx"></span></div>';
            }
            if( $weather==="Drizzle" or $weather=="Thunderstorm" or $weather=="Rain"){
                $content = '<div class="breezy"><ul><li></li><li></li><li></li><li></li><li></li></ul><span class="cloudr"></span></div>';
            }  
            elseif( $weather==="Snow"){
                $content = '<div class="stormy"><ul><li></li><li></li><li></li><li></li><li></li><li></li><li></li><li></li></ul><span class="snowe"></span><span class="snowex"></span><span class="stick"></span><span class="stick2"></span></div>';
            }    
            echo '<div class="weather"><div class="temperature">'.$temperature.'°C</div>'.$content.'</div>';
        ?>
        <!-- Fond animé -->
        <canvas class="background"></canvas>
        <script src="path/to/particles.min.js"></script>
        <script async>window.onload = function() {Particles.init({selector: '.background',maxParticles: 150,connectParticles: true,color: '#4F42DE',speed:0.3,});};</script>
        
        <!-- Boutton deconnexion -->
        <form action="../index.php">
            <?phpsession_destroy ();?>
            <button class= "logout-btn"><i class="fas fa-sign-out-alt" style='padding:5px;'></i>Se déconnecter</button>
        </form>
        <!-- Assistant vocal -->
        <div id='b1' class="voice_icon">
            <i class="fas fa-microphone-alt"></i>
        </div>


        <!-- Chatbot -->
        <div class="chatbot">
            <div class="chat_icon">
            <i class="fas fa-comments"></i>
            </div>
            <?php 
            $username=$_SESSION['username'];
            include '../db/db_connection.php';
            $conn = OpenCon();
            $planning ='';
            $notes ='';
            $results = $conn->query("SELECT * FROM planning WHERE username = '$username'");
            while( $row =$results->fetch_assoc()){
                $planning = $planning."<input type='text' data-conv-question='Le ".$row['date'].' de '.$row['start'].' à '.$row['end'].' en '.$row['room'].' avec '.$row['teacher'].' pour '.$row['subject']."'data-no-answer='true'>";
            }
            $results = $conn->query("SELECT * FROM marks WHERE username = '$username' ORDER BY STR_TO_DATE(date,'%d/%m/%Y') ASC");
            while( $row =$results->fetch_assoc()){
                $note = "<input type='text' data-conv-question='".$row['date'].' '.$row['title'].' : '.$row['mark']."'data-no-answer='true'>";
            }
            $results = $conn->query("SELECT * FROM marks WHERE username = '$username' ORDER BY STR_TO_DATE(date,'%d/%m/%Y') DESC LIMIT 5");
            while( $row =$results->fetch_assoc()){
                $notes = $notes."<input type='text' data-conv-question='".$row['date'].' '.$row['title'].' : '.$row['mark']."'data-no-answer='true'>";
            }
            CloseCon($conn);
            echo ('
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
                                <input type="text" data-conv-question="Votre planning est le suivant :" data-no-answer="true">'
                                .$planning.
                                '<select name="callbackTest" data-conv-question="Avez-vous une autre question ?">
                                    <option value="yes" data-callback="rollback">Oui</option>
                                </select>
                            </div>
                            <div data-conv-case="note">
                                <select name="question_note" data-conv-question="Que souhaitez-vous savoir ?">
                                    <option value="5notes">5 dernières notes</option>
                                    <option value="1note">La dernière note</option>
                                </select>
                                <div data-conv-fork="question_note">
                                    <div data-conv-case="1note">
                                        <input type="text" data-conv-question="Voici votre dernière note :" data-no-answer="true">'
                                        .$note.
                                    '</div>
                                    <div data-conv-case="5notes">
                                        <input type="text" data-conv-question="Voici vos 5 dernières notes :" data-no-answer="true">'
                                        .$notes.
                                    '</div>
                                </div>
                                <select name="callbackTest" data-conv-question="Avez-vous une autre question ?">
                                    <option value="yes" data-callback="rollback">Oui</option>
                                </select>
                            </div> 
                        </div>
                    </form>
                </div>
            </div>')
            ?>
            <script defer>
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
                jQuery(function($){
                        convForm = $('#chat').convform({selectInputStyle: 'disable'});
                        console.log(convForm);
                    });
            </script>
            <!-- Chatbot -->
        </div>  

        <!-- Graphiques -->
        <div class="graphics">
            <canvas id="graphiques_notes"></canvas>
            <h2>Evolution de votre moyenne depuis votre entrée à l'isen</h2>
            <script>
            var [time,values]=<?php
                $username=$_SESSION['username'];
                include '../db/db_connection.php';
                $conn = OpenCon();
                $marks=[];
                $dates=[];
                $graph_results = $conn->query("SELECT * FROM marks WHERE username = '$username' ORDER BY STR_TO_DATE(date,'%d/%m/%Y') ASC");
                CloseCon($conn);
                while($row=$graph_results->fetch_assoc()){
                    array_push($marks,$row['mark']);
                    array_push($dates,$row['date']);
                    }
                echo "[";
                echo json_encode($dates);
                echo ",";
                echo json_encode($marks);
                echo "]";
            ?>;
            
            var ctx = document.getElementById('graphiques_notes');
            var myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: time,
                    datasets: [
                    { 
                        data: values ,
                        label: 'Notes',
                        borderColor: '#3e95cd',
                        fill: false,
                    }
                    ]
                }
            });
            </script>
        </div>

    </body>
</html>