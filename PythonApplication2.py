from os import read
from tkinter import *
from tkinter import ttk

class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To-do-list')
        self.root.geometry('650x410+300+150')

        self.label = Label(self.root, text='To-do-list',
                           font='ariel,25', width=10, bd=5, bg='lightblue', fg='black')
        self.label.pack(side='top', fill=BOTH)

        self.label2 = Label(self.root, text='Add task',
                            font='ariel,18', width=10, bd=5, bg='lightblue', fg='black')
        self.label2.place(x=40, y=54)

        self.label3 = Label(self.root, text='Tasks',
                            font='ariel,18', width=10, bd=5, bg='lightblue', fg='black')
        self.label3.place(x=380, y=54)

        self.main_text = Listbox(self.root, height=9, bd=5, width=23, font='ariel,20')
        self.main_text.place(x=380, y=100)

        self.text = Text(self.root, bd=5, height=2, width=30, font='ariel,10')
        self.text.place(x=20, y=120)

        self.button = Button(self.root, text="Add", font='Calibri,20', width=10, bd=5, bg='lightblue', fg='black', command=self.add)
        self.button.place(x=30, y=180)

        self.button2 = Button(self.root, text="Delete", font='Calibri,20', width=10, bd=5, bg='lightblue', fg='black', command=self.erase)
        self.button2.place(x=30, y=280)

        with open('data.txt', 'r') as file:
            read = file.readlines()
            for i in read:
                ready = i.split()
                self.main_text.insert(END, ready)

    def add(self):
        content = self.text.get(1.0, END)
        self.main_text.insert(END, content)
        with open('data.txt', 'a') as file:
            file.write(content)

        self.text.delete(1.0, END)

    def erase(self):
        erase_index = self.main_text.curselection()
        if erase_index:
            self.main_text.delete(erase_index)
            with open('data.txt', 'r') as f:
                new_f = f.readlines()
            with open('data.txt', 'w') as f:
                for line in new_f:
                    item = str(self.main_text.get(0, END))
                    if item not in line:
                        f.write(line)
def main():
    root = Tk()
    gui = Todo(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()