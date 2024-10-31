<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>
        雛見沢村連続怪死事件
    </title>
    <style>
        body{
            background-image: url("static/寒蝉鸣泣之时2.webp");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        audio {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
        }
    </style>
</head>
<body>
    <div style="text-align:center;">
        <form action="/index.php" method="POST">
            <h1>选择年份（1979年～1983年）:</h1>
            <input type="text" name="year">
            <input type="submit" value="查看">
        </form>
        <?php
        require_once("conn.php");
        error_reporting(0);
        if(isset($_POST["year"])){
            $year = $_POST['year'];
            $blacklist = '/ |flag|select|union|where|and|or|database|&|\||\^/i';
            $denylist = '/ph/i';
            if(preg_match_all($blacklist,$year,$matches)){
                echo "从身体流出来了：" . implode(",", $matches[0]) . "\n";
                $year = preg_replace($blacklist, '', $year);
            }
            if(preg_match_all($denylist,$year)){
                die("古手梨花死亡");
            }
            @$sql="SELECT dead, missing FROM victims WHERE year='$year' LIMIT 0,1";
            $result=mysqli_query($conn,$sql);
            $row = mysqli_fetch_array($result);
        }
        if($row){
            echo "<h2>".$row['dead']."死亡</h2>";
            echo "<h2>".$row['missing']."失踪</h2>";
        }
        ?>
    </div>
    <audio controls autoplay loop>
        <source src="static/ひぐらしのなく頃に.mp3" type="audio/mpeg">
    </audio>
</body>
</html>