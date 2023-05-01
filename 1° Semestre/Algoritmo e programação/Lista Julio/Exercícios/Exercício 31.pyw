#No futebol americano, usa-se o Quarterback Rating como um índice que indica o desempenho do
#quarterback (quanto maior, melhor). ele é calculado como indicado a seguir: Calcula-se o
#percentual de passes completados em relação aos passes tentados pelo quarterback. Deste
#valor subtrai-se 0,3 e divide-se por 0,2. Este valor deve ser maior que 2,375 ou menor que
#ZERO (caso seja, ajusta-se o valor para 2,375 ou 0, respectivamente).
#Em seguida, calcula-se a razão de jardas passadas pela quantidade de passes tentados.
#Deste valor, subtrai-se 3 e divide-se por 4. Novamente, este valor nao deve ser maior
#que 2,475 ou menor que 0 (caso seja, procede como o caso anterior).


# Passes completados

PT=int(input(" Passes Tentados "))
PC=int(input(" Passes completados "))
QR0=(PC/PT)
QR1=(QR0*12)-0.3

if QR1>2.475:
    print (2.475)
elif QR1<0:
    print ("0")

    
#Pronto
