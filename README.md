<h1>Projet d'informatique ISEN fin de 3ème année</h1>

<header>

<li><a href="#IDEE"> Idée du projet </a></li>
<li><a href="#SCRUM"> Utilisation du Scrum </a></li>
<li><a href="#STRUCTURE"> Structure du projet  </a></li>
<li><a href="#LANGAGES"> Langage de programmation  </a></li>

</header>


<div id="IDEE">
<h2>Idée du projet</h2>
<p>
<li>Interface web (html), une fois connecté envoie automatiquement (tous les dimanches) un mail avec l'emploi du temps de la semaine au format .ics et les nouvelles notes.</li>
<br>
<li>Alimente la base de donnée avec l'identifiant, le mot de passe, l'email, le planning et les notes.</li>
<br>
<li>Checking des informations tous les jours pour voir s'il y a des changements. (attention s'il y a trop d'inscrits cela pourrait surcharger le serveur Aurion)</li>
<br>
<li>Créer un assistant vocal qui sera disponible sur la page web pour permettre de poser des questions concernant par exemple le nombre d'heures de cette semaine ou calculer la moyenne génerale</li>
</p>
</div>


<div id="SCRUM">
<h2>Utilisation du Scrum</h2>
<img src='assets\scrum.png'>
</div>

<div id="STRUCTURE">
<h2>Structure du projet</h2>
<img src='assets\projet_2021.png'>
</div>

<div id="LANGAGES">
<h2>Langage de programmation</h2>
<p>
    <ul>
        <li>Python :
        WebAurion ne possède pas d'API, nous utilisons donc la méthode du web-scraping au travers d'un headless web-browser pour récupérer les données comme :
            <ul>
                <li>Verification des données d'indentification </li>
                <li>Les notes </li>
                <li>Le planning </li>
            </ul>
        </li>
        <img src='assets\headless_webbrowser.png' width='400px'>
        <img src='assets\scraping.jpg' width='400px'>
        <br>
        <li>PHP :
        Réaliser une interface web pour utiliser l'application :
            <ul>
                <li> Consultation des données sous forme de graphique</li>
                <li> Instription pour recevoir l'emploi du temps toutes les semaines</li>
            </ul>
        </li>
    </ul>
</p>
</div>





