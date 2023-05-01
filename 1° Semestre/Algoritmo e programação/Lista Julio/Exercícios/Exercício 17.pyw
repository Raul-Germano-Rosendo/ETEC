#um programa para gerenciar saques de um caixa eletronico deve possuir algum
#mecanismo para decidir o numero de notas de cada valor que deve ser
#disponibilizada para o cliente que realizou o saque. um possivel critério
#seria o da "distribuição otima" no sentido de que as notas de menor valor
#fossem distribuídas em numero minimo possivel. por exemplo, se a quantia
#solicitada fosse R$87. o programa deveria indicar uma nota de R$50, tres
#notas de R$10, uma nota de R$5, e duas notas de R$1. Escreva um programa
#que receba o valor de quantia solicitada e retorne a distribuição das notas
#de acordo com o criterio de distribuição otima (considere existir notas de
#R$1.00: R$2.00: R$5.00: R$10.00: R$20.00: R$50.00 e R$100.00).




valor=int(input(" Coloque o Valor "))
do100=(int(valor)/100)
(valor-do100);
do50=(int(valor)/50)
do20=(int(valor)/20)
do10=(int(valor)/10)
do5=(int(valor)/5)
do2=(int(valor)/2)
do1=(int(valor)/1)




#Pronto


