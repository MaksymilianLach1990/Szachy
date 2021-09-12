# Potrzebne moduły
import turtle
import time
from models import *

# Podstawowe narzędzia i wytyczne
t = time.time()
pen = turtle.Turtle()
pen.screen.screensize(800, 800)  # Rozmiar okna
pen.screen.bgcolor('white')  # Kolor tła
pen.speed(0)  # Prędkość rysowania
pen.hideturtle()

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
    pion()
    poziom()
    wspolrzedne = list(pole_kolor.keys())
    for i in wspolrzedne[0: 2]:
        znajdz(i)
        pole(pole_kolor[i])


# Umieszczenie pionków na planszy, uzupełnienie odpowiednich słowników
def teams():
    czarne = (pole_plansza[0:16])
    biale = (pole_plansza[-8:] + pole_plansza[-16:-8])
    for color in range(0, 2):
        kolor(color)
        if color == 0:
            team = biale
            x = team_biale
        else:
            team = czarne
            x = team_czarne

        for i in team[8:16]:
            znajdz(i)
            pionek(color)
            pole_figora[i] = figory[0]
            x[i] = pole_figora[i]
        for i in team[0: 8: 7]:
            znajdz(i)
            wierza(color)
            pole_figora[i] = figory[1]
            x[i] = pole_figora[i]
        for i in team[1: 7: 5]:
            znajdz(i)
            goniec(color)
            pole_figora[i] = figory[3]
            x[i] = pole_figora[i]
        for i in team[2: 6: 3]:
            znajdz(i)
            skoczek(color)
            pole_figora[i] = figory[2]
            x[i] = pole_figora[i]
        znajdz(team[4])
        krol(color)
        pole_figora[team[4]] = figory[5]
        x[team[4]] = pole_figora[team[4]]
        znajdz(team[3])
        krolowa(color)
        pole_figora[team[3]] = figory[4]
        x[team[3]] = pole_figora[team[3]]
        print("Team {} na planszy".format(color))


# Sprawdzenie z jaką figurę postawić
def jaka_figora(figora, col):
    if figora == figory[0]:
        pionek(col)
    elif figora == figory[1]:
        wierza(col)
    elif figora == figory[2]:
        skoczek(col)
    elif figora == figory[3]:
        goniec(col)
    elif figora == figory[4]:
        krolowa(col)
    elif figora == figory[5]:
        krol(col)


# Przemieszczenie wybranego pionka na planszy, wykonanie ruchu
def ruch(pole_1, pole_2, strona):
    # Usuwanie pionka z pola 1 
    znajdz(pole_1)
    pole(pole_kolor[pole_1])
    # Sprawdzenie pola 2 i usuniecie przeciwnika 
    znajdz(pole_2)
    if pole_figora[pole_2] != 0:
        pole(pole_kolor[pole_2])
        jaka_figora(pole_figora[pole_1], strona)
    else:
        jaka_figora(pole_figora[pole_1], strona)
    # Update slownikow 
    if strona == 0:
        team_biale[pole_2] = pole_figora[pole_1]
        team_biale[pole_1] = 0
    elif strona == 1:
        team_czarne[pole_2] = pole_figora[pole_1]
        team_czarne[pole_1] = 0
    pole_figora[pole_2] = pole_figora[pole_1]
    pole_figora[pole_1] = 0


# Pobranie od gracza informacji do wykonania ruchu, pole startowe, pole docelowe i sprawdzenie czy ruch jest prawidłowy
def info_from_player(strona, runda, team):
    while True:
        # Sprawdzenie poprawności podanej informacji 
        pole_start = (pen.screen.textinput("Runda {} - {}".format(runda, team), "Podaj z którego pola")).upper()  # Pole startowe
        pole_end =  (pen.screen.textinput("Runda {} - {}".format(runda, team), "Podaj na jakie pole")).upper()  # Pole docelowe
        if pole_start and pole_end in pole_plansza:
            if strona == 0 and pole_figora[pole_start] == team_biale[pole_start]:
                ruch(pole_start, pole_end, strona=0)
                break
            elif strona == 1 and pole_figora[pole_start] == team_czarne[pole_start]:
                ruch(pole_start, pole_end, strona=1)
                break
        else:
            error_message()
            continue
        
        
    

# Uruchomienie programu
if __name__ == '__main__':
    szachownica()
    plansza()
    teams()
    print(time.time() - t)
    runda = 0
    while True:
        runda += 1
        if runda % 2 == 0:
            druzyna = 1
            team = "Czarne"
        elif runda % 2 != 0:
            druzyna = 0
            team = "Białe"
        info_from_player(druzyna, runda, team)
    

turtle.done()