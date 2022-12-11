import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("FACTURA DE PEDIDO")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GMessage_280=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_280["font"] = ft
        GMessage_280["fg"] = "#cc0000"
        GMessage_280["justify"] = "center"
        GMessage_280["text"] = "SUPERMARKET"
        GMessage_280.place(x=190,y=20,width=207,height=30)

        GLabel_309=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_309["font"] = ft
        GLabel_309["fg"] = "#333333"
        GLabel_309["justify"] = "center"
        GLabel_309["text"] = "FACTURA N°"
        GLabel_309.place(x=10,y=110,width=100,height=30)

        GLineEdit_65=tk.Entry(root)
        GLineEdit_65["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_65["font"] = ft
        GLineEdit_65["fg"] = "#333333"
        GLineEdit_65["justify"] = "center"
        GLineEdit_65["text"] = "Entry"
        GLineEdit_65.place(x=120,y=110,width=187,height=30)

        GLabel_952=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_952["font"] = ft
        GLabel_952["fg"] = "#333333"
        GLabel_952["justify"] = "center"
        GLabel_952["text"] = "TIPO FACTURA"
        GLabel_952.place(x=20,y=60,width=88,height=30)

        GLineEdit_551=tk.Entry(root)
        GLineEdit_551["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_551["font"] = ft
        GLineEdit_551["fg"] = "#333333"
        GLineEdit_551["justify"] = "center"
        GLineEdit_551["text"] = "Entry"
        GLineEdit_551.place(x=260,y=60,width=69,height=30)

        GLabel_114=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_114["font"] = ft
        GLabel_114["fg"] = "#333333"
        GLabel_114["justify"] = "center"
        GLabel_114["text"] = "FECHA"
        GLabel_114.place(x=20,y=160,width=70,height=25)

        GLabel_58=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_58["font"] = ft
        GLabel_58["fg"] = "#333333"
        GLabel_58["justify"] = "center"
        GLabel_58["text"] = "DETALLE"
        GLabel_58.place(x=20,y=210,width=70,height=25)

        GLineEdit_178=tk.Entry(root)
        GLineEdit_178["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_178["font"] = ft
        GLineEdit_178["fg"] = "#333333"
        GLineEdit_178["justify"] = "center"
        GLineEdit_178["text"] = "Entry"
        GLineEdit_178.place(x=120,y=160,width=187,height=30)

        GLineEdit_455=tk.Entry(root)
        GLineEdit_455["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_455["font"] = ft
        GLineEdit_455["fg"] = "#333333"
        GLineEdit_455["justify"] = "center"
        GLineEdit_455["text"] = "Entry"
        GLineEdit_455.place(x=120,y=210,width=187,height=30)

        GLabel_940=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_940["font"] = ft
        GLabel_940["fg"] = "#333333"
        GLabel_940["justify"] = "center"
        GLabel_940["text"] = "CANTIDAD"
        GLabel_940.place(x=20,y=260,width=70,height=25)

        GLineEdit_952=tk.Entry(root)
        GLineEdit_952["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_952["font"] = ft
        GLineEdit_952["fg"] = "#333333"
        GLineEdit_952["justify"] = "center"
        GLineEdit_952["text"] = "Entry"
        GLineEdit_952.place(x=120,y=260,width=150,height=30)

        GLabel_294=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_294["font"] = ft
        GLabel_294["fg"] = "#333333"
        GLabel_294["justify"] = "center"
        GLabel_294["text"] = "TOTAL"
        GLabel_294.place(x=20,y=310,width=70,height=25)

        GLineEdit_149=tk.Entry(root)
        GLineEdit_149["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_149["font"] = ft
        GLineEdit_149["fg"] = "#333333"
        GLineEdit_149["justify"] = "center"
        GLineEdit_149["text"] = "Entry"
        GLineEdit_149.place(x=120,y=310,width=152,height=35)

        GLabel_951=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_951["font"] = ft
        GLabel_951["fg"] = "#333333"
        GLabel_951["justify"] = "center"
        GLabel_951["text"] = "N° DE PEDIDO"
        GLabel_951.place(x=20,y=360,width=70,height=25)

        GLineEdit_993=tk.Entry(root)
        GLineEdit_993["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_993["font"] = ft
        GLineEdit_993["fg"] = "#333333"
        GLineEdit_993["justify"] = "center"
        GLineEdit_993["text"] = "Entry"
        GLineEdit_993.place(x=120,y=360,width=148,height=34)

        GButton_240=tk.Button(root)
        GButton_240["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_240["font"] = ft
        GButton_240["fg"] = "#cc0000"
        GButton_240["justify"] = "center"
        GButton_240["text"] = "ACEPTAR"
        GButton_240.place(x=390,y=430,width=80,height=38)
        GButton_240["command"] = self.GButton_240_command

        GButton_730=tk.Button(root)
        GButton_730["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_730["font"] = ft
        GButton_730["fg"] = "#cc0000"
        GButton_730["justify"] = "center"
        GButton_730["text"] = "CANCELAR"
        GButton_730.place(x=490,y=430,width=79,height=37)
        GButton_730["command"] = self.GButton_730_command

    def GButton_240_command(self):
        print("command")


    def GButton_730_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
