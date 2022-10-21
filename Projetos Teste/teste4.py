from graphics import *
import random

janela = GraphWin("Janela teste", 600, 600)

for posicao in range(0, 600, 4):
    ponto = Point(posicao, 300)
    ponto.setFill(color_rgb(0, 0, 0))
    ponto.draw(janela)

janela.getMouse()
janela.close()