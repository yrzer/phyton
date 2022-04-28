import tkinter as tk # https://docs.python.org/3/library/ # https://www.youtube.com/watch?v=TuLxsvK4svQ


w = tk.Tk()
w.geometry("670x420")
w.title("kalkulator stopni")
w.iconphoto(True, tk.PhotoImage(file='logo.png'))
w.config(background="black")

def oblicz():
    odp_txt_F = 0
    odp_txt_C = 0
    
    # F -> C
    try:
        fahrenheit = int(wpisz_F.get())
        odp_txt_F = (fahrenheit - 32.0) * 5.0 / 9.0
    except:
        print("error or null in frarenhite input")
    else:
        txt_odp_F = tk.Label(w,text=odp_txt_F,font=("Comic Sans",20),fg="#00ff00",bg="black")
        txt_odp_F.place(x=400,y=140)
    # C -> F
    try:
        celsius = int(wpisz_C.get())
        odp_txt_C = (celsius * 9.0) / 5.0 + 32
    except:
        print("error or null in Celcjusz input")
    else:
        txt_odp_C = tk.Label(w,text=odp_txt_C,font=("Comic Sans",20),fg="#00ff00",bg="black")
        txt_odp_C.place(x=400,y=240)


txt = tk.Label(w,text="\nkalkulator z celcjusz na farenhajta i odwrotnie",font=("Comic Sans",20),fg="#00ff00",bg="black")
txt.pack()

txt_F = tk.Label(w,text="wpisz farenhajty:",font=("Comic Sans",20),fg="#00ff00",bg="black")
txt_F.place(x=50,y=100)

wpisz_F = tk.Entry(w,font=("Comic Sans",20))
wpisz_F.place(x=50,y=150)

txt_C = tk.Label(w,text="wpisz celcjusze:",font=("Comic Sans",20),fg="#00ff00",bg="black")
txt_C.place(x=50,y=200)

wpisz_C = tk.Entry(w,font=("Comic Sans",20))
wpisz_C.place(x=50,y=250)

button = tk.Button(w, text="oblicz",command=oblicz,font=("Comic Sans",20))
button.place(x=450,y=350)

w.mainloop() 