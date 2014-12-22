<?php
header ('Content-type: text/html; charset=iso-8859-1');
?>
<head>
<link rel="stylesheet" href="style.css" type="text/css" media="screen" />
</head>
<div style="width:100%; margin:auto; float:left;font-size:36px;">
<div style="width:100%; height:auto; margin-top:4px;">
<table style="width:100%; align="center"; rules="rows">
<?php
    mysql_connect("localhost", "intern", "dennisorakel") or die(mysql_error("Kunne ikke koble til serveren"));
    mysql_select_db("printmon") or die(mysql_error());

    $printers = array('b4n4','b6bn4','b6bn3','b7n3','b10n3h','b10n3v','b12n5','i3n3','pavb2etg');
    $printername = array('Bygg 4.3','Bygg 6b.4','Bygg 6b.3','Bygg 7.3','Grava H','Grava V','Bygg 12.5','Idr 3.3','Pav B 2etg');

    for ($b = 0; $b < 9; $b++) {
    $res = mysql_query("SELECT * FROM $printers[$b] ORDER BY id desc limit 1") or die(mysql_error());
    $status = mysql_fetch_array($res);
    $status = $status['status'];
	
	if ($status == 'Sleep mode on') $status = 'OK';
	if ($status == 'Alert') $status = 'OK';
	if ($status == 'Energy Saver Mode') $status = 'OK (Energy Saver Mode)';
	if ($status == 'Warming Up...') $status = 'OK (Warming Up...)';
	if ($status == 'Printing...') $status = 'OK (Printing...)';
	if ($status == 'Ready') $status = 'OK';
	if (substr($status,0,2) == 'OK') {
    $status = "<span style='color:green;'>" . $status . "</span>";
    }


	if ($status == 'Cartridge Almost Empty') $status = 'Replace Toner';
	if (($status == 'Out of Paper') || ($status == 'Replace Toner') || ($status == 'Call Service')) {
	$status = "<span style='color:#FF6600;'>" . $status . "</span>";
	}

	if ($status == 'Cartridge Empty') $status = 'Toner Empty';
	if ($status == 'Paper Misfeed') $status = 'Paper Jam';
	if ($status == '') $status = 'No response';
	if (($status == 'Paper Jam') || ($status == 'No response') || ($status =='Cover Open') || ($status == 'Error') || ($status == 'Offline') || ($status == 'Toner Empty')) {
	    $status = "<span style='color:red;'><blink>" . $status . "</blink></span>";
    }

    echo "<tr class='border'><td style='width: 250px; align='left' height='0'>" . $printername[$b] . ":</td><td style='padding-left:32px;' align='left' height='0'>" . $status . "</td></tr>";
    }

	mysql_close();

?>
</table>
</div>
</div>