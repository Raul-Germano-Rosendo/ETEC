<?php
	$Var_A = $_POST['VarA'];
	$Var_B = $_POST['VarB'];
	if ($Var_A > $Var_B){
		echo ("$Var_A é maior que $Var_B");
	}
	else 
		echo ("$Var_B é maior que $Var_A");
	
?>