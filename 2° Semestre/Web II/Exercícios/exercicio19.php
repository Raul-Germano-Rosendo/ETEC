
<?php
	$idade = $_POST['idade'];
	
	if ($idade < 18) echo "O Usuário não pode acessar o Conteúdo";
		else echo "Acesso concedido +18";
?>