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
           media = ((n1 * 1) + (n2 * 1.5) + (n3 * 2)) / 4.5
           if media == 0:
               print("SR")
           elif media < 2:
               print("II")
           elif media < 5:
               print("MI")
           elif media < 7:
               print("MM")
           elif media < 9:
               print("MS")
           else:
               print("SS")