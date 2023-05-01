#Em uma certificação são feitos 5 exames (I,II,III,IV,V). escreva um programa que leia as notas destes exames e
#imprima a classificação do aluno, sabendo que a média é 70.

#A
#passou em todos os exames

#B
#passou em I,II mas nao em III ou V

#C
#passou em I e II, III ou IV, mas nao em V


ex1=int(input(" Coloque a nota do exame I "))
ex2=int(input(" Coloque a nota do exame II "))

ex3=int(input(" Coloque a nota do exame III "))
ex4=int(input(" Coloque a nota do exame IV "))

ex5=int(input(" Coloque a nota do exame V "))

if ex1>=7:
    ex1==True
else:
    ex1==False
if ex2>=7:
    ex2==True
else:
    ex2==False
if ex3>=7:
    ex3==True
else:
    ex3==False
if ex4>=7:
    ex4==True
else:
    ex4==False
if ex5>=7:
    ex5==True
else:
    ex5==False
if ex5==False:
    print (" Aluno nota ' C ' ")
if ex3==False:
    print (" Aluno nota ' B ' ")
if ex1==True and ex2==True and ex3==True and ex4==True and ex5==True:
    print (" Aluno nota ' A ' ")




#Pronto
