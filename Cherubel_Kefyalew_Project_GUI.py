# -------------------------------------------------------------------------------
# Final Project
# Student Name: Cherubel Kefyalew
# Python Version: 3.11
# Submission Date: 04/28/2023
# -------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
# -------------------------------------------------------------------------------
# References:
# -------------------------------------------------------------------------------
# Notes to grader:
# -------------------------------------------------------------------------------
# Your source code below
# -------------------------------------------------------------------------------

from tkinter import *
from Cherubel_Kefyalew_Project_CLASS import Item, SmartCart
from functools import partial
import random, string # used in random receipt no function

class MyFrame(Frame):
    def __init__(self, root):
        '''Constructor method'''
        Frame.__init__(self, root) # Frame class initialization
        self.init_container() # initialize all widget containers
        self.cart = SmartCart() # initialize SmartCart dict object - key = Item object item selected, value = quantity
        self.welcome() # start the application
        self.data = StringVar(self, 'Subtotal: $0.00') # Associated with subtotal label

        
    def init_container(self):
        '''Initialize widget containers'''
        self.quantity_entries = [] # qunatity entry list
        self.states = [] # holds state if selected/not i-th list item holds selection for i-th item
 
    def clear_frame(self): 
        '''Clears the previous frame'''
        for widget in self.winfo_children():
            widget.destroy()

    def exit_application(self):
        '''Exits the program'''
        self.quit()
        print('\nThank you for using Instant Cart!')
 
    def welcome(self):
        '''1. Welcome window - refer spec file for details'''
        self.clear_frame()

        Label(self, text='****Welcome to Instant Cart!****', background="gray70").pack(side=TOP)

        # Start Ordering: Button – start the program, command
        Button(self, text='Start Ordering', command=self.shop_by_category).pack()

        # Exit Application: Button – exit the program, command = exit_application
        Button(self, text='Exit Application', command=self.exit_application).pack()


    def shop_by_category(self):
        '''2. Widget to display different category of items - refer spec file for details'''
        self.clear_frame()
        self.init_container()

        # a.	Choose Category: label
        Label(self, text='Chose Category', background="gray70").pack()

        # b.	Dairy: Button – command = start (code below)
        # partial is a special method to pass an argument during button command
        # for dairy category Item.dairy_items will be passed to display all dairy item
        self.dairy_button  = Button(self, text = "Dairy", command=partial(self.start, Item.dairy_items)).pack()

        # c.	Vegetable and Fruit - veg_fruit_button: Button – command = start (Same as dairy)
        self.veg_fruit_button = Button(self, text='Vegetable and Fruit', command=partial(self.start, Item.veg_fruit_items)).pack()

        # d.	Poultry and Meat - poultry_meat_button: Button – command = start(Same as dairy)
        self.poultry_meat_button = Button(self, text='Poultry and Meat', command=partial(self.start, Item.meat_items)).pack()

        # e.	Seafood: Button - seafood_button – command = start(Same as dairy)
        self.seafood_button = Button(self, text='Seafood', command=partial(self.start, Item.seafood_items)).pack()

        # f.	Go Back: Button – command = welcome (go back to #1)
        self.go_back = Button(self, text='Go Back', command=self.welcome).pack()


    def start(self, current_items):
        ''''3. Start ordering from selected category,
        list passed by command will be used as current_items'''
        self.clear_frame()
        self.init_container()
        
        # creating widgets for items using a for loop
        Label(self, text='Select item(s) and Quantity', background="gray70").grid(row=0, columnspan=4)
        row = 0#########

        # iterative over each item of current items and
        for item in current_items:

            # create that many checkbutton, price and unit label,and quantity entry
            self.states.append(IntVar()) # keeps track if an item is selected
            checkbutton = Checkbutton(self, text=item.get_name, variable=self.states[row])# create check buttons
            checkbutton.grid(row = row+2, column = 0)

            # create and layout a price label, set text to item.get_price()
            Label(self, text='Price {}'.format(item.get_price)).grid(row=row+2, column=1)

            # create and layout a quantity entry and append to quantity_entries, set width = 2
            entry = Entry(self, width=4)
            self.quantity_entries.append(entry)
            entry.grid(row=row+2, column=2)

            # create and layout unit_label and set text to item.get_unit() function
            Label(self, text=item.get_unit).grid(row=row+2, column=3)
            row += 1

        # create and layout select categories: button, command = shop_by_category
        Button(self, text='Select Categories', command=self.shop_by_category).grid(row=row+3, column=2)

        # create and layout add_to_cart_button, command = partial(self.add_to_cart, current_items)
        # with each add_to_cart button being pressed
        Button(self, text='Add to Cart', command=partial(self.add_to_cart, current_items)).grid(row=row+4, column=2)

        # create and layout button: checkout, command = self.checkout
        Button(self, text='Checkout', command=self.checkout).grid(row=row+5, column=2)

        # create and layout subtotal lable, set textvaribale = self.data so it changes
        Label(self, textvariable=self.data, background="gray70").grid(row=row+6, column=0)

    def add_to_cart(self, current_items): #####
        '''3. Added to cart, displays subtotal - see spec file for details layout'''
        for i in range(len(current_items)):

            # if item is selected:
            # get() the value of i-th item of self.states -> returns 1 if selected otherwise 0
            if self.states[i].get() == 1:
                # get the product quantity from quantity_entries using get() function
                if current_items[i] in self.cart.keys():
                    self.cart[current_items[i]] = self.cart[current_items[i]] + int(self.quantity_entries[i].get())
                else:
                    # add item to self.cart dict where k = item object, v = quantity
                    self.cart[current_items[i]] = int(self.quantity_entries[i].get())


        # set the StringVar to be the current subtotal (SmartCart object self.cart has subtotal method)
        self.data.set('Subtotal: ${}'.format(self.cart.subtotal()))

        # refer to class file
        self.start(current_items)
        
    def get_receipt_number(self):
        '''Generate random receipt number'''
        return  ''.join(random.choices(string.ascii_letters.upper() + string.digits, k=4))

    def checkout(self):
        '''4. Check out window '''
        self.clear_frame()

        # refer to receipt frame

        #    Your e-receipt: Label
        Label(self, text='Your e-receipt', background="gray70").grid(row=0, columnspan=4)

        #    Receipt Number: Label - Randomly generated by program - text = get_receipt_number()
        Label(self, text='Receipt Number: {}'.format(self.get_receipt_number())).grid(columnspan=4, sticky="nsew")
        Label(self, text='*************').grid(columnspan=4, sticky="nsew")

        #	Name Price Quantity Unit: Header Label
        Label(self, text='Name').grid(row=3, column=0)
        Label(self, text='Price').grid(row=3, column=1)
        Label(self, text='Quantity').grid(row=3, column=2)
        Label(self, text='Unit').grid(row=3, column=3)
        row = 4

        #	Item purchased, price quantity, unit: Label - from cart dictionary using self.cart.items()
        for key, value in self.cart.items():
            Label(self, text=key.get_name).grid(row=row, column=0)
            Label(self, text=key.get_price).grid(row=row, column=1)
            Label(self, text=value).grid(row=row, column=2)
            Label(self, text=key.get_unit).grid(row=row, column=3)
            row += 1

        #	Subtotal: Label - get self.cart subtotal - new label
        Label(self, textvariable=self.data).grid(columnspan=4, sticky="nsew")

        #	Tax: Label - 4.3%
        Label(self, text='Tax (4.3%): ${}'.format(self.cart.tax())).grid(columnspan=4, sticky="nsew")

        #	Total: Label - subtotal + tax
        Label(self, text='Total: ${}'.format(self.cart.final_total())).grid(columnspan=4, sticky="nsew")

        #	‘Thank you’ message: Label
        Label(self, text='Thank you for using Instant Cart!').grid(columnspan=4, sticky="nsew")
        Label(self, text='*************').grid(columnspan=4, sticky="nsew")

        #	Exit application: Button – exit the program- command = exit_application
        Button(self, text='Exit Application', command=self.exit_application).grid(columnspan=4)


        

# main driver code
# create root window


def main():
    root = Tk()
    root.title("Instant Cart")
    f = MyFrame(root)
    f.pack()
    f.mainloop()

# create a myframe object and layout
# call mainloop

main()
