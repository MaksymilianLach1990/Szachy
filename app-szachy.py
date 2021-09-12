# Potrzebne moduły
import turtle
import time
import random
from models import *

# Podstawowe narzędzia i wytyczne
los = random.randint(0.0, 255.0)
t = time.time()
pen = turtle.Turtle()
pen.hideturtle()
pen.screen.screensize(800, 800)  # Rozmiar okna
pen.screen.bgcolor('white')  # Kolor tła
pen.speed(0)  # Prędkość rysowania

#  POZIOM - PUNKT STARTOWY
#  PION - PUNKT STARTOWY
stax = 0 - (700/2-140)
stay = 0 + (700/2+10)

#  SLOWNIKI
pole_kolor = dict()
pole_figora = dict()
pole_plansza = []
team_biale = {'color': 0}
team_czarne = {'color': 1}
figory = ['pionek', 'wierza', 'skoczek', 'goniec', 'krolowa', 'krol']
pen.hideturtle()