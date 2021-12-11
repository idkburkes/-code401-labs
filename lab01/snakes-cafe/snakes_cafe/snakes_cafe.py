
from textwrap import dedent


# lab 1 - Intro to Python


# print intro message
def print_intro():
    print(dedent('''
        **************************************
        **    Welcome to the Snakes Cafe!   **
        **    Please see our menu below.    **
        **
        ** To quit at any time, type "quit" **
        **************************************'''))
    
# print appetizers
def print_apps():
    print(dedent('''
        Appetizers
        ----------
        Wings
        Cookies
        Spring Rolls'''))

# print entrees
def print_entrees():
    print(dedent('''
        Entrees
        -------
        Salmon
        Steak
        Meat Tornado
        A Literal Garden '''))

# print desserts
def print_desserts():
    print(dedent('''
        Desserts
        --------
        Ice Cream
        Cake
        Pie'''))


# print drinks
def print_drinks():
    print(dedent('''
        Drinks
        ------
        Coffee
        Tea
        Unicorn Tears'''))

# Add new item to order
def add_item(new_item, dict):
    
    plural = ""

    if new_item in dict:
       dict[new_item] = dict[new_item] + 1
       if new_item[-1].lower() != 's':
           plural = "s"
    else:
        dict[new_item] = 1

    print(f'\n** {dict[new_item]} order of {new_item}{plural} have been added to your meal **\n')


# main
if __name__ == "__main__":
    print_intro()
    print_apps()
    print_entrees()
    print_desserts()
    print_drinks()

    print(dedent('''
        ***********************************
        ** What would you like to order? **
        ***********************************
        '''))
   
    resume = True
    dict = {}

    while(resume):
        order = input("> ")
        if order.lower().strip() != 'quit':
            add_item(order, dict)
        else: 
            break
    





