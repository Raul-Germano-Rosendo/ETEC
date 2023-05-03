<?php
if (isset($_POST['palavra']) && isset($_POST['letra'])){
	$frase = $_POST['palavra'];
	$letra = $_POST['letra'];
} else {
	echo "Dados Não Recebidos!";
}
//Essa função faz tudo por mim
$cont = substr_count($frase, $letra);
echo $cont;

?>