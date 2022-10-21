from graphics import *
import random

janela = GraphWin("Janela teste", 600, 600)

#Diagonal principal:
for posicao in range(0, 599):
    ponto = Point(posicao, posicao)
    ponto.setFill(color_rgb(0, 0, 0))
    ponto.draw(janela)
#Diagonal secundaria:
    ponto = Point(599 - posicao, posicao)
    ponto.setFill(color_rgb(0, 0, 0))
    ponto.draw(janela)

    ponto = Point(posicao, 0)
    ponto.setFill(color_rgb(0, 0, 0))
    ponto.draw(janela)

    ponto = Point(599, posicao)
    ponto.setFill(color_rgb(0, 0, 0))
    ponto.draw(janela)

    ponto = Point(posicao, 599)
    ponto.setFill(color_rgb(0, 0, 0))
    ponto.draw(janela)

    ponto = Point(0, posicao)
    ponto.setFill(color_rgb(0, 0, 0))
    ponto.draw(janela)


janela.getMouse()
janela.close()