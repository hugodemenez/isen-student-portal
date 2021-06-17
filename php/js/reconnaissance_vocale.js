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



function readCookie(name) {
	var nameEQ = name + "=";
	var ca = document.cookie.split(';');
	for(var i=0;i < ca.length;i++) {
		var c = ca[i];
		while (c.charAt(0)==' ') c = c.substring(1,c.length);
		if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
	}	
	return null;	
}


function caractere_cpeciaux(texte){ //on remplace les caractère spéciaux qui ne s'enregistre pas comme tels quand in créer les cookies

	texte = texte.replace(/%2C/g, ",");
	texte = texte.replace(/%20/g, " ");
	texte = texte.replace(/%3A/g, ":");
	texte = texte.replace(/%28/g, "(");
	texte = texte.replace(/%29/g, ")");
	texte = texte.replace(/\+/g, " ");
	texte = texte.replace (/%2F/g, "/");
	texte = texte.replace (/%C3%A9/g, "é");
	texte = texte.replace (/%C3%A8/g, "è");
	texte = texte.replace (/%C3%AA/g, "ê");
	texte = texte.replace (/%C3%A2/g, "â");
	texte = texte.replace (/%C3%A0/g, "à");
	texte = texte.replace (/%C3%AE/g, "î");
	texte = texte.replace (/%C3%AF/g, "ï");
	texte = texte.replace (/%26/g, "&");

	return texte;
}




function comprendre(texte){ //regex pour comprendre la commande par exemple si la personne dit planning alors on affiche le planning
	let texte_comprendre;
	if ((texte.search(/planning/) != -1 ) || (texte.search(/emploi du temps/)) != -1) {
		//createCookie("Cookie_planning","le cookie fonctionne")
		alert(caractere_cpeciaux(readCookie('Cookie_planning')));
		//message_synthetise = "voici votre planning :" + caractere_cpeciaux(readCookie('Cookie_planning'));
		return "planning";
	}
	else if (texte.search(/note/) != -1) {
		alert(caractere_cpeciaux(readCookie('Cookie_note')));
		message_synthetise = "voici votre dernière note :" + caractere_cpeciaux(readCookie("Cookie_note"));
		return "note";
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
	msg.text = message_synthetise;
	speechSynthesis.speak(msg);
}



