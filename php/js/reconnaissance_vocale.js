let enregistrement_audio = document.getElementById('b1');


enregistrement_audio.addEventListener('click', alerte);
//prononcer.addEventListener('click' , function(){synthetiser("pourquoi")});

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
	if (buffer != "-1"){
	document.location.href=buffer;}
	if (buffer == "-1") { alert("L'instruction n'est pas claire");}
}


function comprendre(texte){ //regex pour comprendre la commande par exemple si la personne dit planning alors on affiche le planning
	let texte_comprendre;
	if (texte.search(/planning/) != -1 ) {texte_comprendre = "http://iseninfo.fr/";}
	else if (texte.search(/note/) != -1) {texte_comprendre = "http://iseninfo.fr/";}
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