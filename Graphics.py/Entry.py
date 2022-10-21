from graphics import *
import random
import time

janela = GraphWin("Janela Teste", 600, 600)

L1 = Line(Point(0, 200), Point(600, 200))
L1.setFill('black')
L1.setWidth(4)
L1.draw(janela)
L2 = Line(Point(0, 400), Point(600, 400))
L2.setFill('black')
L2.setWidth(4)
L2.draw(janela)

o = Oval(Point(175, 50), Point(425, 150))
o.setFill("pink")
o.setOutline('red')
o.setWidth(2)
o.draw(janela)

t = Text(Point(120, 265), 'Qual é o seu nome:')
t.setOutline('black')
t.setSize(18)
t.draw(janela)

inp = Entry(Point(375, 265), 30)
inp.setSize(13)
inp.draw(janela)

tecla = ''
while tecla != 'Escape':
   tecla = janela.getMouse()
   print(tecla)


janela.getMouse()
janela.close()