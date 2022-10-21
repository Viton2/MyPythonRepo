"""   CEUB   -   Bacharelado em Ciência da Computação (BCC)   -   Prof. Barbosa
Teclas de atalho: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha.

Obs.: resolva sem lista

- Uma agência de publicidade quer prestar seus serviços somente para a maior companhia,
considerando a quantidade de funcionários. Para tal, consegue um conjunto de dados
com o CNPJ (Cadastro Nacional de Pessoa Jurídica) e a quantidade de funcionários
de várias empresas. Construa o programa que leia esses dados de entrada e mostre
o CNPJ e a quantidade de funcionários da maior empresa, ou seja, da empresa com
maior recursos humanos.

Teste 1: Entrada: 11, 15;  12, 20;  13, 10;  <enter>     Saída: Maior empresa: 12, qtd 20
Teste 2: Entrada: <enter>                                Saída: Maior empresa: '', qtd 0
"""

maior_qtd = 0                               # Valores iniciais
maior_cnpj = ""
print('Digite <enter> para sair')
while True:
    # Recebe os dados de entrada
    cnpj = input("CNPJ: ")                  # cnpj = str(input("CNPJ: "))
    if cnpj == '':
        break
    qtd = int(input("Quantidade de funcionários: "))
    if qtd > maior_qtd:
        maior_qtd = qtd                     # Atualizando os dados da maior empresa
        maior_cnpj = cnpj
# Fim do while
print(f"A empresa {maior_cnpj} tem o maior número de funcionários com um total de {maior_qtd}.")


''' ----- ALTERAÇÕES:
a. Digite a condição de saída de primeira e mostre a mensagem: "Nenhum dado foi fornecido."
b. Quantas empresas foram processadas?
c. Mostre também o CNPJ e a quantidade de funcionários da menor empresa.
    ----- DICAS:
# se maior_qtd != -1 então pelo menos uma empresa foi recebida. Ela é mostrada com o print   # a.
if maior_qtd != -1:
    # print("A empresa " + maior_cnpj + " tem o maior número de funcionários\ncom  ", maior_qtd)
    # print("A empresa ", maior_cnpj, " possui o maior número de funcionários\ncom ", maior_qtd)
    print(f"A empresa {maior_cnpj} possui o maior número de funcionários\ncom {maior_qtd}")
else:           # caso contrário
    print("Nenhum dado foi fornecido.")
ct = 0                                      # Antes do while                                 # b.
    ct += 1                                 # Dentro do while
print('Quantidade de empresas:', ct)        # Depois do while
menor_qtd = 999999                          # Antes do while                                 # c.
menor_cnpj = ''
    ...
    if qtd <  menor_qtd:                    # Dentro do while
        menor_qtd = qtd
        menor_cnpj = cnpj
...                                         # Depois do while
print(f"A empresa {menor_cnpj} tem o menor número de funcionários com um total de {menor_qtd}")
'''
