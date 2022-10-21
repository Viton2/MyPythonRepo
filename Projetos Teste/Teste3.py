frase = input("Informe a frase criptografada: ")
if (len(frase)==0):
   print ("Digite a frase!")
else:
   cesar=""
   for ind in range(0, len(frase)):
       codigo=ord(frase[ind])
       codigo-=2
       novoCaracter=chr(codigo)
       cesar+=novoCaracter

   print("A frase descriptografada é:", cesar)


