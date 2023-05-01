#construa um programa que receba um numero e verifique se ele é um numero triangular.
#um numero é triangular quando seu resultado do produto de tres numeros consecutivos.
#exemplo: 24=2x3x4


n = int(input(" Digite um numero "))
a=0
b=1
c=2
d=0
while d<n:
    a=a+1
    b=b+1
    c=c+1
    d=a*b*c
if d==n:
    print(" Esse numero é triangular ")
else:
    print(" Esse numero nao é triangular ")



#Pronto
