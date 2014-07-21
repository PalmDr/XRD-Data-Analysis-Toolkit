__author__ = 'j'

import os

def fill_tree(treeview, node):
    if treeview.set(node, "type") != 'directory':
        return

    path = treeview.set(node, "fullpath")
    # Delete the possibly 'dummy' node present.
    treeview.delete(*treeview.get_children(node))

    parent = treeview.parent(node)
    for p in os.listdir(path):
        p = os.path.join(path, p)
        ptype = None
        if os.path.isdir(p):
            ptype = 'directory'

        fname = os.path.split(p)[1]
        oid = treeview.insert(node, 'end', text=fname, values=[p, ptype])
        if ptype == 'directory':
            treeview.insert(oid, 0, text='dummy')

def update_tree(event):
    treeview = event.widget
    fill_tree(treeview, treeview.focus())

def create_root(treeview, startpath):
    dfpath = os.path.abspath(startpath)
    node = treeview.insert('', 'end', text=dfpath,
            values=[dfpath, "directory"], open=True)
    fill_tree(treeview, node)
    return dfpath