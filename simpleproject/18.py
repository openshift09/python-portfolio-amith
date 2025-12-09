import csv

from tkinter.tix import COLUMN

with open("users.csv") as f:
    for row in csv.reader(f):
        print(COLUMN)
