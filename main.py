import pandas as pd
import mmap
from tkinter import *
from tkinter import filedialog
from tqdm import tqdm


def get_num_lines(file_name):
    fp = open(file_name, "r+")
    buf = mmap.mmap(fp.fileno(), 0)
    lines = 0
    while buf.readline():
        lines += 1
    return lines


if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    root.filenames = filedialog.askopenfilenames()
    l = []

    for file in tqdm(root.filenames, desc="전체 진행률", position=0, leave=True):
        f = open(file, 'r')
        if not f:
            print("cannot open " + file)
            continue
        # print("reading : " + file)
        for line in tqdm(f, total=get_num_lines(file), desc=file, position=0, leave=True):
            row = line.split()
            l.append(row)
        # print("done : " + file)
        f.close()

    df = pd.DataFrame(l)
    writer = pd.ExcelWriter("Total.xlsx", options={'strings_to_url': False})
    df.to_excel(writer, index=False)
    writer.close()

    print("complete writing to excel")



