# Manases Garcia
# CSCI 248 Lab#21
# mom_gui.py
# 12-2-2020
#
# This if the GUI for MomGUI

from tkinter import *
import random

class  MomGui:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('300x100')
        self.root.title('Mom GUI')

        self.instructions = Label(self.root,
            text='This program will tell you what to do next.')

        # You will need to modify next_button
        self.next_button = Button(self.root, text='Next Task',
            command=self.show_task)

        self.task_var = StringVar()
        self.task_label = Label(self.root, textvariable=self.task_var)

        self.instructions.pack(side='top')
        self.next_button.pack(side='top')
        self.task_label.pack(side='top')

        self.root.mainloop()

    def show_task(self):
        random_num = random.randint(1, 4)
        if random_num == 1 or random_num == 2: 
            self.task_var.set('Study')
        elif random_num == 3:
            self.task_var.set('Sleep')
        else:
            self.task_var.set('Eat')

        
def main():
    window = MomGui()

main()
        
