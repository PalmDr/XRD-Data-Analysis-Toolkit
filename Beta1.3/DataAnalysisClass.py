__author__ = 'j'

import os

from tkinter import *

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

from Builder import *
from TreeView import *
from ConvertCSV import *


class DataAnalysis():
    def __init__(self):
        self.root = Tk()
        self.sub_1, self.sub_2, self.sub_1_1, self.sub_1_2, self.sub_2_1, self.sub_2_2, self.sub_2_2_1 = buildFrame(self.root)
        self.treeview, self.entry = buildTree(self.sub_1_1, self.sub_1_2)
        self.selected = buildSelectedBox(self.sub_2_2_1)

        self.choosefilebutton = Button(master=self.sub_1_2, text='Choose Directory',
                                       command=self.choosefile)
        self.choosefilebutton.pack(side=RIGHT,anchor = 'e', fill='x')

        self.selectbutton = Button(master=self.sub_2_1, text='>>',command=self.selectitems)
        self.selectbutton.pack(fill=X)

        self.unselectbutton = Button(master=self.sub_2_1, text='<<', command=self.unselectitems)
        self.unselectbutton.pack(fill=X)

        self.plot = Button(master=self.sub_2_1, text='Plot', command=self.childWindow)
        self.plot.pack(fill=X)

        self.convert = Button(master=self.sub_2_1, text='Convert',command=self.SQ_Pilatus)
        self.convert.pack()
        self.root.mainloop()

    def choosefile(self):
        filepath = filedialog.askdirectory()
        if filepath:
            self.treeview.delete(*self.treeview.get_children())
            self.entry.insert(0,filepath)
            dfpath = os.path.abspath(filepath)
            node = self.treeview.insert('', 'end', text=dfpath,
                                        values=[dfpath, "directory"], open=True)
            fill_tree(self.treeview, node)

    def selectitems(self):
        temp = treeview.selection()
        for key in temp:
            if self.treeview.item(key)['values']:
                self.selected.insert(END, self.treeview.item(key)['values'][0])

    def unselectitems(self):
        temp = self.selected.curselection()
        temp2 = []
        for key in temp:
            temp2.insert(0, key)
        for key in temp2:
            self.selected.delete(key)

    def childWindow(self):
        win2 = Toplevel()
        message = "Plots"
        Label(win2, text=message).pack()
        temp = self.selected.curselection()
        temp2 = []
        for key in temp:
            temp2.append(self.selected.get(int(key)))

        allcsv = convertCSV(b, 10)

        f = Figure()
        a = f.add_subplot(111)
        for column in allcsv.columns:
            a.semilogy(allcsv.index, allcsv[column])
        a.set_xlabel('Q Value')
        a.set_ylabel('Intensity')

        canvas = FigureCanvasTkAgg(f, master=win2)
        canvas.show()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        toolbar = NavigationToolbar2TkAgg(canvas, win2)

    def SQ_Pilatus(self):
        return
