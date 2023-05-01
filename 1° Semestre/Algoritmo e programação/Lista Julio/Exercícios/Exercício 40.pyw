#escreva um programa que receba um numero inteiro de 1 a 100 e mostre na tela o numero
#por extenso



from num2words import num2words
x=int(input (" Digite um Número de 1 a 100 "))
num_ptbr=num2words(x, lang='pt-br')
if x<100 and x>0:
   print ("Seu Número é "f'{num_ptbr}')
else:
    print (" Seu Número nâo corresponde de 1 a 100 ")
    exit



















#n=int(input(" coloque o numero "));
#i = 0;
#for i <= 100:{
#    if(i == n){
#        print("Seu numero é ",n)
#    }else{
#        i+1
#        continue;
#    }
#}
#print("Seu numero não está de 0 até 100");



#Pronto
