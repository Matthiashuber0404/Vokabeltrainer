from tkinter import *
from tkinter import ttk
from tkinter import Tk, Frame
import random

root = Tk()
root.title('Vokabeltrainer [V 0.1.1]')
root.configure(background="#C3B1E1")
root.geometry("800x400")
#root.attributes('-fullscreen', True)
#root.resizable(width=False, height=False)


# Column
root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=0)
root.columnconfigure(2, weight=0)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=8)
root.columnconfigure(5, weight=1)
# Column

# Row
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=0)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=5)
# Row

# Add a vertical line as a Frame widget
separator = Frame(root, background="black", width=1)
separator.grid(row=0, column=3, rowspan=6, sticky="ns")

style = ttk.Style()
style.configure("CustomSeparator.TSeparator", foreground="black", bordercolor="black")

ttk.Label(root, text="Pfad zur CSV-Datei angeben", background="#C3B1E1", foreground="#000000", font=('Arial', 15)).grid(column=0, row=1)
entryCSV = ttk.Entry(root,font=('Arial', 15))

translations = []

def read_entryCSV():
    try:
        eingabe = entryCSV.get()
        entryCSV.delete(0, END)
        with open(eingabe, "r", encoding='utf-8-sig') as file:
            file.readline()
            content = file.readlines()
        
        
        translations.clear()
        for line in content:
            english, german = line.strip().split(';')
            translation = [english.strip(), german.strip(), 0]
            translations.append(translation)

        # for translation in translations:
        #     print(translation)
        ttk.Label(root, text="  Datei ausgelesen  ", background="#C3B1E1", foreground="#000000", font=('Arial', 20)).grid(column=0, row=3)
        loesung.grid(column=4, row=1)
        randomWord()
        buttonConfirm.grid(column=5, row=2)
        input.grid(column=4, row=2, padx=10, pady=10)
        #  buttonOK.config(state='disabled')
    except FileNotFoundError:
        ttk.Label(root, text="Datei nicht gefunden", background="#C3B1E1", foreground="#FF0000", font=('Arial', 20)).grid(column=0, row=3)

akt=''

def randomWord():
    global akt
    randomWord = random.choice(translations)
    if randomWord[2] == 2:
        while randomWord[2] == 2:
            randomWord = random.choice(translations)
    akt = randomWord
    loesung.config(text=akt[1])


def equal():
    eingabe = input.get()
    if akt[0] == eingabe:
        ergebnis.config(text="Richtig!")
        for item in translations:
            if item[0] == eingabe and item[1] == akt[1] :
                item[2] -= -1
    
                
    else:
        ergebnis.config(text="Leider falsch! Richtig wäre gewesen: "+ akt[0])
        for item in translations:
            if item[0] == akt[0] and item[1] == akt[1] :
                item[2] += -1
    ergebnis.grid(column=4, row=3)
    root.after(2000, clear_ergebnis)
    input.delete(0, END)

def clear_ergebnis():
    ergebnis.config(text="")
    randomWord()
    
    
    
    
loesung = ttk.Label(root, text=akt, background="#C3B1E1", foreground="#000000", font=('Arial', 30))

entryCSV.grid(column=0, row=2)

buttonOK = ttk.Button(root, text="Datei auslesen", command=read_entryCSV, width=25)
buttonOK.grid(column=1, row=2, padx=5, pady=5)


buttonConfirm = ttk.Button(root, text="Abschicken", command=equal, width=30)
ergebnis = ttk.Label(root, text='', background="#C3B1E1", foreground="#000000", font=('Arial', 20))

input = ttk.Entry(root,font=('Arial', 25), width=50)


root.mainloop()
