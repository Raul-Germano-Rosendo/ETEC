<?php
//criar uma função que recebe uma string como argumento e retorna a string com todas as letras em maiúsculo.
//mb_strtoupper() - Make a string uppercase.

/*function M ($texto){
	$turn_M = strtoupper($texto);
	return $turn_M;
}

$texto = "POUTA QUE PARIO";
turn_M = M($texto);
echo ($turn_M);*/

function converter_maiusculo($texto){
	$texto_maiusculo = strtoupper($texto);
	return $texto_maiusculo;
}

$texto = "hello world!";
$texto_maiusculo = converter_maiusculo($texto);
echo "Texto Original" . $texto . "<br>";
echo "Texto em Maiúsculas: " . $texto_maiusculo;
?>