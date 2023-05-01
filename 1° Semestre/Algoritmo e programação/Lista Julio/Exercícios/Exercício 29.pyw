#escreva um programa que calcule o desconto previdenciário de um funcionário. dado um salario o programa deve
#retornar o valor do desconto proporcional ao mesmo. o calculo segue a regra: o desconto é de 11% do valor do
#salario, entretanto, o valor maximo de desconto é 334,29, o que seja menor


sal=float(input(" Coloque o salário "))
desc=11%sal
valsar=sal-desc
if desc<=334.29:
    print(sal-334.29)

else:
    print(valsar)


#Pronto

