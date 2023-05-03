<?php
	$pesomas = $_POST['pesomas'];
	$pesofem = $_POST['pesofem'];
	$altmas = $_POST['altmas'];
	$altfem = $_POST['altfem'];
	$massamas = ($altmas * 72.7) - 58 ;
	$massafem = ($altfem * 62.1) - 44.7 ;
	print ("O PESO MASCULINO IDEAL É: $massamas");
	
	print ("O PESO FEMININO IDEAL É: $massafem");
























?>