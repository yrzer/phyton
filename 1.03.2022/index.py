from random import randrange # komentaż do random
f_w = open("1.03.2022/XD.txt", "w")
f_r = open("1.03.2022/txt.txt", "r")
r = f_r.read()
print(r)
print("---------------------------------------")
for x in range(10):
    f_w.write("XD ")
print("---------------------------------------")
print(len(r))
print("---------------------------------------")
a = ["Lorem"," ipsum"," dolor"," sit"," amet"," consectetur"," adipiscing"," elit"," Sed"," non"," felis"," sit"," amet"," orci"," varius"," tristique"," sit"," amet"," pulvinar"," mi"]
f_w.write(a[randrange(3)])