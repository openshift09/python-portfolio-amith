import tkinter as tk

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Python GUI Calculator")
root.geometry("300x400")

entry = tk.Entry(root, width=20, font=('Arial', 18), borderwidth=3, relief='solid')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('+',4,2), ('=',4,3)
]

for (text, row, col) in buttons:
    if text == "=":
        tk.Button(root, text=text, width=5, height=2, font=('Arial', 14),
                  command=calculate).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(root, text=text, width=5, height=2, font=('Arial', 14),
                  command=lambda val=text: button_click(val)).grid(row=row, column=col, padx=5, pady=5)

clear_button = tk.Button(root, text="C", width=24, height=2, font=('Arial', 14), command=clear)
clear_button.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

root.mainloop()
