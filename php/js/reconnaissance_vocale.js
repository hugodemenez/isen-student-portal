let enregistrement_audio = document.getElementById('b1');
let ajouter = document.getElementById('b2');


ajouter.addEventListener('click', afficher);

enregistrement_audio.addEventListener('click', alerte);
let final_transcript = '';
let recognition = new webkitSpeechRecognition();
recognition.continuous = false;
recognition.interimResults = true;


recognition.onresult = function(event) 
{ 
	//alert(event.results[0][0].transcript);
	final_transcript = event.results[0][0].transcript;
	
}

function alerte(){
		recognition.lang = "fr-FR";
		recognition.start();
}

function afficher(){
    let para = document.createElement('p');
    para.textContent = final_transcript + ' est le mot indiqué';
    document.body.appendChild(para);
}