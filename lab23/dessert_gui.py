# Manases Garcia, Alex Pantoja, Ashley Martinez Rodriguez, Jackson Montgomery
# CSCI 248 Lab#23 Problem #1
# dessert_gui.py
# 12-3-2020
#
# This program creates a GUI that  orders desserts and keeps counts of how many
# sold.

from tkinter import *
import tkinter.font
import tkinter.messagebox # ADD import statement for dialog boxes HERE


DESSERT1 = 1
DESSERT2 = 2
DESSERT3 = 3

DESSERT_OPT1 = 'Chocolate Cake'
DESSERT_OPT2 = 'Cheese Cake'
DESSERT_OPT3 = 'Pumpkin Pie'

class OrderDessert:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('350x160')
        self.root.title('Desserts')

        self.__count = 0

        self.label = Label(self.root, font=('Times', 14),
            text='Choose your dessert')
        self.label.pack(side='top', pady=10)

        # Create the dessert choices
        self.dessert = IntVar()
        self.dessert.set(DESSERT1)
        # NEED CODE HERE
        self.dessert1 = Radiobutton(self.root, text=DESSERT_OPT1,
            variable=self.dessert, value=DESSERT1)
        self.dessert2 = Radiobutton(self.root, text=DESSERT_OPT2,
            variable=self.dessert, value=DESSERT2)
        self.dessert3 = Radiobutton(self.root, text=DESSERT_OPT3,
            variable=self.dessert, value=DESSERT3)
        self.dessert1.pack()
        self.dessert2.pack()
        self.dessert3.pack()

        self.bottom_frame = Frame(self.root)
        self.bottom_frame.pack(pady=10)

        self.quit_button = Button(self.bottom_frame, text='Quit',
            command=self.root.destroy)
        self.order_button = Button(self.bottom_frame, 
            text='Place Order', command=self.process_choices)
        self.quit_button.pack(side='left', padx=40)
        self.order_button.pack(side='right', padx=40)

        self.root.mainloop()

    # Determine which choices were made, display a
    # dialog box with the result, increment and print
    # the count to the command line
    def process_choices(self):
        # ADD code to increment and print the count
        self.__count += 1
        print('%d Dessert(s) sold.' % self.__count)

        # FINISH this code
        if self.dessert.get() == DESSERT1:
            result = 'You ordered ' + DESSERT_OPT1
            print('%s ordered' % DESSERT_OPT1)
        elif self.dessert.get() == DESSERT2: 
            result = 'You ordered ' + DESSERT_OPT2
            print('%s ordered' % DESSERT_OPT2)
        else:
            result = 'You ordered ' + DESSERT_OPT3
            print('%s ordered' % DESSERT_OPT3)

        # Display results in dialog box    
        tkinter.messagebox.showinfo(title='Order',
            message=result)

        # ADD code to set default choice to DESSERT1
        self.dessert.set(DESSERT1)

def main():
    window = OrderDessert()

main()
        
