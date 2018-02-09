<?php
  $link = @mysql_connect(localhost, "root", "123456");
  if(!$link){
   echo "Error connecting to MySQL: " . $mysql_error();
   exit();
  }
  $db = @mysql_selectdb("rcl-ns");
  if(!$db){
    echo "Error connecting to the database: " . $mysql_error();
    exit();
  }
  $query = "INSERT INTO ns(email) VALUES($email);";
  $result = @mysql_query($query);
  if(!$result){
    echo "Couldn't add your email. Try again....";
    exit();
  }
  else{
    @mysql_close($link);
    echo "<script language='javascript'>";
    echo "alert('Succesfully saved your email!')";
    echo "</script>";
  }
?>
