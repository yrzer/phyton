import math
def kula():
    print("podaj promien")
    r=int(input())
    print( (4/3)*math.pi*(r*r*r))
def szescian():
    print("podaj bok")
    a=int(input())
    print( a*a*a)
def prostopadloscian():
    print("podaj bok a,b,c")
    a=int(input())
    b=int(input())
    c=int(input())
    print( a*b*c)

print("1:kula | 2:szescian | 3:prostopadloscian")
s = input()
match int(s):
    case 1:
        kula()
    case 2:
        szescian()
    case 3:
        prostopadloscian()
    case _:
        print("error")