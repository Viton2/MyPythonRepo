ni = int(input("Qual o valor inicial?: "))
if ni < 0:
   print("Insira um valor positivo!")
else:
   nf = int(input("Qual o valor final?: "))
   if nf < 0 or nf < ni:
       print("Insira um valor positivo e maior que o numero inicial!")
   else:
       p = int(input("Qual o valor do passo?: "))
       if p < 0:
           print("Insira um valor positivo!")
       else:
           for var in range(ni, nf + 1, p):
               print(var)

