<?php
	$Sal = $_POST['Sal'];
	$novosal = 0.0;
	if ($Sal <= 1000){
		$novosal = ($Sal+($Sal/2));
		echo ("O reajuste do salário foi de $novosal");
	}
	else{
		$novosal = ($Sal*0.30+($Sal));
		echo ("O reajuste do salário foi de $novosal");
}
?>