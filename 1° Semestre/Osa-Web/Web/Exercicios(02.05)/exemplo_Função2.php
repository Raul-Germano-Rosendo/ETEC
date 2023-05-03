<?php
//como criar uma uma função que receba um string como argumento e retorna o número de caracteres da string
function contar_caracteres($texto) {
	$num_caracteres = strlen($texto);
	return $num_caracteres;
}
$texto = "Hello, world!";
$num_caracteres = contar_caracteres($texto);
echo "O texto tem " . $num_caracteres . " caracteres.";
?>