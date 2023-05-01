#chama se ano bissexto o ano ao qual é acrescentado um dia extra, ficando ele com 366 dias, um dia a mais do que os
#anos anos normais de 365 dias, ocorrendo a cada quatro anos. escreva um programa que verifique se um ano é bissexto
#um ano bissexto se ele é divizivel por 4. entretanto, se o ano é divisivel por 100, ele não é bissexto. mas se ele
#for divizivel por 400, ele volta a ser bissexto.

#sao anos bissextos:1600, 1996, 2000, 2004, 2008, 2012, 2016, 2400, 2800
#nao sao: 1500, 1974, 1982, 193, 1990, 2018, 2022, 2030, 2038.



ano=int(input(" Coloque o Ano para descobrir se é bissexto ou Não "))

resp=ano%4



if resp==0:
    print (" Ano Bissexto ")
else:
    print (" Não é ano bissexto ")



#Pronto
