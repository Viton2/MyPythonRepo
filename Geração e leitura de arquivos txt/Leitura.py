def ler():
   arqTxt = open('c:\\temp\\teste.txt', 'r')
   print ('Lista de nomes do arquivo:')
   for nome in arqTxt:
       print (nome, end='')
   arqTxt.close()
   print('Fim de leitura do arquivo')

ler()
