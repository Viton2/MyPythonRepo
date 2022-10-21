num = int(input("Digite um número: "))

file = open("tabuada.txt", "w")

file.write(f"Tabuada do {num}: \n")

for c in range(0, 11):
    file.write(f"\n {num} X {c} = {num * c}")

file.close()
