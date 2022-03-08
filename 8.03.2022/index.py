def kula()

def szescian()

def prostopadloscian()

print("1:kula | 2:szescian | 3:prostopadloscian")
s = input()

match int(s):
    case 1:
        print("OK")
    case 2:
        print("Not Found")
    case 3:
        print("I'm a teapot")
    case _:
        print("Code not found")