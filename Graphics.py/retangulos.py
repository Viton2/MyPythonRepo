from graphics import *
import random

janela = GraphWin("janela Teste", 600, 600)

retangulo = Rectangle(Point(10, 10), Point(590, 100))
retangulo.setFill("green")
retangulo.setOutline("black")
retangulo.draw(janela)

outroRetangulo = Rectangle(Point(500, 110), Point(590, 590))
outroRetangulo.setFill("yellow")
outroRetangulo.setOutline("black")
outroRetangulo.draw(janela)

terceiro = Rectangle(Point(10, 110), Point(490, 590))
terceiro.setFill("red")
terceiro.setOutline("black")
terceiro.draw(janela)

janela.getMouse()
janela.close()