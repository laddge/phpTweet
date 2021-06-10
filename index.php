<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>phpTweet</title>
</head>
<body>
<form action="" method="POST">
<input name="content"><button type="submit">Tweet</button>
</form>
<?php
    if(isset($_POST['content'])){
        $content = $_POST['content'];
        $url = shell_exec('python3 tweet.py \'' . $content . '\'');
        echo '<a href="' . $url . '">' . $url . '</a>';
    }
?>
</body>
</html>
