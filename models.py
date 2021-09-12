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


