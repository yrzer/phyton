from random import randrange # komentaż do random
import math
"""
komentaż
"""
MyGames = ["Gothic", "Tetris", "LoL", "Minecraft", "Stalker", "Asassin"]
MyFilms = ["Breaking Bad", "Wojny Klonów", "Wiedźmin", "Perfekcyjny Chaos", "Dark"]
print(MyGames)
print(MyFilms)
MyHobby = MyGames + MyFilms
print(MyHobby)

print("------------------")

txt = " Hello World "
x = txt.strip()
y = txt.replace("H", "J")
print(y+" "+x)

print("------------------")

for x in range(10):
    a = randrange(10)
    b = str(a)
    if (a%2)==0:
        print(b+" :parzysta liczba")
    else:
       print(b + " :nieparzysta liczba")

print("------------------")

a=int(input())
b=int(input())
c=int(input())

delta = lambda a, b, c:(b*b)-4*a*c
print(delta(a,b,c))
print(math.sqrt(delta(a,b,c)))

print("------------------")

for x in range(10):
    def silnia(n):
        if n <= 1:
            return 1
        else:
            return n * silnia(n - 1)

for x in range(10):
    r = randrange(10)
    wynik = silnia(r)
    print("Silnia z ", r, " jest równa ", wynik)

print("------------------")
