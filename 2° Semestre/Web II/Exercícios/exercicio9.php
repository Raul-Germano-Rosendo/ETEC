<?php
//crie um algoritmo que receba um numero digitado pelo usuário e verifique se esse valor é positivo, negativo ou igual a zero
//a saida deve ser; "Valor Positivo", "Valor Negativo" ou "Igual a Zero"

$receba = 0;
$resultado = "";
if($receba > 0){
$resultado = "Valor Positivo";
}elseif($receba < 0){
$resultado = "Valor Negativo";
}else{
$resultado = "Igual a Zero";
}
echo $resultado;