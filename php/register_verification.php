<?php 
ini_set('display_errors', 'on');
session_start();
$_SESSION['output']=shell_exec('python test.py');
if (shell_exec('python test.py')==NULL){
   header('Location: login.php?register_error=1');
}
else{
   header('Location: principale.php');
}
?>
