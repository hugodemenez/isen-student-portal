<h1>Projet d'informatique ISEN fin de 3ème année</h1>

<header>

<li><a href="#IDEE"> Idée du projet </a></li>
<li><a href="#GESTION"> Gestion du projet </a></li>
<li><a href="#SCRUM"> Utilisation du Scrum </a></li>
<li><a href="#STRUCTURE"> Structure du projet  </a></li>
<li><a href="#INSPIRATION"> Inspiration pour la projet  </a></li>
<li><a href="#LANGAGES"> Langage de programmation  </a></li>
<li><a href="#FONCTIONNALITES"> Fonctionnalités  </a></li>
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

<div id ="GESTION">
<h2>Gestion de projet</h2>
<img src='https://github.com/hugodemenez/Projet_2021_Informatique/blob/4b599a2f103d4208800308d49610600feba39c62/assets/gantt.svg?sanitize=true' width=100%>
<p>Nous avons créé un projet sur github avec une liste des différentes tâches classées selon leur état d'avancement :</p>
<li><a href ='https://github.com/hugodemenez/Projet_2021_Informatique/projects/1'>Suivre l'état d'avancement du projet</a></li>
<br>
<p>Nous nous sommes entendus pour avoir une répartition équitable des tâches :</p>
<img src='https://github.com/hugodemenez/Projet_2021_Informatique/blob/4b599a2f103d4208800308d49610600feba39c62/assets/repartition.svg?sanitize=true' width=100%>
</div>

<div id="SCRUM">
<h2>Utilisation du Scrum</h2>
<img src='assets\Méthode_SCRUM.gif' width=100%>
</div>

<div id="STRUCTURE">
<h2>Structure du projet</h2>
<img src='https://github.com/hugodemenez/Projet_2021_Informatique/blob/171dee09402def314a4c13d4d688bcf2ec456399/assets/Diapositive1.SVG?sanitize=true' width=100%>
<img src='https://github.com/hugodemenez/Projet_2021_Informatique/blob/171dee09402def314a4c13d4d688bcf2ec456399/assets/Diapositive2.SVG?sanitize=true' width=100%>
<img src='https://github.com/hugodemenez/Projet_2021_Informatique/blob/5565ed569cd0083ae62235b7543a8a96bb6f99ee/assets/Diapositive2.SVG?sanitize=true'>
</div>

<div id="INSPIRATION">
<h2>Inspiration pour le projet</h2>
<img src='assets/login-form-exemple.gif' width=100%>
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
        <img src='https://github.com/hugodemenez/Projet_2021_Informatique/blob/a579c3dd82197ade58e5c8727bf4661bed7ccd28/assets/Diapositive3.SVG?sanitize=true' width=100%>
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

<div id="FONCTIONNALITES">
<h2>Les fonctionnalités présentes</h2>
<li>ChatBot</li>
<p>
Nous avons eu l'idée d'ajouter un chatbot afin que l'utilisateur puisse profiter d'une nouvelle expérience et cela permet d'obtenir d'autres services.
Notre chatbot pourra par exemple afficher le planning de la semaine, le planning du jour, la moyenne, la dernière note obtenue, etc ...
L'utilsateur n'aura qu'à ouvrir la chatbox en cliquant sur l'icone en bas à droite puis le bot posera une question et l'utilisateur choisira sa réponse en cliquant dessus.
</p>
<br>
<p>

</p>
</div>





