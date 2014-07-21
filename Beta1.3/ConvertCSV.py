__author__ = 'j'

import pandas as pd

FACTOR = 10

def convertCSV(filelists, factor):
    allcsv = pd.DataFrame()
    for i, file in enumerate(filelists):
        a = pd.read_csv(file, header=1)
        a.index = a[a.columns[0]]
        a = pd.DataFrame(a[a.columns[4]])
        a.columns = [str(i)]
        if allcsv.empty:
            allcsv = a
        else:
            allcsv = pd.merge(allcsv, a, how='outer', left_index=True, right_index=True)

    for i in range(len(allcsv.columns)-1):
        allcsv[str(i+1)] = allcsv[str(i)] * factor

    return allcsv

