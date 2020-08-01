"""

They are good at taking orders, but they don't know how to capitalize words, or use a space bar!

All the orders they create look something like this:

"milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"

The kitchen staff are threatening to quit, because of how difficult it is to read the orders.
Their preference is to get the orders as a nice clean string with spaces and capitals like so:

"Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke"

The kitchen staff expect the items to be in the same order as they appear in the menu.
The menu items are fairly simple, there is no overlap in the names of the items:

1. Burger
2. Fries
3. Chicken
4. Pizza
5. Sandwich
6. Onionrings
7. Milkshake
8. Coke
"""

def insert_space(string, integer):
    return string[0:integer] + ' ' + string[integer:]

def get_order(order):
    menu = ["Burger", "Fries", "Chicken", "Pizza", "Sandwich", "Onionrings", "Milkshake", "Coke"]

    # For each item in the menu, go over the whole order and place spaces after
    for item in menu:
        # Insert a space after the first occurence of the item
        itemLen = len(item)
        startLoc = order.find(item.lower())
        endLoc = startLoc + itemLen
        # Item found
        if startLoc != -1:
            order = insert_space(order, endLoc)
            
        # Find next occurences of menu items if any and place spaces
        while (order.find(item.lower(), endLoc, len(order) - 1)) != -1:
            startLoc = order.find(item.lower(), endLoc, len(order) - 1)
            endLoc = startLoc + itemLen
            order = insert_space(order, endLoc)
    
    orderList = order.title().rstrip().split()
    finalOrder = []

    # Append index locations to final order
    for item in orderList:
        finalOrder.append(menu.index(item))
        
    # Sort in ascending order
    finalOrder.sort()
    # Replace them with the strings and join
    for x in range(0, len(finalOrder)):
        finalOrder[x] = menu[finalOrder[x]]
    return " ".join(finalOrder)


print(get_order("milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"))
