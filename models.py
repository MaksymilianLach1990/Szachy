# Potrzebne moduły
import turtle
import random

# Nazwy dla funkcji
los = random.randint(0, 255)
pen = turtle.Turtle()
#  POZIOM - PUNKT STARTOWY
stax = 0 - (700/2-140)
#  PION - PUNKT STARTOWY
stay = 0 + (700/2+10)


# Funkcje odpowiadające za wygląd graficzny


# PLANSZA
# Nadawanie konkretnego koloru polom na planszy i pionką
def kolor(color):
    pen.color('black')
    if color == 1:
        pen.fillcolor('black')
    elif color == 0:
        pen.fillcolor('white')


# Tworzenie pojedynczego pola. Główny element planszy
def pole(col):
    pen.seth(0)
    pen.down()
    pen.color('black')
    if col == 1:
        pen.fillcolor('grey')
    elif col == 0:
        pen.fillcolor('white')
    pen.begin_fill()
    for x in range(4):
        pen.forward(80)
        pen.right(90)
    pen.end_fill()
    pen.up()


# Ustalanie pozyscji od której zacząć rysować
def znajdz(pole_1):
    pion = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'
    poziom = '1', '2', '3', '4', '5', '6', '7', '8'
    wartosc = 0
    x = 0
    y = 0
    for w in pole_1:
        if w in pion:
            for i in pion:
                if w == i:
                    y = stay - (wartosc * 80)
                else:
                    wartosc += 1
        elif w in poziom:
            n = int(w) - 1
            x = stax + (n * 80)
    pen.up()
    pen.goto(x, y)


# Rysowanie oznaczeń pionowych, zakres liter od A do H
def pion():
    x = stax - 20
    y = stay - 40
    pen.up()
    pen.goto(x, y)
    for i in 'ABCDEFGH':
        pen.write(str(i))
        y -= 80
        pen.goto(x, y)
    x = stax + 660
    y = stay - 40
    pen.up()
    pen.goto(x, y)
    for i in 'ABCDEFGH':
        pen.write(str(i))
        y -= 80
        pen.goto(x, y)


# Rysowanie oznaczeń poziomych, zakres liczb od 1 do 8
def poziom():
    x = stax + 40
    y = stay + 10
    pen.up()
    pen.goto(x, y)
    for i in '12345678':
        pen.write(str(i))
        x += 80
        pen.goto(x, y)
    x = stax + 40
    y = stay - 670
    pen.up()
    pen.goto(x, y)
    for i in '12345678':
        pen.write(str(i))
        x += 80
        pen.goto(x, y)


# FIGÓRY
# Pionek
def pionek(color):
    punkt = pen.pos()
    pen.goto(x=punkt[0] + 40, y=punkt[1] - 60)
    pen.down()
    pen.begin_fill()
    kolor(color)
    pen.seth(0)
    pen.circle(20)
    pen.end_fill()
    pen.up()


# Wierza
def wierza(color):
    punkt = pen.pos()
    pen.begin_fill()
    kolor(color)
    pen.seth(0)
    pen.goto(x=punkt[0] + 20, y=punkt[1] - 10)
    pen.down()
    for p in range(2):
        pen.forward(40)
        pen.right(90)
        pen.forward(60)
        pen.right(90)
    pen.end_fill()
    pen.up()


# Goniec
def goniec(color):
    punkt = pen.pos()
    pen.seth(180)
    pen.begin_fill()
    kolor(color)
    pen.goto(x=punkt[0] + 70, y=punkt[1] - 70)
    pen.down()
    for g in range(3):
        pen.forward(60)
        pen.right(120)
    pen.end_fill()
    pen.up()


# Skoczek
def skoczek(color):
    punkt = pen.pos()
    kolor(color)
    pen.seth(180)
    pen.begin_fill()
    pen.goto(x=punkt[0] + 60, y=punkt[1] - 70)
    pen.down()
    pen.forward(40)
    pen.right(120)
    pen.forward(40)
    pen.right(60)
    pen.left(90)
    for q in range(3):
        pen.forward(20)
        pen.left(120)
    pen.seth(60)
    pen.right(120)
    pen.forward(40)
    pen.end_fill()
    pen.up()


# Królowa
def krolowa(color):
    punkt = pen.pos()
    pen.seth(0)
    kolor(color)
    pen.begin_fill()
    pen.goto(x=punkt[0] + 25, y=punkt[1] - 75)
    pen.down()
    pen.forward(30)
    pen.left(90)
    pen.forward(50)
    pen.right(110)
    pen.circle(10)
    pen.seth(180)
    pen.forward(30)
    pen.right(160)
    pen.circle(10)
    pen.seth(-90)
    pen.forward(50)
    pen.end_fill()
    pen.up()


# Król
def krol(color):
    punkt = pen.pos()
    pen.seth(0)
    pen.begin_fill()
    kolor(color)
    pen.goto(x=punkt[0] + 25, y=punkt[1] - 70)
    pen.down()
    pen.forward(30)
    pen.left(90)
    pen.forward(50)
    pen.right(90)
    pen.forward(5)
    pen.left(90)
    pen.forward(10)
    pen.left(90)
    pen.forward(10)
    pen.left(90)
    pen.forward(10)
    pen.right(90)
    pen.forward(20)
    pen.right(90)
    pen.forward(10)
    pen.left(90)
    pen.forward(10)
    pen.left(90)
    pen.forward(10)
    pen.left(90)
    pen.forward(5)
    pen.right(90)
    pen.forward(50)
    pen.end_fill()
    pen.up()

