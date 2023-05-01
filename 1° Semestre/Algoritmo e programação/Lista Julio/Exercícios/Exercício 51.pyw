#a serie Fibonacci é formada pela sequencia: 1,1,2,3,5,8,13,21,34,55
#escreva um programa que gere a série de FIBONACCI até o N-ésimo termo





p=int(input(" Coloque o Fechamento "))
i=1
soma=0
while (soma<=p):
    soma=soma+i
    i=i+soma
    print(soma)



#Pronto
