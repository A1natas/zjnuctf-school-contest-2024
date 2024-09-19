<?php
$conn=mysqli_connect("0.0.0.0","ctf","ctf","incident");
if (!$conn)
{
    echo("连接错误: " . mysqli_connect_error());
} 
