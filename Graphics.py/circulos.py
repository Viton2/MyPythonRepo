from graphics import *
import random

janela = GraphWin("janela Teste", 600, 600)

fundo = Rectangle(Point(0, 0), Point(600, 600))
fundo.setFill('blue')
fundo.setOutline('black')
fundo.draw(janela)

circulo = Circle(Point(299, 299), 200)
circulo.setOutline("black")
circulo.setFill("red")
circulo.draw(janela)

outroCirculo = Circle(Point(299, 299), 150)
outroCirculo.setFill("white")
outroCirculo.setOutline("Black")
outroCirculo.draw(janela)

terceiro = Circle(Point(299, 299), 100)
terceiro.setOutline('black')
terceiro.setFill('red')
terceiro.draw(janela)

quarto = Circle(Point(299, 299), 50)
quarto.setOutline('black')
quarto.setFill('white')
quarto.draw(janela)

quinto = Circle(Point(299, 299), 15)
quinto.setOutline('black')
quinto.setFill('red')
quinto.draw(janela)

janela.getMouse()
janela.close()
