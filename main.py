import pandas as pd
from tkinter import *
from tkinter import filedialog

root = Tk()
root.withdraw()
root.filenames = filedialog.askopenfilenames()
l = []

for file in root.filenames:
    f = open(file, 'r')
    while True:
        line = f.readline()
        if not line: break
        row = line.split()
        l.append(row)
    f.close()

df = pd.DataFrame(l)
writer = pd.ExcelWriter("합친것.xlsx", options={'strings_to_url': False})
df.to_excel(writer, index=False)
writer.close()







