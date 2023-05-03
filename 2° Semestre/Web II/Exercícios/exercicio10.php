<?php
//crie um programa para informar se o aluno esta aprovado ou reprovad
//para ser aprovado, a nota precisa ser maior e igual do que 6.

$nota = 10;
$resultado = "";
if ($nota > 6){
$resultado = "Aprovado";
}else{
$resultado = "Reprovado";
}
echo $resultado;