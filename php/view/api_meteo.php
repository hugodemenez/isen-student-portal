<?php 
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
/* echo $meteo->weather[0]->description . "<br />"; //exemple pour avoir des trucs
echo $meteo->weather[0]->id	; pour plus d'infos:https://openweathermap.org/current#format

IL FAUT INSTALLER LA BLIBLIOTHEQUE CURL

 */ 

?>
