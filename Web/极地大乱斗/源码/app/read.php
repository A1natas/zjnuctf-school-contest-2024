
<?php
error_reporting(0);
require('./cookies.php');
$cookies=$_COOKIE["session"];

$name=unserialize(base64_decode($cookies));

 if ($name->name==="石头人"||$name->name==="墨菲特"){
     echo"你并不喜欢我，你只是喜欢我的R".'<br>';
 }elseif($name->name==="小鱼人"){
     echo"小鱼人是最最最最，最尼玛好玩的".'<br>';
 }elseif($name->name==="剑魔"){
     echo"我带错了，带了疾跑，你吗一个人摸不到，点了"."<br>";
 }elseif($name->name==="寒冰"){
     echo"我再也不玩寒冰了"."<br>";
 }


 if ($name->power!=="admin"){
     die("你还不是admin！这里不给你看！");
 }
 echo "欢迎管理员！,请随便查查文件吧";
$file=$_POST['file'];

 if (!isset($file)){
     die("还没有输入文件呢");
 }

 if ($file!=="cookies.php"&&$file!=="index.php"&&$file!=="read.php"){
     die($file."不可以读取哦");
 }

 $context=file_get_contents($file);
 echo $file."文件内容如下".$context;
