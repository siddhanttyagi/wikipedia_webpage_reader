ur = []
for i in range(0, 7):
    ur.append("0")
ur[0] = "https://en.wikipedia.org/wiki/Sachin_Tendulkar"
ur[1] = "https://species.wikimedia.org/wiki/Heliconia_angusta"
ur[2] = "https://en.wikipedia.org/wiki/India"
ur[3] = "https://species.wikimedia.org/wiki/Agama_sinaita"
ur[4] = "https://species.wikimedia.org/wiki/Phyllidia_varicosa"
ur[5] = "https://species.wikimedia.org/wiki/Aepyceros_melampus"
ur[6] = "https://en.wikipedia.org/wiki/Ancient_Aliens"
from tkinter import *
from tkinter.ttk import *
import random
import webbrowser

master = Tk()
master.geometry("400x400")
master.title("WIKIPEDIA WEBPAGE GENERATOR")


def openNewWindow():
    newWindow = Toplevel(master)
    newWindow.title("WIKIPEDIA WEBPAGE GENERATOR")

    newWindow.geometry("400x400")
    num = random.randint(0, 5)
    print(num)
    url = str(ur[num])
    newWindow.config(bg="black")

    def openweb():
        webbrowser.open(url)

    Btn = Button(newWindow, text=str(url[35:]) + " page", command=openweb)
    Btn.pack(padx=10, pady=19)

    btn2 = Button(newWindow, text="LOOK FOR ANOTHER ARTICLE", command=openNewWindow)
    btn2.pack(padx=10, pady=19)
    Btn3 = Button(newWindow, text="QUIT", command=newWindow.destroy)
    Btn3.pack(padx=10, pady=19)


label = Label(master, text="Wikipedia  Webpage Generator")

label.pack(pady=20, padx=20)
btn = Button(master, text="START", command=openNewWindow)
btn.pack(pady=10)
master.config(bg="black")
mainloop()