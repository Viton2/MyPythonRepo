from graphics import *

janela = GraphWin("Janela Teste", 500, 500)

ponto = Point(100, 100)
ponto.setFill("Blue")
ponto.draw(janela)

for coluna in range(10, 490):
    janela.plot(coluna, 200, "blue")
    time.sleep(0.01)

janela.getMouse()
janela.close()