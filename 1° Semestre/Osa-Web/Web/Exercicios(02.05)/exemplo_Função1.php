<?php
//como criar uma função que recebe dois números como argumentos e retorna a soma deles
function somar($num1, $num2) {
	$resultado = $num1 + $num2;
	return $resultado;
}
$resultado_soma = somar(5, 10);
echo "A soma de 5 e 10 é: " . $resultado_soma;
?>