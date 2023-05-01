#uma cidade deseja sincornizar os semáforos, com isso quando um semáforo abre
#(fica verde), os veiculos que nele estavam parados tendem a encontrar os
#proximos semáforos tambem abestos, para que isso seja feito, os proximos
#semáforos precisam abrir pouco depois, assim ao abrir o semáforo, um veiculo
#começa a acelerar ate atingir a velocidade permitida, que mantem ate chegar
#ao proximo semáforo, levando um certo tempo para percorrer essa distancia,
#para que encontre o próximo semáforo aberto, este deve abrir um pouco antes
#da chegada do veiculo (por exemplo:3 segundos antes). faça assim um algoritmo
#que informe quanto tempo depois de um semáforo deve abrir dadas as seguintes
#informações

#A . a distancia desde o semáforo anterior
#B . a velocidade permitida da via
#C . a aceleraçao tipica dos carros

a=int(input(" Distancia do semáforo anterior "))
b=int(input(" Velocidade permitida da via em Km/h "))
c=int(input(" A aceleraçao típica dos carros em Km/h "))

r=b*c
r2=r/a
print ((r2/a*b)," segundos ")



#Pronto

