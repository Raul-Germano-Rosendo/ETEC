#escreva um programa que determine se um numero dado N é primo ou nao


n = int(input("Coloque o Número "))
mult=0

for count in range(2,n):
    if (n % count == 0):
        mult += 1

if(mult==0):
    print("É primo")
else:
    print("Não é Primo")



#Pronto
