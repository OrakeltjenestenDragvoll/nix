 <?php
 header ('Content-type: text/html; charset=utf-8');
?>
 <!DOCTYPE HTML>
<html>
<head>
<title>Orakeltjenesten Dragvoll</title>
<link rel="stylesheet" href="style.css" type="text/css" media="screen" />
    <link href="slider/themes/1/js-image-slider.css" rel="stylesheet" type="text/css" />
    <script src="slider/themes/1/js-image-slider.js" type="text/javascript"></script>
    <link href="slider/generic.css" rel="stylesheet" type="text/css" />
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.3.0/jquery.min.js"></script>

<script>
var auto_refresh = setInterval(
function()
{
$('#loaddiv').load('ajax2.php');
}, 3000);
$(document).ready(function(){
$('#loaddiv').load('ajax2.php')
})
</script>
</head>

<body>
 <div id="box">

<img src="header.png" alt="" />

<div id="sliderFrame">
        <div id="slider">
			<!-- img src="slider/images/1.jpg" alt="" / -->
			<img src="slider/images/3.jpg" alt="" />
			<img src="slider/images/4.jpg" alt="" />
			<img src="slider/images/5.jpg" alt="" />
			<img src="slider/images/6.jpg" alt="" />
			<img src="slider/images/7.jpg" alt="" />
			<img src="slider/images/8.png" alt="" />
		</div>

</div>

<div id="status">
<p class="beskjed"><?php
    mysql_connect("localhost", "intern", "dennisorakel") or die(mysql_error("Kunne ikke koble til serveren"));
    mysql_select_db("intern") or die(mysql_error());
	$data = mysql_query("SELECT * FROM tavle WHERE tema='info' ORDER BY id desc limit 3") or die(mysql_error());
	while($info = mysql_fetch_array($data)) {
	echo $info['beskjed'];
	}
	mysql_close();
?></p>

</div>


<img src="monitor.png" alt="" />

<div id="printmon">

<?php include 'ajax2.php'; ?>

</div>

<div id="footer">
</div>

</div>

</body>

</html>