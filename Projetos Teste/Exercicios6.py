frase = input("Digite uma palavra: ")

frase2 = ""

for var in range(0, int(len(frase)/2)):
    frase2 += frase[len(frase) - 1 - var]
    frase2 += frase[var]

if len(frase) % 2 != 0:
    frase2 += frase[int(len(frase)/2)]

print(frase2)