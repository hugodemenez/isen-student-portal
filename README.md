<h1>Projet d'informatique ISEN fin de 3ème année</h1>
<img src='https://github.com/hugodemenez/Projet_2021_Informatique/blob/main/assets/JUNIA%20ISEN%20CMJN%20300%20DPI.jpg?raw=true' width=100%>

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
Nous sommes partis d'un constat et d'un problème que tous les membres du projet avaient rencontrés.
 " Il est difficile de récuperer les informations d'Aurion et de les avoir disponibles dans notre telephone sans être connecté à internet. "
 
<li>Interface web (php,html,css), une fois connecté envoie automatiquement (tous les dimanches) un mail avec l'emploi du temps de la semaine au format .csv et les nouvelles notes.</li>
<br>
<li>Alimenter la base de données avec l'identifiant, le mot de passe, l'email, le planning et les notes.</li>
<br>
<li>Checking des informations tous les jours pour voir s'il y a des changements. (attention s'il y a trop d'inscrits cela pourrait surcharger le serveur Aurion)</li>
<br>
<li>Créer un assistant vocal qui sera disponible sur la page web pour permettre de poser des questions concernant par exemple le nombre d'heures de cette semaine ou calculer la moyenne génerale</li>
<br>
<li>Créer des graphiques pour visualiser les notes</li>
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
<img src='https://raw.githubusercontent.com/hugodemenez/Projet_2021_Informatique/4c0ac15565e202905abe443e7adb6f5032e75462/assets/Diapositive1.SVG?sanitize=true' width=100%>
<img src='https://raw.githubusercontent.com/hugodemenez/Projet_2021_Informatique/4c0ac15565e202905abe443e7adb6f5032e75462/assets/Diapositive2.SVG?sanitize=true' width=100%>
<img src='https://raw.githubusercontent.com/hugodemenez/Projet_2021_Informatique/4c0ac15565e202905abe443e7adb6f5032e75462/assets/Diapositive3.SVG?sanitize=true' width=100%>
<img src='https://raw.githubusercontent.com/hugodemenez/Projet_2021_Informatique/4c0ac15565e202905abe443e7adb6f5032e75462/assets/Diapositive4.SVG?sanitize=true' width=100%>
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
        <img src='https://raw.githubusercontent.com/hugodemenez/Projet_2021_Informatique/4c0ac15565e202905abe443e7adb6f5032e75462/assets/Diapositive5.SVG?sanitize=true' width=100%>
        <br>
        <li>PHP :
        Réaliser une interface web pour utiliser l'application :
            <ul>
                <li> Consultation des données sous forme de graphique</li>
                <li> Inscription pour recevoir l'emploi du temps toutes les semaines</li>
            </ul>
        </li>
        <br>
        <img src='https://raw.githubusercontent.com/hugodemenez/Projet_2021_Informatique/4c0ac15565e202905abe443e7adb6f5032e75462/assets/Diapositive6.SVG?sanitize=true' width=100%>
    </ul>
</p>
</div>

<div id="FONCTIONNALITES">
<h2>Les fonctionnalités présentes</h2>
<li>ChatBot</li>
<p>
Nous avons eu l'idée d'ajouter un chatbot afin que l'utilisateur puisse profiter d'une nouvelle expérience et cela permet d'obtenir d'autres services.
Notre chatbot pourra par exemple afficher le planning de la semaine, le planning du jour, la moyenne, la dernière note obtenue, etc ...
L'utilisateur n'aura qu'à ouvrir la chatbox en cliquant sur l'icone en bas à droite puis le bot posera une question et l'utilisateur choisira sa réponse en cliquant dessus.
</p>
<br>
<li>Reconnaissance Vocale</li>
<p>
Nous avons souhaité ajouter une fonctionnalité de reconnaissance vocale pour nous permettre d'explorer des langages de programmations que nous ne connaissions pas forcément.
La notion de reconnaissance vocale paraît être une tâche complexe et cela nous a permi de nous challanger.
</p>
<br>
<li>Graphiques Dynamiques</li>
<p>
Pour permettre aux étudiants de suivre l'évolution de leurs notes au cours de leur scolarité, nous avons souhaité dessiner des graphiques, pour pouvoir visualiser leur forme et leur permettre de retravailler certaines matières.
</p>
<br>
<li>Station Météorologique</li>
<p>
Pourquoi pas beneficier de widgets supplémentaires qui nous seraient bien utiles lorsque l'on se prépare le matin. Nous avons donc, à l'aide d'une API, récuperé la météo de la zone géographique du campus de ISEN Lille.
</p>
</div>





