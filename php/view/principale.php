<!-- Code php pour verifier que l'utilisateur existe dans la base de donnée et pour créer les cookies pour transmettre des infos au JavaScript -->
<?php
    session_start();
    include '../db/db_connection.php';     
    $username=$_SESSION['username'];
    $conn = OpenCon();
    $results = $conn->query("SELECT * FROM user WHERE username='$username'");
    if (mysqli_num_rows($results)==0){
        header('Location: ../index.php?register_error=3');
    }
    CloseCon($conn);


    $conn = OpenCon();
    $Cookie_planning ='';
    $results = $conn->query("SELECT * FROM planning WHERE username = '$username'");
    while( $row =$results->fetch_assoc()){
        $Cookie_planning = $Cookie_planning.' '.$row['date'].' de '.$row['start'].' à '.$row['end'].' en '.$row['room'].' avec '.$row['teacher'].' pour '.$row['subject'];
    }
    setcookie('Cookie_planning', $Cookie_planning);
    $Cookie_note ='';
    $results = $conn->query("SELECT * FROM marks WHERE username = '$username' ORDER BY STR_TO_DATE(date,'%d/%m/%Y') ASC");
    while( $row =$results->fetch_assoc()){
        $Cookie_note =$row['title'].' : '.$row['mark'];
    }
    CloseCon($conn);
    setcookie('Cookie_note', $Cookie_note);
?>

