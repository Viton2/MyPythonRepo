"""   CEUB   -   Bacharelado em Ciência da Computação (BCC)   -   Prof. Barbosa
Teclas de atalho: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha.

- Resolva com lista

- Desenvolva o programa que calcule a média aritmética de uma turma, onde
cada aluno realizou uma avaliação. Não sabemos a quantidade de alunos,
por isso usaremos o valor “ -1” como condição (flag) de saída. Na tela de saída,
mostre também a quantidade de alunos da turma. Sempre que tivermos uma divisão,
temos que verificar se o divisor é diferente de zero.

Teste 1:    notas: 5, 6 e -1      Saída: Média 5.5        Quantidade de alunos: 2
Teste 2:    notas: 5, 6, 7 e -1   Saída: Média 6          Quantidade de alunos: 3
Dica: media = soma / ct


"""
# - Solução com lista:
l_notas = []                            # Cria uma lista vazia
print('Digite [ -1 ] para sair')
while True:             # Laço de repetição while, repete enquanto condição verdadeira
    nota = float(input("Nota do aluno: "))    # Indentação é obritória
    if nota == -1:
        break                           # Sai de uma estrutura de repetição (while)
    l_notas.append(nota)                # Armazena um valor na lista
# Fim da estrutura de repetição de repetição "while"
qtd_alunos = len(l_notas)               # Quantidade de elementos na lista
soma_notas = sum(l_notas)               # Soma dos elementos na lista
media = soma_notas / qtd_alunos
print("Média da turma: ", media)
print('Quantidade de alunos: ', qtd_alunos)
print('Relação das notas:')
print(l_notas)                          # Solução 1, mostra os valores na horizontal
for nota in l_notas:                    # Solução 2, for nome_variavel in nome_lista:
    print(nota)
''' ----- ALTERAÇÕES:
a. Se digite -1 na primeira leitura ocorre o erro: "ZeroDivisionError: division by zero". 
    Resolva esse problema. 
    Teste 3:    notas: -1                 Saída: Não existe divisão por zero
b. Troque a mensagem estática da entrada de dados por uma mensagem dinâmica.
c. Mostre também a soma das notas dos alunos da turma.
d. Mostre a média da turma com duas casas decimais.
e. Mostre a média e a quantidade de alunos na mesma linha, nesta frase:
    A média da turma de X alunos é X.XX.          
'''