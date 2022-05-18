from functools import partial
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import math, string

root = tk.Tk()
root.geometry("300x200")
root.resizable(False, False)

prizeDict = {"small" : 6.95, "medium" : 11.50, "large" : 15.50}
ammoutDict = {"small" : 0, "medium" : 0, "large" : 0}
question = 0

# updates label with progressbar percentage
def update_progress_label():
    return f"Current Progress: {pb['value']}%"


# updates program progressbar
def progress():
    if pb['value'] < 100:
        pb['value'] += 25
        value_label['text'] = update_progress_label()
    else:
        showinfo(message='The progress completed!')       


def buttonPressed():
    global question, quest_label, anwser_entry, prizeLabel, root
    sizeList = list(ammoutDict.keys())
    raiseError = False
    chars = False
    try:
        DictValue = int(anwser_entry.get())
        ammoutDict[sizeList[question]] = DictValue
    except ValueError as error:
        getAnwser = anwser_entry.get()
        if isFloat(getAnwser) == True:
            showinfo(title="Melding!", message="U kan alleen hele pizza's bestellen! Probeer het opnieuw!")
            raiseError = True
        else:
            if raiseError == False:
                if ',' in getAnwser:
                    showinfo(title="Melding!", message="U kan alleen hele pizza's bestellen! Probeer het opnieuw!")
                    raiseError = True
            if raiseError == False:
                alphaChars = list(string.ascii_lowercase)
                for char in getAnwser:
                    if char in alphaChars:
                        raiseError = True
                        chars = True
                        break
            if raiseError == False:
                specialSym = {'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', '&', '<', '`', '}', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/'}
                for char in getAnwser:
                    if char in specialSym:
                        raiseError = True
                        chars = True
                        break
            if raiseError == True:
                if chars == True:
                    showinfo(title="Error intercepted!", message="U kan geen letters/symbolen gebruiken! Probeer het opnieuw!")
    else:
        if raiseError == False:
            ammoutDict[sizeList[question]] = DictValue
    finally:
        if raiseError == False:
            question += 1
            progress()
            if question >= 3:
                totaalPrijs = 0
                for ammoutValue, prizeValue in zip(ammoutDict.values(), prizeDict.values()):
                    totaalPrijs += (float(ammoutValue) * prizeValue)
                quest_label.config(text="Uw totaal: " + str(totaalPrijs))
                showinfo(title="Melding!!!", message="Klik hier om het programma te beëindigen")
                root.destroy()
            else:
                textMessage = ("Hoeveel " + str(sizeList[question]) + " pizza's wilt u hebben?")
                quest_label.config(text=textMessage)
                prizeLabel.config(text="Prijs (" + str(sizeList[question]) + "): " + str(prizeDict[sizeList[question]]))


def isFloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


# the progressbar itself
pb = ttk.Progressbar(root, orient='horizontal', mode='determinate', length=280)
pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)

# shows percentage of progressbar
value_label = tk.Label(root, text=update_progress_label())
value_label.grid(column=0, row=1, columnspan=2)

# shows questions for pizza's
quest_label = tk.Label(root, font=("Helvetica", 12), bg="light gray", text=("Hoeveel small pizza's wilt u hebben?"))
quest_label.grid(column=0, row=2, columnspan=2)

# number entry 
anwser_entry = tk.Entry(root, justify="center")
anwser_entry.insert(0, int(0))
anwser_entry.grid(column=0, row=3, columnspan=2)

# comfirm button
anwser_button = tk.Button(root, text="Bevestig", width=7, command=buttonPressed)
anwser_button.grid(column=1, row=3, columnspan=2)

# show prize label
prizeLabel = tk.Label(root, font=("Helvetica", 12), bg="light gray", width=20, text=("Prijs (small): " + str(prizeDict["small"])))
prizeLabel.grid(column=0, row=4, columnspan=2)

# run program
progress()

root.mainloop()