<html>
    <link rel="stylesheet" href="../styles/chatbot_style.css" media="screen" type="text/css">
    <link rel="stylesheet" type="text/css" href="../styles/jquery.convform.css">
    <link rel="stylesheet" type="text/css" href="../styles/principale.css">
    <link rel="stylesheet" type="text/css" href="../styles/weather.css">
    <link rel="stylesheet" type="text/css" href="../styles/graph.css">
    <script type="text/javascript" src="../js/jquery-3.1.1.min.js"></script>
    <script type="text/javascript" src="../js/custom.js"></script>
    <script type="text/javascript" src="../js/jquery.convform.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/particlesjs/2.2.2/particles.min.js"></script>
    <script src="https://kit.fontawesome.com/ed342dc3ca.js" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="../js/reconnaissance_vocale.js" async></script>
    
    <meta name = "viewport" content = "width=device-width, minimum-scale=1.0, maximum-scale = 1.0, user-scalable = no">

    <head>
    <meta charset="utf-8">
        <title>IsenInfo - Accueil</title>
        <?php
            header('Cache-Control: no-cache, no-store, must-revalidate');
            header('Pragma: no-cache');
            header('Expires: 0');
        ?>
    </head>
    <body>
        <!-- Connexion à l'API openweathermap pour récuperer les informations sur la température et faire un affichage dynamique en fonction des conditions météorologiques -->
        <?php
            if (isset($_SESSION['username'])) {
            echo "<h1>Bienvenue</h1>";
            
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
            if( $weather==="Drizzle" or $weather=="Thunderstorm" or $weather=="Rain" or $weather=="Mist" or $weather=="Haze"){
                $content = '<div class="breezy"><ul><li></li><li></li><li></li><li></li><li></li></ul><span class="cloudr"></span></div>';
            }  
            elseif( $weather==="Snow"){
                $content = '<div class="stormy"><ul><li></li><li></li><li></li><li></li><li></li><li></li><li></li><li></li></ul><span class="snowe"></span><span class="snowex"></span><span class="stick"></span><span class="stick2"></span></div>';
            }    
            echo '<div class="weather">'.$content.'<div class="temperature">'.$temperature.'°C</div></div>';
        ?>

        <!-- Graphique ordinateur et tablette -->
        <div class="graphics other">
            <canvas id="graphiques_notes" width="100%" height="65%"></canvas>
            <script>
            var [time,values]=<?php
                $username=$_SESSION['username'];
                $conn2 = OpenCon();
                $marks=[];
                $dates=[];
                $graph_results = $conn2->query("SELECT * FROM marks WHERE username = '$username' ORDER BY STR_TO_DATE(date,'%d/%m/%Y') ASC");
                CloseCon($conn2);
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
                        borderColor: '#004980',
                        
                    }
                    ]
                }
            });
            </script>
            <h2>Evolution de vos notes depuis votre entrée à l'isen</h2>
        </div>

        <!-- Graphique telephone -->
        <div class="graphics iphone">
            <canvas id="graphiques_notes_iphone" width="100%" height="100%"></canvas>
            <script>
            var [time,values]=<?php
                $username=$_SESSION['username'];
                $conn2 = OpenCon();
                $marks=[];
                $dates=[];
                $graph_results = $conn2->query("SELECT * FROM marks WHERE username = '$username' ORDER BY STR_TO_DATE(date,'%d/%m/%Y') DESC LIMIT 5");
                CloseCon($conn2);
                while($row=$graph_results->fetch_assoc()){
                    array_push($marks,$row['mark']);
                    array_push($dates,$row['date']);
                    }
                echo "[";
                echo json_encode(array_reverse($dates));
                echo ",";
                echo json_encode(array_reverse($marks));
                echo "]";
            ?>;
            
            var ctx = document.getElementById('graphiques_notes_iphone');
            var myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: time,
                    datasets: [
                    { 
                        data: values ,
                        label: 'Notes',
                        borderColor: '#004980',
                        
                    }
                    ]
                }
            });
            </script>
            <h2>Evolution de vos 5 dernières notes</h2>
        </div>

        <!-- Chatbot -->
        <div class="chatbot">
            <div class="chat_icon">
            <i class="fas fa-comments"></i>
            </div>
            <?php 
            $username=$_SESSION['username'];
            $conn = OpenCon();
            $planning ='';
            $notes ='';
            $note = '';
            $results = $conn->query("SELECT * FROM planning WHERE username = '$username'");
            while( $row =$results->fetch_assoc()){
                $planning = $planning."<input type='text' data-conv-question='".$row['date'].' de '.$row['start'].' à '.$row['end'].' en '.$row['room'].' avec '.$row['teacher'].' pour '.$row['subject']."'data-no-answer='true'>";
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
                        <select name="bonjour" data-callback="storeState"  data-conv-question="Bonjour">
                            <option>Bonjour</option>
                        </select>
                        <div data-conv-fork="bonjour">
                            <select name="question" data-conv-question="En quoi puis-je vous aider ?">
                                <option value="planning">planning</option>
                                <option value="note">note</option>
                            </select>
                            <div data-conv-fork="question">
                                <div data-conv-case="planning">
                                    <select name="question_planning" data-conv-question="Que souhaitez-vous savoir ?">
                                        <option value="planning">mon planning</option>
                                    </select>
                                    <div data-conv-fork="question_planning">
                                        <div data-conv-case="planning">
                                            <input type="text" data-conv-question="Voici votre planning de la semaine :" data-no-answer="true">'
                                            .$planning.
                                            '<select name="callbackTest" data-conv-question="Avez-vous une autre question ?">
                                                <option value="yes" data-callback="rollback">Oui</option>
                                            </select>
                                        </div>
                                    </div>
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
                                            '<select name="callbackTest" data-conv-question="Avez-vous une autre question ?">
                                                <option value="yes" data-callback="rollback">Oui</option>
                                            </select>
                                        </div>
                                        <div data-conv-case="5notes">
                                            <input type="text" data-conv-question="Voici vos 5 dernières notes :" data-no-answer="true">'
                                            .$notes.
                                            '<select name="callbackTest" data-conv-question="Avez-vous une autre question ?">
                                                <option value="yes" data-callback="rollback">Oui</option>
                                            </select>
                                        </div>
                                    </div>
                                </div> 
                            </div>
                        </div>
                    </form>
                </div>
            </div>');
            ?>
            <script>
                var rollbackTo = false;
                var originalState = false;
                var rollbackAnswers  = false;
                function storeState(stateWrapper, ready) {
                    rollbackTo = stateWrapper.current;
                    rollbackAnswers = { ...stateWrapper.answers };
                    console.log("storeState called: ",rollbackTo);
                    ready();
                }
                function rollback(stateWrapper, ready) {
                    console.log("rollback called: ", rollbackTo, originalState);
                    if(rollbackTo!=false) {
                        if(originalState==false) {
                            console.log('stored original state');
                        }
                        stateWrapper.current = rollbackTo;
                        stateWrapper.answers = { ...rollbackAnswers};
                        console.log('changed current to rollbackTo');
                    }
                    ready();
                }
                
                
            </script>
            <!-- Chatbot -->
        </div>  

        <!-- Boutton deconnexion -->
        <form action="../index.php">
            <?php session_destroy ();?>
            <button class= "logout-btn"><i class="fas fa-sign-out-alt" style='padding:5px;'></i>Se déconnecter</button>
        </form>
        
        <!-- Assistant vocal -->
        <div id='b1' class="voice_icon">
            <i class="fas fa-microphone-alt"></i>
        </div>

    </body>

</html>