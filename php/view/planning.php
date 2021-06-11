<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Planning</title>
</head>
<body>
<?php 
    $username=$_SESSION['username'];
    include '../db/db_connection.php';
    $conn = OpenCon();
    $results = $conn->query("SELECT * FROM planning WHERE username = '$username'");
    while( $row =$results->fetch_assoc()){
        echo "<p> Le ".$row['date'].' de '.$row['start'].' à '.$row['end'].' en '.$row['room'].' avec '.$row['teacher'].' pour le cours : '.$row['subject']."</p>";
    }
?>

</body>
</html>