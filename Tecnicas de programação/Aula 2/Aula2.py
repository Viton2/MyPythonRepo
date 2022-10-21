lista = []  # Cria uma lista vazia
# lista = list()                                 # Cria uma lista vazia usando a classe list
print("Digite [0] para sair")
while True:
    valor = int(input("Valor: "))
    if valor == 0:  # Condição de saída
        break  # Sai de uma estrutura de repetição
    lista.append(valor)  # Acrescenta o valor v no final da lista

# Fim do While

print('Quantidade de elementos da lista: ', len(lista))
print('Soma: ', sum(lista))
print('Maior valor: ', max(lista))
print('Menor valor', min(lista))
pesquisa = int(input('Valor da pesquisa: '))

if pesquisa in lista:
    print('Valor encontrado!')
    posicao = lista.index(pesquisa)
    print('Posição do valor da pesquisa na lista: ', posicao)
else:
    print('Valor não encontrado.')

lista.sort()  # lista.sort(reverse = False)
print('Lista na ordem crescente: ', lista)
lista.insert(1, 33)
print(lista)  # lista.insert(índice, item)
# lista.reverse()                              0 # Errado! Não coloca na ordem decrescente
lista.sort(reverse=True)  # Correto! Ordem decrescente
print('Decrescente: ', lista)
print('Média: ', sum(lista) / len(lista))  # Média dos valores da lista

''' - Dica

Porcentagem dos números maiores que dez na lista.
Teste 1 = lista = [1, 33]             Saída: Porcentagem 50
Teste 2: lista = [1, 2, 33]           Saída: Porcentagem 33.3
Regra de três:      100%  -  x%
                  O todo  - uma parte / todo * 100
Isolando o x = uma parte * 100 / todo   # x = uma parte / todo 100

'''
