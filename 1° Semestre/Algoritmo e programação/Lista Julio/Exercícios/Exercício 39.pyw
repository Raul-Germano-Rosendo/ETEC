#em diversas situações, é util o uso de difitos verificadores. digito verificador ou algarismo de controle é um
#mecanismo de autenticação utilizado para verificar a validade e a autemticidade de um valor numerico, evintando
#dessa forma fraudes ou erros de tranmissao ou digitação. uma das formas mais comuns de calculo de dígitos
#verificadores é o metodo conhecido por modulo 11. o calculo do DV no modulo 11 é feito, é feito como se segue
#para calcular o primeiro digito verificador, cada digito do numero começando da direita para a esqueira, do digito
#menos significativo para o digito mais significatico, é multiplicado na orde, por 2, depois por 3, depois por 4 e
#e assim sucessivamente, até o primeiro digito do número. o somatório dessas multiplicações é dividido por 11.
#o resto da divisao (modulo 11) é subtraido da base (11), o resultado é o digito verificador
#O banco do brasil utiliza o codigo modulo 11, substituindo X o valor do digito verificador
#quando este é 10. Escreva um programa que receba um numero com os 4 primeiros digitos de uma
#agencia e imprima o numero da agencia completo (numero - dv)





dig1=int(input(" Coloque o Digito Um "))
dig2=int(input(" Coloque o Digito Dois "))
dig3=int(input(" Coloque o Digito Três "))
dig4=int(input(" Coloque o Digito Quatro "))

mod11=(dig4*2+dig3*3+dig2*4+dig1*5)/11
print (mod11)




#pronto
