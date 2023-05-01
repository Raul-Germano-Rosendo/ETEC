#uma cia de pulverização ultiliza um aviao para pulverizar lavouras.
#os custos de pulverização dependem do tipo de praga e da área a ser
#contratada conforme a tabela:

#tipo1
#ervas daninhas R$50,00 por acre

#tipo2
#gafanhotos R$100,00 por acre

#tipo3
#broca R$150,00 por acre

#tipo4
#todos acima R$250,00 por acre



#type1=50
#type2=100
#type3=150
#type4=250


#se a area a ser pulverizada for superior a 1000 acres, o fazendeiro tem um desconto de 5%.
#em adição, qualquer fazendeiro cujo custo for maior do que R$750,00 tem um desocnto de 10%
#sobre o valor que ultrapassar os 750.
#caso ambos os descontos se aplicam, o da area é calculado antes. fazer um algoritmo que leia
#o tipo de pulverização (1 a 4) e área a ser pulverizada e imprima o valor a ser pago


acr=float(input(" Coloque o tamanho em acres "))
typ=float(input(" Coloque o tipo de 1 a quatro "))
if typ==1:
    typ=50
elif typ==2:
    typ=100
elif typ==3:
    typ=150
elif typ==4:
    typ=250

valdesc=(acr*typ -((acr*typ)*0.05))
if acr>1000:
    print (valdesc)
    if acr*typ>750:
        print (valdesc-(valdesc*0.10))



#Pronto
    
