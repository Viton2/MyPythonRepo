"""   CEUB   -   Bacharelado em Ciência da Computação (BCC)   -   Prof. Barbosa
Teclas de atalho: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha.

Obs.: resolva com lista

- Elabore o programa que leia a altura e o gênero (‘m’ pra masculino e ‘f’ pra feminino)
de um grupo de pessoas. Gere a tela de saída com as seguintes informações:
maior altura do grupo, menor altura do grupo, quantidade de homens e quantidade de mulheres.
Teste 1: 1.80, m;  1.60, f;  0             Saída: Maior=1.80   Menor=1.60   Masc.= 1   Fem.= 1
Teste 2: 1.80, m;  1.60, f;  1.7, m; 0     Saída: Maior=1.80   Menor=1.60   Masc.= 2   Fem.= 1
Teste 3: 1.80, m;  1.60, f;  1.7, f; 0     Saída: Maior=1.80   Menor=1.60   Masc.= 1   Fem.= 2
"""

l_altura = []                                   # Duas formas de criar lista vazia
l_genero = list()
print('Digite [0] pra sair')
while True:                                     # Início da estrutura de repetição (while)
    altura = float(input("Altura: "))           # Recebe a altura. Indentação obrigatória.
    if altura == 0:
        break                                   # Sai da estrutura de repetição (while)
    l_altura.append(altura)
    genero = input("[m] para Masculino\n[f] para Feminino: ")  # Recebe o gênero
    l_genero.append(genero)
# fim do while
print("Maior altura no grupo:", max(l_altura))
print("Menor altura no grupo:", min(l_altura))
print("Quantidade de homens:", l_genero.count('m'))  # Conta quantas vezes o 'm' aparece na lista
print("Quantidade de mulheres:", l_genero.count('f'))
# print(f"Quantidade de mulheres: {l_genero.count('f')}")


''' ---   ALTERAÇÕES:
a. Calcule e mostre também a média de alturas do grupo.
Teste 4: 1.80, m, 1.60,  f, 0     Saída: Maior=1.80   Menor=1.60   Masc.= 1 Fem.= 1  Média = 1.7
b. Calcule e mostre também a porcentagem de homens.
Teste 5: 1.80, m, 1.60, f, 0 Saída: Maior=1.80 Menor=1.60  Masc.= 1 Fem.= 1 Média = 1.7 Porc. = 50
c. Digite a condição de saída (zero) de primeira e evite os erros do Python.
    Mostre somente esta mensagem:    "Não foi digitado nenhum dado."
d. Permita o usuário digitar letra maiúscula ou minúscula. Resolva de duas maneiras. 
--- DICAS ABAIXO:
soma = sum(l_altura)                                                    # a.
ct = len (l_altura)
media = soma/ct

ct_geral = ct_masc + ct_fem              # Depois do while                               # c.
if ct_geral != 0:                                                                                 
    print ("Maior altura no grupo: ", maior)
    print ("Menor altura no grupo: ", menor)
    print ("Quantidade de homens: ", ct_masc)
    print ("Quantidade de mulheres: ", ct_fem)
    . . .          # Todo o código depois do while
else:
    print("Não foi digitado nenhum dado.")
    #if (genero == "m" or genero == "M"):                              #  Solução 1     # d.
    if genero.lower() == "m":   # if (genero.lower() == "m"):  #  Solução 2
        ct_masc += 1                       # ct_masc = ct_masc + 1
    elif geneno == 'f' or genero == 'F':      # elif genero.lower() == 'f':
        ct_fem += 1                         # ct_fem = ct_fem + 1
    else:
        . . .
----------
- Teoria:
test = "AuLa"
print(test.lower())  # Todas as letras minúsculas.
test = "AuLa"
print(test.upper())  # Todas as letras maiúsculas.
test = "AuLa"         # test = "AULA"
print(test.capitalize())  # Primeira letra maiúscula e as outras letras minúsculas.
---
    #if (genero == "m" or "M"):                              #  ERRO. Solução 1     # e.
    #if (genero == "m" or genero == "M"):                              #  Solução 1     # e.
    if genero.lower() == "m":   # if (genero.lower() == "m"):  #  Solução 2
        ct_masc += 1                       # ct_masc = ct_masc + 1
    # elif genero == 'f' or 'F':                                     # ERRO
    elif genero == 'f' or genero == 'F':      # elif genero.lower() == 'f':
        ct_fem += 1                         # ct_fem = ct_fem + 1
    else:
        . . .
---
a. Se o usuário digitar qualquer tecla diferente de 'm' ou 'f' mostre a mensagem 
de erro: "Você digitou opção inválida.".

'''
