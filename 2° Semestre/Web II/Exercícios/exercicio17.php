<?php
	$valorA = $_POST['valorA'];
	$valorB = $_POST['valorB'];
	
	if ($valorA < $valorB) print "$valorA $valorB";
		elseif ($valorA > $valorB) print "$valorB $valorA";
		elseif ($valorA == $valorB) print "$valorA $valorB";
	?>