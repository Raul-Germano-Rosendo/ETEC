#um circuito eletronico é composto de duas resistencias R1 e R2 em paralelo,
#e ambas em sequencia de uma resistencia R3. faça um algoritmo para calcular
#a resistencia equivalente desse circuito

R1 = int(input(" Coloque a resistência em Ohms da primeira "))
R2 = int(input(" Coloque a resistência em Ohms da segunda "))
R3= int(input(" Coloque a resistência em Ohms da terceira "))
Rtotal=R1+R2+R3
print (((Rtotal)," Ohms, Essa é a resistência equivalente"))

#Pronto
