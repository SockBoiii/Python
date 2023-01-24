# Manases Garcia 
# CSCI 248 Homework#15 Problem#2
# gasmiles_gui.py
# 12-10-2020
#
# This program is a gui application that calculates a car's gas mileage. 

from tkinter import *

class MileageGUI:

    def __init__(self):
        self.root = Tk()
        self.root.geometry('320x200')
        self.root.title('MPG Calculator')

        self.miles_label = Label(self.root,
            padx=10, pady=10, text='Miles')
        self.miles_label.pack()

        self.miles_var = StringVar()
        self.miles_entry = Entry(self.root, width=30,
            textvariable=self.miles_var)
        self.miles_entry.pack()

        self.gallons_label = Label(self.root, pady=10,
            padx=10, text='Gallons')
        self.gallons_label.pack()

        self.gallons_var = StringVar()
        self.gallons_entry = Entry(self.root, width=30,
            textvariable=self.gallons_var)
        self.gallons_entry.pack()

        self.button = Button(self.root, text='Calculate MPG',
            command=self.get_calculation)
        self.button.pack(expand=True)

        self.calculation_var = StringVar()
        self.calculation_label = Label(self.root,
            textvariable=self.calculation_var)
        self.calculation_label.pack(side='bottom')

        self.root.mainloop()

    def get_calculation(self):
        mpg = (float(self.gallons_var.get())) / (float(self.miles_var.get()))
        self.calculation_var.set(self.miles_var.get() + ' miles /'
            + self.gallons_var.get() + ' gallons = %3.1f miles per gallon' % mpg)

        self.miles_var.set('')
        self.gallons_var.set('')

def main():
    window = MileageGUI()

main()
