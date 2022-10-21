from graphics import *
import random

janela = GraphWin("Janela Teste", 600, 600)

for i in range(12000):
    coluna = random.randrange(0, 600)
    linha = random.randrange(0, 600)
    ponto = Point(coluna, linha)
    ponto.setFill("Red")
    ponto.draw(janela)

janela.getMouse()
janela.close()