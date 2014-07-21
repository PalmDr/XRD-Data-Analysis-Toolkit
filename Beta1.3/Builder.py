__author__ = 'j'

from tkinter import ttk
from tkinter import *
from TreeView import *

def buildFrame(root):
    sub_1 = Frame(root)
    sub_1.pack(side=LEFT,anchor = 'w', fill='both', expand=True)

    sub_1_1 = Frame(sub_1)
    sub_1_1.pack(side=TOP, anchor='n',fill='both',expand=True)

    sub_1_2 = Frame(sub_1)
    sub_1_2.pack(side=BOTTOM,anchor = 's',expand=False,fill='x')

    sub_2 = Frame(root)
    sub_2.pack(side=RIGHT, anchor='w', fill='both', expand=True)

    sub_2_1 = Frame(sub_2)
    sub_2_1.pack(side=LEFT, anchor='w',expand=False)

    sub_2_2 = Frame(sub_2)
    sub_2_2.pack(side=RIGHT,anchor='e',fill='both',expand=True)

    sub_2_2_1 = Frame(sub_2_2)
    sub_2_2_1.pack(side=TOP,anchor='e',fill='both',expand=True)

    return sub_1, sub_2, sub_1_1, sub_1_2, sub_2_1, sub_2_2, sub_2_2_1

def buildTree(sub_1_1, sub_1_2):
    treeview = ttk.Treeview(master=sub_1_1,columns=("fullpath", "type"), displaycolumns='')
    treeview.grid(column=0, row=0, sticky='nsew', in_=sub_1_1)
    treeview.bind('<<TreeviewOpen>>', update_tree)

    vsb = Scrollbar(orient="vertical", command=treeview.yview)
    hsb = Scrollbar(orient="horizontal", command=treeview.xview)

    treeview.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    vsb.grid(column=1, row=0, sticky='ns', in_=sub_1_1)
    hsb.grid(column=0, row=1, sticky='ew', in_=sub_1_1)

    sub_1_1.grid_columnconfigure(0, weight=1)
    sub_1_1.grid_rowconfigure(0, weight=1)

    entry = Entry(master=sub_1_2)
    entry.pack(side=LEFT,anchor="w",expand=True,fill='x')

    return treeview, entry

def buildSelectedBox(sub_2_2_1):
    selected = Listbox(master=sub_2_2_1,selectmode=EXTENDED)

    vsb = Scrollbar(orient="vertical", command=selected.yview)
    hsb = Scrollbar(orient="horizontal", command=selected.xview)

    selected.grid(column=0, row=0, sticky='nsew', in_=sub_2_2_1)

    vsb.grid(column=1, row=0, sticky='ns', in_=sub_2_2_1)
    hsb.grid(column=0, row=1, sticky='ew', in_=sub_2_2_1)

    sub_2_2_1.grid_columnconfigure(0, weight=1)
    sub_2_2_1.grid_rowconfigure(0, weight=1)

    return selected