import re

# Definindo os tokens
tokens = [
    (r'\d+\.\d+', 'FLOAT'),    # Número com ponto flutuante
    (r'\d+', 'NUM'),           # Número inteiro
    (r'\+', 'ADD'),            # Operador de adição
    (r'-', 'SUB'),             # Operador de subtração
    (r'\*', 'MUL'),            # Operador de multiplicação
    (r'/', 'DIV'),             # Operador de divisão
    (r'\(', 'LPAR'),           # Parêntese esquerdo
    (r'\)', 'RPAR'),           # Parêntese direito
    (r'\s+', None),            # Espaços em branco (ignorados)
]


# Função para analisar a expressão em tokens
def lex(expression):
    pos = 0
    tokens_list = []

    while pos < len(expression):
        match = None
        for token in tokens:
            pattern, tag = token
            regex = re.compile(pattern)
            match = regex.match(expression, pos)
            if match:
                value = match.group(0)
                if tag:
                    tokens_list.append((value, tag))
                break
        if not match:
            print("Erro: Caractere inválido encontrado na posição", pos)
            return None
        else:
            pos = match.end(0)

    return tokens_list


# Teste
# expression1 = "3.5 + 4 * 10 - (7.2 / 2)"
expression1 = str(input("Digite a expressao: "))
tokens_list1 = lex(expression1)
for token, tag in tokens_list1:
    print(f'{token} => {tag}')
