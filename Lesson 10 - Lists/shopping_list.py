# =====================================================================
# PROJECT: Shopping List & Budget Tracker
# GOAL: Practice adding items to lists and calculating data from them.
# =====================================================================

# INITIALIZE YOUR LISTS
# TODO: Create an empty list called 'shopping_cart' to hold item names.
# TODO: Create an empty list called 'price_list' to hold item prices.


# MAIN
# TODO Create an infinite while loop

    # Info for user
    # TODO Output info for user:
    # Current cart/shopping list
    # Current prices

    # TODO Output Options for user: 1. Add item to cart, 2. Remove item from cart, 3. Clear cart and restart, 4. View total and checkout
    # TODO Get user input (1-4) and save in variable

    # -----------------------------------------------------------------
    # OPTION 1: ADD ITEM 
    # -----------------------------------------------------------------
    # TODO Check if option 1
        # TODO Ask user for the name of the item
        # TODO Add it to shopping list
        # TODO Add user for price of item
        # TODO Change price into a float
        # TODO Add price to price list

    # -----------------------------------------------------------------
    # OPTION 2: REMOVE ITEM 
    # -----------------------------------------------------------------
    # TODO Else check if option 2
        # TODO Ask user for the name of the item they want to remove
        # TODO Use .index() to get the index of the item and save in variable
        # TODO Remove the item from cart
        # TODO Remove the price (using its index) from the price list


    # -----------------------------------------------------------------
    # OPTION 3: CLEAR CART (Practice clearing a list)
    # -----------------------------------------------------------------
    # TODO Else check if option 3
        # TODO: Use the .clear() method on both lists to empty them out.
        # TODO Tell them their cart is empty.


    # -----------------------------------------------------------------
    # OPTION 4: CHECKOUT
    # -----------------------------------------------------------------
    # TODO Else check if option 4
        #total_cost = sum(price_list)

        
        # TODO Display the results
        # TODO Exit the loop (to exit the program)

    # -----------------------------------------------------------------
    # NO OPTION
    # -----------------------------------------------------------------
    # TODO Otherwise
        # TODO Tell them that option isn't valid

# ====================================================================
# EXTENSION
# Add a budget to the list
# TODO Tell them if their cart is over budget
# TODO Recommend items to remove based on their price.

# =====================================================================
# EXPERT
# Change your program to use dictionaries so prices are connected to shopping items
# Display the cart in alphabetical order
# Add an option to display the cart in order of price.


shopping_cart =[]
price_list =[]
answer_vaild = False
while True:
    answer_vaild = False
    print(f"printing current shopping list and current prices\n {shopping_cart}\n {price_list}")
    while answer_vaild == False:
        print("you have 4 options \n1. Add item to cart\n2. Remove item from cart\n3. Clear cart and restart\n4. View total and checkout")
        user_pick = input("please use the numbers \n")
        try:
            user_pick = int(user_pick)
            answer_vaild = True
        except:
            print("invaild answer try again\n")
            answer_vaild = False
    if user_pick == 1:
        shopping_cart.append(input("what is the item called "))
        answer_vaild = False
        while answer_vaild == False:
            try:
                item_price = float(input("what is the item cost "))
                answer_vaild = True
            except:
                print("invaild answer try again\n")
                answer_vaild = False
        price_list.append(item_price)
    elif user_pick == 2:
        answer_vaild = False
        while answer_vaild == False:
            try:
                remove_item_name = input("what is the name of the item you want to remove ")
                remove_item_index = shopping_cart.index(remove_item_name)
                shopping_cart.pop(remove_item_index)
                price_list.pop(remove_item_index)
                answer_vaild = True
            except:
                print("invaild answer try again\n")
                answer_vaild = False
    elif user_pick == 3:
        shopping_cart.clear()
        price_list.clear()
        print("cart is clear")
    elif user_pick == 4:
        total_cost = sum(price_list)
        print(f"the total cost is {total_cost}")

            
            
        