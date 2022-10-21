flag = True
while flag:
    entrada = input("Digite uma frase: ")
    if len(entrada) < 3:
        print("Insira uma entrada com pelo menos 3 caracteres!")
    else:
        print("Entrada válida!\n" + entrada)
        flag = False

