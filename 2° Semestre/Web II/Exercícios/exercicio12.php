<?php
$val = 0;
$resultado = "";

if ($val > 0){
	$resultado = "Valor Positivo";
}
elseif ($val < 0){
	$resultado = "Valor Negativo";
}
else{
	$resultado = "Igual a Zero";
}
echo $resultado;
?>