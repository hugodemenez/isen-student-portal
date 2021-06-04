let enregistrement_audio = document.getElementById('b1');
let ajouter = document.getElementById('b2');
let prononcer = document.getElementById('b3');


ajouter.addEventListener('click', afficher);
enregistrement_audio.addEventListener('click', alerte);
prononcer.addEventListener('click' , function(){synthetiser("Pourquoi")});





let final_transcript = '';
let recognition = new webkitSpeechRecognition();
recognition.continuous = false;
recognition.interimResults = true;
	 


recognition.onresult = function(event) 
{ 
	//alert(event.results[0][0].transcript);
	final_transcript = event.results[0][0].transcript;
	
}


function synthetiser(message){
	let msg = new SpeechSynthesisUtterance();
	let voices = window.speechSynthesis.getVoices();
	msg.voice = voices[6]; // Note: some voices don't support altering params
	msg.voiceURI = 'native';
	msg.volume = 1; // 0 to 1
	msg.rate = 1; // 0.1 to 2
	msg.pitch =1; //0 to 2
	msg.text = message;
	speechSynthesis.speak(msg);
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
    para.textContent = final_transcript + ' est le mot indiqué';
    document.body.appendChild(para);
}

