import math
import os
import time

def lts(s): 
    return ' '.join([str(elem) for elem in s])
def stl(a):
    l =[]
    r = ""
    for x in range(len(a)):
        if a[x]==' ':
            l.append(int(r))
            r=""
        else:
            r+=a[x]
    l.append(int(r))
    return l

def toB(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m

def toS(a):
  l=[]
  m=""
  for i in a:
    b=0
    c=0
    k=int(math.log10(i))+1
    for j in range(k):
      b=((i%10)*(2**j))   
      i=i//10
      c=c+b
    l.append(c)
  for x in l:
    m+=chr(x)
  return m

def def1():
    f_r = open("txt.txt", "r")
    r = f_r.read()
    f_w = open("txt.txt", "w")
    f_w.write(lts(toB(r))) 

def def2():
    f_r = open("txt.txt", "r")
    r = f_r.read()
    f_w = open("txt.txt", "w")
    f_w.write(toS(stl(r))) 

def def6():
    def1()
    f_r = open("txt.txt", "r")
    r = f_r.read()
    r= stl(r) # tablica
    
    
    

def main():
    os.system('cls' if os.name=='nt' else 'clear')
    print(time.strftime("%d.%m.%Y - %I:%M:%S %p", time.localtime()))
    w=int(input("| 1:txt file to binary | 2:binary file to txt |\n| 3:txt to binary | 4:txt to binary |\n| 5:path // txt.txt| 6:cipher txt to txt |\n:"))
    if w==1 :
        def1()
    elif w==2 :
        def2()
    elif w==3 :
        w=input("txt:")
        print(toB(w))
    elif w==4 :
        w=input("0000000 0000000 0000000...\n:")
        print(toS(w))
    elif w==5 :
        print("5")
    elif w==6 :
        def6()
    else:
        print("error")
    
    main()
    
main()