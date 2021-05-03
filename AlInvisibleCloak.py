from tkinter import *
from tkinter import font
import os
import pyttsx3
import sys

cwd = os.path.dirname(os.path.realpath(__file__))

class AlInvisibleCloak():
    def __init__(self, operation):
        root = Tk(className = " ALINVISIBLECLOAK ")
        root.geometry("450x200+1460+815")
        root.resizable(0,0)
        root.iconbitmap(os.path.join(cwd+'\\UI\\icons', 'alinvisiblecloak.ico'))
        if operation.lower() == 'hide':
            opr = 'Attrib +h /s /d'
            response = "hidden"
            root.attributes('-alpha',0.6)
        elif operation.lower() == 'unhide':
            opr = 'Attrib -h -s /s /d'
            response = "unhidden"
            root.attributes('-alpha',1)

        def speak(audio):
            engine = pyttsx3.init('sapi5')
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)
            engine.say(audio)
            engine.runAndWait()

        def folderOperation():
            text.delete(1.0, END)
            selection = var.get()
            path = folderPath.get()
            if selection == 1:
                os.system(f'{opr} "{path}"')
                path = path+'\*'
                os.system(f'{opr} "{path}"')
                text.insert(1.0, f"Folder and it's sub folders and files are now {response}")
                speak(f"Folder and it's sub folders and files are now {response}")
            elif selection == 2:
                os.system(f'{opr} "{path}"')
                text.insert(1.0, f"Folder is now {response}")
                speak(f"Folder is now {response}")

        appHighlightFont = font.Font(family='sans-serif', size=12, weight='bold')
        textHighlightFont = font.Font(family='Segoe UI', size=12, weight='bold')

        folderPath = Label(root, text = "FOLDER PATH")
        folderPath.pack()
        folderPath.config(font=textHighlightFont)
        folderPath= Entry(root, highlightthickness=3, bd=0,font=appHighlightFont)
        folderPath.pack(fill=X)

        ask = Label(root, text = f'DO YOU WANT TO {operation.upper()} SUB FOLDERS AND FILES ALSO?')
        ask.pack(fill=X,pady=5)
        ask.config(font=textHighlightFont)

        confirm = Label(root)
        confirm.pack(fill=X)
        confirm.config(font=textHighlightFont)
        var = IntVar()
        radioYes = Radiobutton(confirm, text="Yes", variable=var, value=1, command=folderOperation)
        radioYes.config(font=textHighlightFont)
        radioYes.grid(column=0,row=0,padx=70)

        radioNo = Radiobutton(confirm, text="No", variable=var, value=2, command=folderOperation)
        radioNo.config(font=textHighlightFont)
        radioNo.grid(column =1,row=0,padx=70)
        
        text = Text(root, font="sans-serif",  relief=SUNKEN , highlightthickness=5, bd=0)
        text.config(height=2, font=appHighlightFont)
        text.pack(fill=BOTH, expand=True)
        
        root.mainloop()

if __name__ == "__main__":
    AlInvisibleCloak(sys.argv[1]) 