nome=input(" Coloque o Nome " )
idade=int(input(" Coloque a Idade " ))
if idade>=18:
    print (" É maior de Idade ")
else:
    print (" Não é maior de Idade ")
resposta=input(" Quer continuar o Programa (s/n) ")
if resposta==("s"):
    resposta=True
else:
    resposta=False
while (resposta==True):
    nome=input(" Coloque o Nome " )
    idade=int(input(" Coloque a Idade " ))
    if idade>=18:
        print (" É maior de Idade ")
    else:
        print (" Não é maior de Idade ")
    resposta=input(" Quer continuar o Programa (s/n) ")
    if resposta==("s"):
        resposta=True
    else:
        resposta=False
        
