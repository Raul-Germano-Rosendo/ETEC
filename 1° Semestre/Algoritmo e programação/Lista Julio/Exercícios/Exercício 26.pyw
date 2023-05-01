#escreva um programa que leia 3 valores e escreva a soma dos 2 maiores.

a=int(input(" Escreva o valor de A "))
b=int(input(" Escreva o valor de B "))
c=int(input(" Escreva o valor de C "))


if a>=b and a>=c and b>c:
    print (a+b)
elif a>=b and a>=c and c>b:
    print (a+c)
elif b>=a and b>=c and a>c:
    print (b+a)
elif b>=a and b>=c and c>a:
    print (b+c)
elif c>=a and c>=b and a>b:
    print (c+a)
elif c>=a and c>=b and b>a:
    print (c+b)

#codigo rede fechada
    #Pronto
