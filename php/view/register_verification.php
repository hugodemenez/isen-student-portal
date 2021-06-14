<?php 
ini_set('display_errors', 'on');

session_start();
$username_register=$_POST['username_register'];
$password_register=$_POST['password_register'];
$email_register=$_POST['email_register'];
include '../db/db_connection.php';
$conn = OpenCon();
$results = $conn->query("SELECT * FROM user WHERE username='$username_register'");
if (mysqli_num_rows($results)==1){
    header('Location: ../index.php?register_error=1');
}
else{
    $item=$_POST['username_register'];
    $item2=$_POST['password_register'];
    set_time_limit (20);
    $tmp = exec("python3 ../scripts/aurion_check.py $item $item2");
    echo $tmp;
    if ($tmp==true){
        $results = $conn->query("INSERT INTO user VALUES ('$username_register','$password_register','$email_register')");
        $_SESSION['username']=$username_register;
        file_put_contents("../scripts/waiting_list.txt", "1");
        header('Location: ../principale.php');
    }
    


}
CloseCon($conn);
?>
