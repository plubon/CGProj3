import Tkinter as Tk
import tkFileDialog
from PIL import ImageTk
from Drawer import Drawer


WIDTH = 800
HEIGHT = 800


class MainWindow(Tk.Tk):

    def __init__(self):
        Tk.Tk.__init__(self)
        self.toppanel = None
        self.botpanel = None
        self.canvas = None
        self.filter = None
        self.combobox = None
        self.img = None
        self.startX = None
        self.startY = None
        self.drawer = None
        self.initialize()

    def initialize(self):
        self.title = "CGP2"
        self.toppanel = Tk.Frame(self)
        self.toppanel.pack(side=Tk.TOP)
        self.botpanel = Tk.Frame(self)
        self.botpanel.pack()
        self.canvas = Tk.Canvas(self.botpanel, width=WIDTH, height=HEIGHT, bg='white')
        self.img = Tk.PhotoImage(width=WIDTH, height=HEIGHT)
        self.canvas.create_image((0, 0), image=self.img, anchor="nw")
        self.canvas.bind('<ButtonPress-1>', self.onStart)
        self.canvas.bind('<ButtonRelease-1>', self.onEnd)
        self.canvas.pack(fill=Tk.BOTH, expand=1)
        combooptions = ["Symmetric bresenham", "Midpoint circle algorithm", "Xiaolin Wu Line", "Xiaolin Wu Circle"]
        self.filter = Tk.StringVar(self)
        self.filter.set(combooptions[0])
        self.combobox = apply(Tk.OptionMenu, (self.toppanel, self.filter)+tuple(combooptions))
        self.combobox.pack(side=Tk.LEFT)
        self.drawer = Drawer(self.img)
        self.mainloop()

    def onStart(self, event):
        self.startX = event.x
        self.startY = event.y

    def onEnd(self, event):
        if(self.filter.get() == "Symmetric bresenham"):
            self.drawer.drawsymbresenham(self.startX, self.startY, event.x, event.y)
        elif (self.filter.get() == "Midpoint circle algorithm"):
            self.drawer.circle(self.startX, self.startY, event.x, event.y)
        elif (self.filter.get() == "Xiaolin Wu Line"):
            self.drawer.xaolinwuline(self.startX, self.startY, event.x, event.y)
        elif (self.filter.get() == "Xiaolin Wu Circle"):
            self.drawer.xaolinwuciricle(self.startX, self.startY, event.x, event.y)

if __name__ == "__main__":
    mw = MainWindow()