#dado um pais A. com 5.000.000 de habitantes e uma taxa de natalidade de 3% ao ano, e um
#um pais B com 7.000.000 de habitantes e uma taxa de natalidade de 2% ao ano, escreva um
#programa, que imprima o tempo necessário para que a população do país A ultrapasse a
#população do pais B



#pais A tem (5.000.000)
#A adquire *0.03 ao ano

#pais B tem (7.000.000)
#B adquire *0.02 ao ano


ano=0
a=5000000
b=7000000



while b>a:
    populacaopaisa=a*0.03
    populacaopaisb=b*0.02
    a=a+populacaopaisa
    b=b+populacaopaisb
    ano=ano+1
print(ano,"Anos")



#Pronto
