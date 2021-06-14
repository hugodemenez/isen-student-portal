let enregistrement_audio = document.getElementById('b1');
let variable_a_modifier;
let message_synthetise = '';
enregistrement_audio.addEventListener('click', alerte);
let final_transcript = ''; // paramètre de base pour la reconnaissance vocale
let recognition = new webkitSpeechRecognition();
recognition.continuous = false;
recognition.interimResults = true;
recognition.onresult = function(event) 
{ 
	//alert(event.results[0][0].transcript);
	final_transcript = event.results[0][0].transcript;
}
recognition.onspeechend = function(){
	buffer = comprendre(final_transcript);
	if (buffer == "planning"){
		synthetiser()}
	if (buffer == "note"){
		synthetiser()}
	if (buffer == "-1") {alert("L'instruction n'est pas claire");}
}


function comprendre(texte){ //regex pour comprendre la commande par exemple si la personne dit planning alors on affiche le planning
	let texte_comprendre;
	if (texte.search(/planning/) != -1 ) {
		message_synthetise = "voici votre planning";
		return "planning";
	}
	else if (texte.search(/note/) != -1) {
		message_synthetise = "voici votre dernière note";
		return "note"
	}
	else {texte_comprendre = "-1";}
	return texte_comprendre;
}

function alerte(){
	if (!('webkitSpeechRecognition' in window)) {
	alert("La reconnaissance vocale n'est pas disponible sur votre navigateur")}
	else {
		recognition.lang = "fr-FR";
		recognition.start();
	}
}


function synthetiser(variable_a_modifier){
	let msg = new SpeechSynthesisUtterance();
	let voices = window.speechSynthesis.getVoices();
	msg.voice = voices[6]; //6 pour la voix française
	msg.voiceURI = 'native';
	msg.volume = 1; // 0 to 1
	msg.rate = 1; // 0.1 to 2
	msg.pitch =1; //0 to 2
	msg.text = message_synthetise + " bonjour";
	speechSynthesis.speak(msg);
}



