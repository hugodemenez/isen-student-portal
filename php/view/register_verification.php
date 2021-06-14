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
    $item=$_POST['username_register'];
    $item2=$_POST['password_register'];
    $item3=$_POST['email_register'];
    $item4=$_POST['niveau_register'];
    $item5=$_POST['specialite_register'];
    set_time_limit (20);
    $tmp = exec("python /home/ubuntu/aurion_check.py $item $item2 $item3 $item4 $item5 &");
    echo $tmp;
    if ($tmp==true){
        $results = $conn->query("INSERT INTO user VALUES ('$username_register','$password_register','$email_register')");
        $_SESSION['username']=$username_register;
        file_put_contents("/home/ubuntu/waiting_list.txt", "1");
        header('Location: ../principale.php');
    }
    else{
        header('Location: ../index.php?register_error=1');
    }


}
CloseCon($conn);
?>
