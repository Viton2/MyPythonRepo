n1 = float(input("Primeira nota: "))
if n1 < 0 or n1 > 10:
   print("Valor inválido")
else:
   n2 = float(input("Segunda nota: "))
   if n2 < 0 or n2 > 10:
       print("Valor inválido")
   else:
       n3 = float(input("Terceira nota: "))
       if n3 < 0 or n3 > 10:
           print("Valor inválido")
       else:
           media = (n1 + n2 + n3) / 3
           print("Media:", "%.2f" % media)
           if media >= 7:
               print("Aprovado!")
           else:
               print("Reprovado")