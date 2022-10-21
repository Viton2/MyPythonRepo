from graphics import *
import random

janela = GraphWin("Janela teste", 600, 600)

linha = Line(Point(10, 100), Point(590, 100))
linha.setFill("Black")
linha.setArrow("first")
linha.draw(janela)

janela.getMouse()
janela.close()
