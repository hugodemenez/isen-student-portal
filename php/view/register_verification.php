<?php 
ini_set('display_errors', 'on');
session_start();
$username_register=$_POST['username_register'];
$password_register=$_POST['password_register'];
$email_register=$_POST['email_register'];
$niveau_register=$_POST['niveau_register'];
$specialite_register=$_POST['specialite_register'];
include '../db/db_connection.php';
$conn = OpenCon();
$results = $conn->query("SELECT * FROM user WHERE username='$username_register'");
if (mysqli_num_rows($results)==1){
    header('Location: ../index.php?register_error=1');
}
else{
    $results = $conn->query("INSERT INTO user VALUES ('$username_register','$password_register','$email_register')");
    CloseCon($conn);
    $username=$username_register;
    header('Location: ../principale.php');
}
?>
