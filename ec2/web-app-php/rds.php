<!DOCTYPE html>
<html>
<body>

<h1>RDS db</h1>

<?php

// Setup RDS connection details
// E.g. $con=mysqli_connect('myrds.cle1covvccqa.us-east-1.rds.amazonaws.com:3306', 'root', 'password');
 
$con=mysqli_connect('RDS_HOSTNAME', 'DB_USERNAME', 'DB_PASSWORD');

// Check connection
if (mysqli_connect_errno($con))
  {
  echo "Failed to connect to RDS/MySQL: " . mysqli_connect_error();
  }else {
  echo "Connected to RDS/MySql DB";
  }

mysqli_close($con);
?>

</body>
</html>
