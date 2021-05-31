<?php
ini_set('display_errors', 'on');
session_start();
if(isset($_POST['username']) && isset($_POST['password']))
{
   echo $_POST['username'];
}
?>
