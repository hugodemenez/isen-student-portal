let enregistrement_audio = document.getElementById('b1');
let ajouter = document.getElementById('b2');
let prononcer = document.getElementById('b3');


ajouter.addEventListener('click', afficher);
enregistrement_audio.addEventListener('click', alerte);
//prononcer.addEventListener('click' , function(){synthetiser("pourquoi")});
prononcer.addEventListener('click' ,synthetiser);




let final_transcript = ''; // paramètre de base pour la reconnaissance vocale
let recognition = new webkitSpeechRecognition();
recognition.continuous = false;
recognition.interimResults = true;
recognition.onresult = function(event) 
{ 
	//alert(event.results[0][0].transcript);
	final_transcript = event.results[0][0].transcript;
	
}



function comprendre(texte){ //regex pour comprendre la commande par exemple si la personne dit planning alors on affiche le planning
	let texte_comprendre;
	let re = /planning/;
	if (texte.search(/planning/) != -1 ) {texte_comprendre = "voici le planning de votre journée";}
	if (texte.search(/note/) != -1) {texte_comprendre = "voici votre dernière note: "}
	if (text.search(/note/)!= -1) {texte_comprendre = "Voici la météo: "}
	else {texte_comprendre = "l'instruction n'est pas clair";}
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

function afficher(){
    let para = document.createElement('p');
    para.textContent = comprendre(final_transcript);
    document.body.appendChild(para);
}
function synthetiser(){
	let msg = new SpeechSynthesisUtterance();
	let voices = window.speechSynthesis.getVoices();
	msg.voice = voices[6]; //6 pour la voix française
	msg.voiceURI = 'native';
	msg.volume = 1; // 0 to 1
	msg.rate = 1; // 0.1 to 2
	msg.pitch =2; //0 to 2
	msg.text = comprendre(final_transcript);
	speechSynthesis.speak(msg);
}
