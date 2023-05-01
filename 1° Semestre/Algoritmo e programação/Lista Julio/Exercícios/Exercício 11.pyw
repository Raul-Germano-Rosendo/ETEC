#faça um algoritimo para calcular a nota semestral de um aluno, a nota semestral
#é obtida pela media aritmética entre a nota de 2 bimestres.
#cada nota de bimestre é composta por 2 notas de provas

#ns = nota semestral
#x2
#ma = media aritmetica
#x2
#nb = nota bimestral
#x2
#np = nota de prova

nt01 = int(input(" Insira a nota da primeira Prova do primeiro Bimestre "))
nt02 = int(input(" Insira a nota da segunda Prova do primeiro Bimestre "))
nb0=(nt01+nt02)/2

#

nt11 =int(input(" Insira a nota da primeira Prova do segundo Bimestre "))
nt12 =int(input(" Insira a nota da segunda Prova do segundo Bimestre "))
nb1=(nt11+nt12)/2

#

ma=(nb0+nb1)/2
ns=ma

#

print (" A nota Semestral deste aluno foi",(ns))


#Pronto
