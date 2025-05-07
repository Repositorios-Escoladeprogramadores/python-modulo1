# ==============================
# Exercicio 1
'''
Problema: Criar uma solução que receba 05 numeros (em uma lista com itens inteiros) , calcule a media destes numeros e imprima a média. 
Imprima ao final QUAIS dos numeros informados é maior ou igual ao valor da media (somente os maiores)
'''

dados =[10,24,33,38,79]
media = sum(dados) /  len(dados)
print ("Media ", media)

for x in range(len(dados)):
    if(dados[x] >= media):
        print (dados[x] , " é maior ou igual a media")


# ==============================
# Exercicio 2
'''
Problema: Criar uma solução que receba 06 numeros (em uma lista com valores inteiros) .
Mostre ao final qual foi o MAIOR e o MENOR valor recebido.
'''

dados =[-50,24,33,38,79]
maior = max(dados) 
menor = min(dados) 
print ("Maior ", maior)
print ("Menor ", menor)


# outra forma 
dados =[50,-10,-133,85,482,320]
maior = dados[0] 
menor = dados[0]

for x in range(1, len(dados) ):
    if (dados[x] > maior):
        maior = dados[x]
    if (dados[x] < menor ):
        menor = dados[x]    

print ("Maior ", maior)
print ("Menor ", menor)
