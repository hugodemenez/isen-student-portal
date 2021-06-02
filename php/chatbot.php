<html>
    <link rel="stylesheet" href="styles\chatbot_style.css" media="screen" type="text/css">
    <link rel="stylesheet" type="text/css" href="styles\jquery.convform.css">
    <script type="text/javascript" src="js\jquery-3.1.1.min.js"></script>
    <script type="text/javascript" src="js\custom.js"></script>
    <script type="text/javascript" src="js\jquery.convform.js"></script>
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
            <input data-conv-question="Type in your e-mail" data-pattern="^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$" id="email" type="email" name="email" required placeholder="What's your e-mail?">
            <select name="programmer" data-conv-question="So, are you a programmer? (this question will fork the conversation based on your answer)">
	            <option value="yes">Yes</option>
	            <option value="no">No</option>
            </select>
            <div data-conv-fork="programmer">
	            <div data-conv-case="yes">
	 	            <input type="text" data-conv-question="A fellow programmer! Cool." data-no-answer="true">
	            </div>
	            <div data-conv-case="no">
		            <select name="thought" data-conv-question="Have you ever thought about learning? Programming is fun!">
			            <option value="yes">Yes</option>
			            <option value="no">No..</option>
		            </select>
	            </div>
            </div>
        </form>
        </div>
    </div>
    <!-- Chatbot -->
    </body>
</html>
 