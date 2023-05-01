#escreva um algoritmo que leia 2 valores (x e y), que devem representar as coordenadas de um ponto em um plano.
#A seguir, determine qual o quadrante ao qual o ponto, ou se está sobre um dos eixos cartezianos ou na origem




x=int(input(" Coloque o eixo X "))
y=int(input(" Coloque o eixo Y "))



if x>0 and y>0:
    print (" Está no Eixo ( I ) ") 
if x>0 and y<0:
    print(" Está no Eixo ( IV ) ")
if x<0 and y>0:
    print(" Está no Eixo II ")
if x<0 and y<0:
    print (" Está no Eixo III ")

#


if x==0 and y==0:
    print (" Ele está no Ponto Inicial Do Plano Cartesiano ")


#


if x>=0 and y>=0:
    print (" Está sobre um Eixo ")
if x>=0 and y<=0:
    print(" Está sobre um Eixo ")
if x<=0 and y>=0:
    print(" Está sobre um Eixo ")
if x<=0 and y<=0:
    print (" Está sobre um Eixo ")




#Pronto
