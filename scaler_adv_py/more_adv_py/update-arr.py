'''
Problem Description:

Your friend Suresh is running a restaurant and wants to update the price of some items on the menu. Suresh has made his menu in a nested list such that the menu list contains sub-lists in the form [item_name, Price]. Suresh wants to increase the price of some selected dishes by 10%.

Menu List:

Menu = [['Sweet_Corn_Soup', 300.0], ['Cream_of_Tomato_Soup', 100.0], ['Bacon_and_Cheese', 150.0], ['Honey_Mustard', 230.0], ['Hot_Coffee', 50.0], ['Cold_Coffee', 50.0], ['Egg_Sandwiches', 130.0], ['Tacos', 400.0]]
Input Format:

Space separated strings representing the items whose price is to be reduced
Output Format:

The main menu list with updated price.
'''

def new_menu(item_list):
    #This is the Menu list we want to update
    Menu = [['Sweet_Corn_Soup', 300.0], ['Cream_of_Tomato_Soup', 100.0], 
            ['Bacon_and_Cheese', 150.0], ['Honey_Mustard', 230.0], ['Hot_Coffee', 50.0], 
            ['Cold_Coffee', 50.0], ['Egg_Sandwiches', 130.0], ['Tacos', 400.0]]
    #Write your code here
    
    menu = item_list.split()
    index = 0
    for name, price in Menu:
        if name in menu:
            price += price * 0.1
            Menu[index][1] = price
        index += 1  
    
    return Menu

A = "Hot_Coffee Cold_Coffee Tacos"
print(new_menu(A))