from tkinter import Tk, END, Frame, SUNKEN, BOTH, X, Text
from tkinter import (font, filedialog, Button, Label, IntVar,
                     Radiobutton)
import os
from PIL import ImageTk, Image
import sys
import platform

cwd = os.path.dirname(os.path.realpath(__file__))
systemName = platform.system()


class AlInvisibleCloak():
    def __init__(self, operation):
        root = Tk(className=" ALINVISIBLECLOAK ")
        root.geometry("500x250+1410+780")
        root.resizable(0, 0)
        iconPath = os.path.join(cwd+'\\UI\\icons',
                                'alinvisiblecloak.ico')
        if systemName == 'Darwin':
            iconPath = iconPath.replace('\\','/')
        root.iconbitmap(iconPath)
        root.overrideredirect(1)
        if operation.lower() == 'hide':
            if systemName == 'Darwin':
                opr = 'chflags hidden'
            elif systemName == 'Windows':
                opr = 'Attrib +h /s /d'
            response = "hidden"
            root.attributes('-alpha', 0.6)
        elif operation.lower() == 'unhide':
            if systemName == 'Darwin':
                opr = 'chflags nohidden'
            elif systemName == 'Windows':
                opr = 'Attrib -h -s /s /d'
            response = "unhidden"
            root.attributes('-alpha', 1)
        self.opr = opr

        def liftWindow():
            root.lift()
            root.after(1000, liftWindow)

        def callback(event):
            root.geometry("450x250+1460+800")

        def showScreen(event):
            root.deiconify()
            root.overrideredirect(1)

        def screenAppear(event):
            root.overrideredirect(1)

        def hideScreen():
            root.overrideredirect(0)
            root.iconify()

        def getFile():
            folderPathEntry.delete(1.0, END)
            filename = filedialog.askdirectory()
            folderPathEntry.insert(1.0, filename)

        def subFolderOperation(path, eopr):
            for root, _, files in os.walk(path):
                if '.git' not in root:
                    if root != path: 
                        os.system(f'{eopr} "{root}"')
                    for file in files:
                        os.system(f'{eopr} "{root}/{file}"')

        def folderOperation():
            text.delete(1.0, END)
            selection = var.get()
            path = folderPathEntry.get("1.0", END)
            path = path.replace('/', '\\')[:-1]
            if systemName == 'Darwin':
                path = path.replace('\\','/')
            opr = self.opr
            if selection == 1:
                os.system(f'{opr} "{path}"')
                if systemName == 'Windows':
                    path = path+'\\*'
                    os.system(f'{opr} "{path}"')
                elif systemName == 'Darwin':
                    subFolderOperation(path, opr)
                text.insert(1.0, "Folder and it's sub folders and files are " +
                            f"now {response}")
            elif selection == 2:
                os.system(f'{opr} "{path}"')
                if operation.lower() == 'hide':
                    if systemName == 'Windows':
                        path = path+'\\*'
                        os.system(f'Attrib -h -s /s /d "{path}"')
                    elif systemName == 'Darwin':
                        opr = 'chflags nohidden'
                        subFolderOperation(path, opr)
                elif operation.lower() == 'unhide':
                    if systemName == 'Windows':
                        path = path+'\\*'
                        os.system(f'Attrib +h /s /d "{path}"')
                    elif systemName == 'Darwin':
                        opr = 'chflags hidden'
                        subFolderOperation(path, opr)
                text.insert(1.0, f"Folder is now {response}")

        textHighlightFont = font.Font(family='OnePlus Sans Display', size=12)
        appHighlightFont = font.Font(family='OnePlus Sans Display', size=12,
                                     weight='bold')

        titleBar = Frame(root, bg='#141414', relief=SUNKEN, bd=0)
        icon = Image.open(iconPath)
        icon = icon.resize((30, 30), Image.ANTIALIAS)
        icon = ImageTk.PhotoImage(icon)
        iconLabel = Label(titleBar, image=icon)
        iconLabel.photo = icon
        iconLabel.config(bg='#141414')
        iconLabel.grid(row=0, column=0, sticky="nsew")
        titleLabel = Label(titleBar, text='ALINVISIBLECLOAK', fg='#909090',
                           bg='#141414', font=appHighlightFont)
        titleLabel.grid(row=0, column=1, sticky="nsew")
        closeButton = Button(titleBar, text="x", bg='#141414', fg="#909090",
                             borderwidth=0, command=root.destroy,
                             font=appHighlightFont)
        closeButton.grid(row=0, column=3, sticky="nsew")
        minimizeButton = Button(titleBar, text="-", bg='#141414', fg="#909090",
                                borderwidth=0, command=hideScreen,
                                font=appHighlightFont)
        minimizeButton.grid(row=0, column=2, sticky="nsew")
        titleBar.grid_columnconfigure(0, weight=1)
        titleBar.grid_columnconfigure(1, weight=50)
        titleBar.grid_columnconfigure(2, weight=1)
        titleBar.grid_columnconfigure(3, weight=1)
        titleBar.pack(fill=X)

        folderPath = Button(root, text="FOLDER PATH", borderwidth=0,
                            highlightthickness=3, command=getFile)
        folderPath.pack(fill=X)
        folderPath.config(font=appHighlightFont)
        folderPathEntry = Text(root, highlightthickness=3, bd=0,
                               font=appHighlightFont, height=1)
        folderPathEntry.pack(fill=BOTH, expand=True)
        ask = Label(root, text=f'DO YOU WANT TO {operation.upper()} ' +
                    'SUB FOLDERS AND FILES ALSO?')
        ask.pack(fill=X, pady=5)
        ask.config(font=appHighlightFont)

        confirm = Label(root)
        confirm.pack(fill=X)
        confirm.config(font=appHighlightFont)
        var = IntVar()
        radioYes = Radiobutton(confirm, text="Yes", variable=var, value=1,
                               command=folderOperation)
        radioYes.config(font=appHighlightFont)
        radioYes.grid(column=0, row=0, padx=70)

        radioNo = Radiobutton(confirm, text="No", variable=var, value=2,
                              command=folderOperation)
        radioNo.config(font=appHighlightFont)
        radioNo.grid(column=1, row=0, padx=70)

        text = Text(root, font="sans-serif",  relief=SUNKEN,
                    highlightthickness=5, bd=0)
        text.config(height=2, font=textHighlightFont)
        text.pack(fill=BOTH, expand=True)

        titleBar.bind("<B1-Motion>", callback)
        titleBar.bind("<Button-3>", showScreen)
        titleBar.bind("<Map>", screenAppear)

        if systemName == 'Windows':
            liftWindow()
        root.mainloop()


if __name__ == "__main__":
    AlInvisibleCloak(sys.argv[1])
