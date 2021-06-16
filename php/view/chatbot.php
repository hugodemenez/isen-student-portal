<html>
    <link rel="stylesheet" href="../styles/chatbot_style.css" media="screen" type="text/css">
    <link rel="stylesheet" type="text/css" href="../styles/jquery.convform.css">
    <script type="text/javascript" src="../js/jquery-3.1.1.min.js"></script>
    <script type="text/javascript" src="../js/custom.js"></script>
    <script type="text/javascript" src="../js/jquery.convform.js"></script>
    <script src="https://kit.fontawesome.com/ed342dc3ca.js" crossorigin="anonymous"></script>
    <head>

        
    </head>
    <body class="neutral">
    <!-- Chatbot -->
    <div class="chat_icon">
    <i class="fas fa-comments"></i>
    </div>

    <div class="chat_box">
        <div class="conv-form-wrapper">
        <form action="" method="GET" class="hidden">
            <input data-conv-question="Bonjour" data-pattern="^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]">
            <input data-conv-question="Type in your e-mail" data-pattern="^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$" id="email" type="email" name="email" required placeholder="What's your e-mail?">
            <select name="programmer" data-conv-question="En quoi puis-je vous aider ?">
	            <option value="planning">planning</option>
	            <option value="note">note</option>
            </select>
            <div data-conv-fork="programmer">
	            <div data-conv-case="planning">
	 	            <input type="text" data-conv-question="Votre planning est le suivant :">
	            </div>
	            <div data-conv-case="note">
		            <select name="note" data-conv-question="Voulez-vous votre dernière note ?">
			            <option value="Oui">Oui</option>
			            <option value="Non">Non</option>
		            </select>
                    <div data-conv-fork="note">
                        <div data-conv-case="Oui">
                            <input type="text" data-conv-question="Votre note est :">
                        </div> 
                        <div data-conv-case="Non">
                            <input type="text" data-conv-question="Tant pis">
                        </div> 
	            </div>
            </div>
    <!-- Chatbot -->
        </form>
    </body>
</html>
 