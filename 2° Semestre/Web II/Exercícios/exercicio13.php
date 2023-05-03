<form method="POST">
<input type = "text" name = "valor">
<input type= "submit" value ="carregar">
</form>

<?php

//efetue um algoritmo PHP que recena um valor digitado pelo usuário e imprima o texto "o valor é maior que 10" caso isso seja verdade
//caso nao, imprima "o Valor é menor que 10"


$valor= $_POST['valor'];
if($valor > 10){
	echo "Valor é maior que 10";
}
else{
	echo "valor é menor que 10";
}
?>

<?php
/*
<form action="nome_do_arquivo" method="post">
	<p>
	Insira um Valor: <input type="text" name="o_que_estiver_entre_[]_no_caso_valor">
	</p>
	<p>
	input type="submit" value="enviar"
	input type="reset" value="limpar"
	</p>
</form>
*/
?>