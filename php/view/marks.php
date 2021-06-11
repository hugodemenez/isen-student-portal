<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Notes</title>
</head>
<body>
    <?php
        $username=$_SESSION['username'];
        include '../db/db_connection.php';
        $conn = OpenCon();
        $results = $conn->query("SELECT * FROM marks WHERE username = '$username'");
        while($row =$results->fetch_assoc()){
            echo "<input type='text' data-conv-question='".$row['title'].' : '.$row['mark']."'data-no-answer='true'>";
        }
    ?>  
</body>
</html>