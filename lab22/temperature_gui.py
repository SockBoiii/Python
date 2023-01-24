# Manases Garcia
# CSCI 248 Lab#22
# temperature_gui.py
# 12-2-2020
#
# This program is a GUI for converting fahrenheit to celsius.

from tkinter import *

class  TemperatureGUI:

    def __init__(self):
        self.root = Tk()
        self.root.geometry('260x160')
        self.root.title('Conversion GUI')

        self.frame = Frame(self.root)
        self.fahrenheit_label = Label(self.frame, 
            padx=10, pady=10, text='Fahrenheit')
        self.fahrenheit_var = StringVar()
        self.fahrenheit_entry = Entry(self.frame,
            textvariable=self.fahrenheit_var)  
        self.fahrenheit_label.pack(side='left')
        self.fahrenheit_entry.pack(side='right')

        self.button = Button(self.root, text='Convert', bg='yellow',
            command=self.convert)

        self.celsius_var = StringVar()
        self.celsius_label = Label(self.root, textvariable=self.celsius_var)

        self.frame.pack(side='top')
        self.button.pack(expand=True)
        self.celsius_label.pack(side='bottom')

        self.root.mainloop()

    def convert(self):
        celsius = (int(self.fahrenheit_var.get())- 32) * .556
        self.celsius_var.set(self.fahrenheit_var.get() + ' Fahrenheit' + \
            '= %3.1f Celsius.' % celsius)

        # Reset the entry
        self.fahrenheit_var.set('')
        
def main():
    window = TemperatureGUI()

main()

