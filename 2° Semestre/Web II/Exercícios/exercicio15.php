<form> action="exercicio15.php" method="post">
	<p><input type="text" name="nota1" placeholder="Informe a primeira nota"></p>
	<p><input type="text" name="nota2" placeholder="Informe a segunda nota"></p>
	<p><input type="text" name="nota3" placeholder="Informe a terceira nota"></p>
	<p><input type="text" name="nota4" placeholder="Informe a quarta nota"></p>	
	<button type="submit"> Conferir Resultado </button>
</form>

<?php
	$nota = $_POST['nota1'];
	$nota = $_POST['nota2'];
	$nota = $_POST['nota3'];
	$nota = $_POST['nota4'];
	$media = ($nota1 + $nota2 + $nota3 + $nota4)/4
	if ($media >= 7.0) echo "Sua media é: $media <br>voce foi aprovado, parabens!";
		else echo "sua media é: $media <br>voce foi reprovado :(";
?>