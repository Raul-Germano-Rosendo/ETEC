#um posto esta vendendo combustiveis com a seguinte tabela de descontos

#alcool ; Até 25 litros, desconto de 2% por litro
#       ; Acima de 25 litros, desconto de 4% por litro
#Gasolina ;Até 25 litros, desconto de 3% por litro
#         ;Acima de 25 litros, desconto de 5% por litro

#escreva um algoritimo que leia o número de litros vendidos e o tipo de combustivel
#Codificação; (A) Alcool ; (G) Gasolina, calcule e imprima o valor a ser pago pelo cliente
#sabendo-se que o preco do litro da gasolina é de R$2,70 e o preco do litro do alcool
#é de R$1,90






A=float(input(" Insira a quantidade de Alcool "))
G=float(input(" Insira a quantidade de Gasolina "))

At=A*1.90
Gt=G*2.70
DAtMaior=At-(At/100*4)
DAtMenor=At-(At/100*2)
DGtMaior=Gt-(Gt/100*5)
DGtMenor=Gt-(Gt/100*3)


    
if A>25:
    print (DAtMaior, "Este vai ser o valor a ser pago")
elif A<=25:
    print (DAtMenor, "Este vai ser o valor a ser pago")
if G>25:
    print (DGtMaior, "Este vai ser o valor a ser pago")
elif G<=25:
    print (DGtMenor, "Este vai ser o valor a ser pago")



#Pronto




    

