<?php
	$nota1 = $_POST['nota1'];
	$nota2 = $_POST['nota2'];
	$nota3 = $_POST['nota3'];
	$nota4 = $_POST['nota4'];
	$media = ($nota1 + $nota2 + $nota3 + $nota4)/4;
	if ($media >= 7.0) echo "Sua media é: $media <br>voce foi aprovado, parabens!";
		else echo "sua media é: $media <br>voce foi reprovado :(";
?>