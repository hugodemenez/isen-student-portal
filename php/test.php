<?php
include 'db_connection.php';
$conn = OpenCon();
$sql = "SELECT * FROM user";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
    echo "id: " . $row["username"]. " - Name: " . $row["password"]. " " . $row["email"]. "<br>";
  }
} else {
  echo "0 results";
}
echo "Connected Successfully";
CloseCon($conn);
?>