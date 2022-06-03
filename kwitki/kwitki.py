from calendar import month
import tkinter as tk # https://docs.python.org/3/library/tkinter # https://www.youtube.com/watch?v=TuLxsvK4svQ
from datetime import date
today = date.today().strftime("%d/%m/%Y")
w = tk.Tk()
w.geometry("520x500")
w.title("kwitki")
try:
    w.iconphoto(True, tk.PhotoImage(file='logo.png'))
except:
  print("404 image not found")
w.config(background="black")
kiedypodlac = ""

def oblicz():
    try:
        k = listbox.get(listbox.curselection())
    except:
        k = "kaktus"
    e = wpisz_F.get()
    
    if k == "kaktus": #2 tygodnie
        k=14
    elif k == "muchołówk": #3 dni
        k=3
    elif k == "areka": #2 tygodnie
        k=14
    elif k == "stewia": #4 dni
        k=4
    elif k == "storczyk": #1 tydzień
        k=7
    else: print("error wybur")
    
    #     00/00/0000
    day = int(e[0]+e[1])
    month = int(e[3]+e[4])
    year = int(e[6]+e[7]+e[8]+e[9])
    miesiace = [31, 29, 31, 30 ,31 ,30 ,31 ,31 ,30 ,31 ,30 , 31]
    
    day+=k
    if day>miesiace[month-1]:
        day -= miesiace[month-1]
        month+=1
        if month>12:
            year+=1
            day = 1
            month = 1

    kiedypodlac = str(day)+"/"+str(month)+"/"+str(year)+"  "
    txt_a = tk.Label(w,text="kolejne podlanie: "+kiedypodlac,font=("Comic Sans",20),fg="#00ff00",bg="black")
    txt_a.place(x=20,y=340)


txt = tk.Label(w,text="\nkwitki",font=("Comic Sans",20),fg="#00ff00",bg="black")
txt.pack()

txt_F = tk.Label(w,text="wybierz kwitka:",font=("Comic Sans",20),fg="#00ff00",bg="black")
txt_F.place(x=50,y=70)
listbox=tk.Listbox(w,
                  bg="#36393f",
                  font=("Comic Sans",20),
                  width=12,fg="#00ff00")
listbox.place(x=320,y=80)
listbox.insert(1,"kaktus")
listbox.insert(2,"muchołówk")
listbox.insert(3,"areka")
listbox.insert(4,"stewia")
listbox.insert(5,"storczyk")
listbox.config(height=listbox.size()) # print(listbox.get(listbox.curselection()))

txt_k = tk.Label(w,text="kiedy ostatnio\npodlałeś kwitki:",font=("Comic Sans",20),fg="#00ff00",bg="black")
txt_k.place(x=20,y=150)

wpisz_F = tk.Entry(w,bg="#36393f",font=("Comic Sans",20),fg="#00ff00")
wpisz_F.place(x=10,y=220)
wpisz_F.insert("0",today)


button = tk.Button(w, text="wylicz",command=oblicz,font=("Comic Sans",20))
button.place(x=350,y=260)

txt_a = tk.Label(w,text="kolejne podlanie: "+kiedypodlac,font=("Comic Sans",20),fg="#00ff00",bg="black")
txt_a.place(x=20,y=340)




w.mainloop() 

"""
    
    txt_F = tk.Label(w,text="wpisz farenhajty:",font=("Comic Sans",20),fg="#00ff00",bg="black")
txt_F.place(x=50,y=100)

wpisz_F = tk.Entry(w,font=("Comic Sans",20))
wpisz_F.place(x=50,y=150)

txt_C = tk.Label(w,text="wpisz celcjusze:",font=("Comic Sans",20),fg="#00ff00",bg="black")
txt_C.place(x=50,y=200)

wpisz_C = tk.Entry(w,font=("Comic Sans",20))
wpisz_C.place(x=50,y=250)

button = tk.Button(w, text="oblicz",font=("Comic Sans",20))
button.place(x=450,y=350)

"""