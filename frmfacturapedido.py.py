import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("FACTURAS DE PEDIDOS")
        #setting window size
        width=371
        height=374
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_551=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_551["font"] = ft
        GLabel_551["fg"] = "#333333"
        GLabel_551["justify"] = "center"
        GLabel_551["text"] = " Factura N°"
        GLabel_551.place(x=0,y=20,width=79,height=30)

        GLabel_426=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_426["font"] = ft
        GLabel_426["fg"] = "#333333"
        GLabel_426["justify"] = "center"
        GLabel_426["text"] = "Fecha "
        GLabel_426.place(x=0,y=60,width=82,height=30)

        GLineEdit_965=tk.Entry(root)
        GLineEdit_965["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_965["font"] = ft
        GLineEdit_965["fg"] = "#333333"
        GLineEdit_965["justify"] = "center"
        GLineEdit_965["text"] = "Entry"
        GLineEdit_965.place(x=90,y=20,width=138,height=32)

        GLineEdit_487=tk.Entry(root)
        GLineEdit_487["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_487["font"] = ft
        GLineEdit_487["fg"] = "#333333"
        GLineEdit_487["justify"] = "center"
        GLineEdit_487["text"] = "Entry"
        GLineEdit_487.place(x=90,y=60,width=139,height=32)

        GLabel_8=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_8["font"] = ft
        GLabel_8["fg"] = "#333333"
        GLabel_8["justify"] = "center"
        GLabel_8["text"] = "Detalle"
        GLabel_8.place(x=10,y=110,width=62,height=30)

        GLineEdit_374=tk.Entry(root)
        GLineEdit_374["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_374["font"] = ft
        GLineEdit_374["fg"] = "#333333"
        GLineEdit_374["justify"] = "center"
        GLineEdit_374["text"] = "Entry"
        GLineEdit_374.place(x=90,y=110,width=212,height=32)

        GLabel_952=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_952["font"] = ft
        GLabel_952["fg"] = "#333333"
        GLabel_952["justify"] = "center"
        GLabel_952["text"] = "Cantidad"
        GLabel_952.place(x=0,y=160,width=70,height=25)

        GLabel_247=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_247["font"] = ft
        GLabel_247["fg"] = "#333333"
        GLabel_247["justify"] = "center"
        GLabel_247["text"] = "Total "
        GLabel_247.place(x=0,y=200,width=70,height=25)

        GLineEdit_934=tk.Entry(root)
        GLineEdit_934["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_934["font"] = ft
        GLineEdit_934["fg"] = "#333333"
        GLineEdit_934["justify"] = "center"
        GLineEdit_934["text"] = "Entry"
        GLineEdit_934.place(x=90,y=160,width=94,height=30)

        GLineEdit_426=tk.Entry(root)
        GLineEdit_426["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_426["font"] = ft
        GLineEdit_426["fg"] = "#333333"
        GLineEdit_426["justify"] = "center"
        GLineEdit_426["text"] = "Entry"
        GLineEdit_426.place(x=90,y=200,width=136,height=30)

        GButton_550=tk.Button(root)
        GButton_550["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_550["font"] = ft
        GButton_550["fg"] = "#000000"
        GButton_550["justify"] = "center"
        GButton_550["text"] = "Aceptar"
        GButton_550.place(x=190,y=320,width=72,height=30)
        GButton_550["command"] = self.GButton_550_command

        GButton_101=tk.Button(root)
        GButton_101["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_101["font"] = ft
        GButton_101["fg"] = "#000000"
        GButton_101["justify"] = "center"
        GButton_101["text"] = "Cancelar"
        GButton_101.place(x=280,y=320,width=69,height=30)
        GButton_101["command"] = self.GButton_101_command

        GLabel_83=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_83["font"] = ft
        GLabel_83["fg"] = "#333333"
        GLabel_83["justify"] = "center"
        GLabel_83["text"] = "Pedido N°"
        GLabel_83.place(x=0,y=250,width=70,height=25)

        GLineEdit_220=tk.Entry(root)
        GLineEdit_220["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_220["font"] = ft
        GLineEdit_220["fg"] = "#333333"
        GLineEdit_220["justify"] = "center"
        GLineEdit_220["text"] = "Entry"
        GLineEdit_220.place(x=90,y=250,width=134,height=30)

    def GButton_550_command(self):
        print("command")


    def GButton_101_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
