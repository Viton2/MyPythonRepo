frase = input('Digite algo: ')
tam = len(frase)
ind = 0
while ind < tam:
    if (tam - 1) == ind:
        print(frase[ind], end='')
    else:
        print(frase[ind], end='+')
    ind += 1
