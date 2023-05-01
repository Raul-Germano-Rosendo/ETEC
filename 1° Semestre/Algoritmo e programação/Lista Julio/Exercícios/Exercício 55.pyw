#dizemos que dois numeros sao amigos se cada um deles é igual a soma dos divisores dos
#proprios do outro. os divisores proprios de um numero positivo N sao todos os divisores
#inteiros positivos de N exceto o proprio N. Um exemplo de Numeros amigos sao 284 e 220,
#pois os divisores proprios de 220 sao 1,2,4,5,10,11,20,22,44,55 e 110.
#efetuando a soma destes numeros obtemos o resultado de 284(1+2+4+5+10+11+20+22+44+55+110=284)
#os divisores proprios de 284 sao 1,2,4,71 e 142. efetuando a soma obtemos 220(1+2+4+71+142=220)
#escreva um programa que dado dois inteiros, verifique se eles sao amigos




N,d=1500,lambda n:sum(i for i in range(1,n) if n%i==0)
print({i:d(i) for i in range(N+1) if i==d(d(i)) and i>d(i)})
