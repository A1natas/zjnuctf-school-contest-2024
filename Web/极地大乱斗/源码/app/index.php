<?php
error_reporting(0);
include ('./cookies.php');

$name=$_POST["name"];

if(!isset($name)){
    $name="ctfer";
}

$user=new ctf($name);
$ser_user=base64_encode(serialize($user));

setcookie("session",$ser_user);
echo "欢迎".$name;
