# ==============================
# Exercicio 
'''
Dado a lista abaixo, faça a separação em sublistas para ano  e presidente .
Iremos receber via input um determinado ano. Devemos validar se existe , procurar (e mostrar) o presidente daquele ano.
'''
dados = ["Exercicio Sublistas",[1989,1994,2002,2010],["Collor","FHC","Dilma","Luis"]]
ano = dados[1]
presidente = dados[2]

anoEscolha = int(input("Ano a pesquisar "))
achou = 0
for x in range(len(ano)):
    if (ano[x] == anoEscolha):
        print(presidente[x])
        achou=1
if (achou == 0):
    print ("Ano existe na Lista")
        
