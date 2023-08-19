# -------------------------------------------------------------------------------
# Final Project
# Student Name: Cherubel Kefyalew
# Python Version: 3.11
# Submission Date: 04/24/2023
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
import math as mt

class SmartCart(dict):
    '''dict subclass to maintain user cart'''

    # initialize subtotal and tax amounts
    sub_t = 0.0
    tax_amt = 0.0
    def subtotal(self):
        '''Returns subtotal from a dictionary object'''

        # initialize total amount
        total = 0.0

        # iterate over each key, value in dict
        for key, value in self.items():
            if value > 0:

                # obtain the price and quantity for each key
                total += key.get_price * value

        # add to total variable after multiplying price with the quantity
        SmartCart.sub_t = round(total, 2)

        # return amount correctly formatted with commas and rounded to the nearest tenth decimal place
        return self.commas(SmartCart.sub_t)

    def tax(self):
        # calculate tax amount with 4.3% of subtotal
        SmartCart.tax_amt = SmartCart.sub_t * .043 # OR subtotal * 4.3 / 100

        # return amount correctly formatted with commas and rounded to the nearest tenth decimal place
        return self.commas(round(SmartCart.tax_amt, 2))

    def final_total(self):

        # return amount correctly formatted with commas and rounded to the nearest tenth decimal place
        return self.commas(round(SmartCart.tax_amt + SmartCart.sub_t, 2))

    def commas(self, var):

        if len(str(mt.trunc(var))) <= 3:
            if str(var)[-2] == '.':
                return str(var) + '0'
            return var

        # truncates number and puts it into a list where each item is a string variable of a number
        lis = [i for i in str(mt.trunc(var))]

        # gets the difference of length with truncated number and original number
        decimal = (len(str(var)) - (len(lis))) * -1

        # control variable to start from the -3 index of the number in string format
        control = -3
        y = int(len(lis)/3)

        # inserts ',' into list for every 3 places
        for x in range(y):
            lis.insert(control, ',')
            control -= 4

        # removes extra ',' at end if there is one
        if lis[0] == ',':
            lis.pop(0)

        # adds remaining numbers to end of list that was truncated
        lis.extend(str(var)[decimal:])

        # Checks if number is $xx.x, if it is it adds a 0 at the end
        if lis[-2] == '.':
            lis.extend('0')

        # returns list joined together into a string
        return ''.join(lis)



class Item(object):
    '''Item class defines an item
    available in store. Item object saved in
    lists per category'''
    dairy_items = [] # list of all dairy items
    veg_fruit_items = [] # list of  veg and fruit items
    meat_items = [] # list of  meat and poultry items
    seafood_items = [] # list of seafood items

    def __init__(self, category, name, price, unit):
        '''Initialization method'''
        self.__category = category.lower()
        self.__name = name.lower()
        self.__price = price
        self.__unit = unit.lower()
        # initialize name, price and unit as private method

        if self.get_category == 'Dairy'.lower():
            Item.dairy_items.append(self)
        elif self.get_category in ['Vegetable'.lower(), 'Fruit'.lower()]:
            Item.veg_fruit_items.append(self)
        elif self.get_category == 'Seafood'.lower():
            Item.seafood_items.append(self)
        elif self.get_category in ['Meat'.lower(), 'Poultry'.lower()]:
            Item.meat_items.append(self)

        # append items to list as per category

    # define four get methods
    @property
    def get_category(self):
        return self.__category

    @property
    def get_name(self):
        return self.__name

    @property
    def get_price(self):
        return self.__price

    @property
    def get_unit(self):
        return self.__unit

    # to return four private attributes

    def __str__(self):
        line = 'Category: {}, Name: {}, Price: {}, Unit: {}'\
            .format(self.get_category, self.get_name, self.get_price, self.get_unit)
        return line


# process file

def main():
    # open file, read information, create Item object
    with open('input_data.txt', 'r') as id:
        items = [i.strip().split('|') for i in id]

    for item in items:
        Item(item[1], item[0], float(item[2]), item[3])
    return 'Items compiled successfully\n'

'''
Testing code to check object creation per category list
Comment out when done. After successful completion
of class, the following code will print each item in the input file
'''


def item_list():
    print('Dairy Items')
    for item in Item.dairy_items:
        print(item)
    print('++++++++++')

    print('\nVeg and Fruit Items')
    for item in Item.veg_fruit_items:
        print(item)
    print('++++++++++')

    print('\nMeat Items')
    for item in Item.meat_items:
        print(item)
    print('++++++++++')

    print('\nSeafood Items')
    for item in Item.seafood_items:
        print(item)
    print('++++++++++')


print(main())


if __name__ == '__main__':
    item_list()
