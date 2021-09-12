# Potrzebne moduły
import turtle
import time
import random
from models import *

# Podstawowe narzędzia i wytyczne
los = random.randint(0, 255)
t = time.time()
pen = turtle.Turtle()
pen.hideturtle()
pen.screen.screensize(800, 800)  # Rozmiar okna
pen.screen.bgcolor('white')  # Kolor tła
pen.speed(0)  # Prędkość rysowania

#  POZIOM - PUNKT STARTOWY
stax = 0 - (700/2-140)
#  PION - PUNKT STARTOWY
stay = 0 + (700/2+10)

#  SLOWNIKI
pole_kolor = dict()  # Słownik odpowiadający za określenie kolorów pól na planszy
pole_figora = dict()  # Słownik odpowiadający za określanie jaki pionek stoi na danym polu
pole_plansza = []  # Lista pól na planszy
team_biale = {'color': 0}  # Słownik zawierający pionki drużyny białej i ich pozycje
team_czarne = {'color': 1}  # Słownik zawierający pionki drużyny czarnej i ich pozycje
figory = ['pionek', 'wierza', 'skoczek', 'goniec', 'krolowa', 'krol']  # Lista dostępnych figór w grze
pen.hideturtle()


# Wypełnianie słowników odpowiednimi elementami, ustalenie odpowiednik kolorów dla konkretnych pól
def szachownica():
    liczba = 0
    c = 1
    for i in 'ABCDEFGH':
        for n in '12345678':
            if liczba == 8:
                liczba = 0
                if c == 1:
                    c -= 1
                elif c == 0:
                    c += 1
            if c == 1:
                pole_kolor[i + n] = 0
                pole_figora[i + n] = 0
                team_biale[i + n] = 0
                team_czarne[i + n] = 0
                pole_plansza.append(i+n)
                c -= 1
            elif c == 0:
                pole_kolor[i + n] = 1
                pole_figora[i + n] = 0
                team_biale[i + n] = 0
                team_czarne[i + n] = 0
                pole_plansza.append(i+n)
                c += 1
            liczba += 1


# Rysowanie planszy wraz z oznaczeniami na pionowej i poziomej lini
def plansza():
    
    wspolrzedne = list(pole_kolor.keys())
    for i in wspolrzedne[0: 2]:
        znajdz(i)
        pole(pole_kolor[i])





# Uruchomienie programu
if __name__ == '__main__':
    szachownica()
    plansza()
    pen.up()
    print(time.time() - t)
    turtle.done()