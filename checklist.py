# coding: utf-8
checklist = list()

# CREATE
def create(item):
    checklist.append(item)

# READ
def read(index):
    print(checklist[index])
    return checklist[index]

# UPDATE
def update(index, item):
    checklist[index] = item

# DESTROY
def destroy(index):
    checklist.pop(index)

# LIST ALL ITEMS AND INDICES
def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

# CHECKMARK
def mark_completed(index):
    completed_item = "√" + checklist[index]
    print(completed_item)

# INPUT
def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

# SELECT 
def select(function_code):
    # Create item
    if function_code.upper() == "C":
        input_item = user_input("Input item:")
        create(input_item)

    # Read item
    elif function_code.upper() == "R":
        item_index = user_input("Index Number?")
        item_index = int(item_index)
        # ensures index is in checklist
        if item_index < len(checklist):
            read(item_index)
        else:
            print("Please select a real index.")     

    # Update list
    elif function_code.upper() == "U":
        item_index = user_input("What index would you like to update?")
        # casts response to integer
        item_index = int(item_index)
        # ensures index is in checklist
        if item_index < len(checklist):
            replacement = user_input("What would you like to change index " + str(item_index) + " to?")
            user_is_sure = user_input("Are you sure you want to change " + checklist[item_index] + " to " + replacement + "? (Y/N)")
            if user_is_sure.upper() == "Y" or user_is_sure.upper() == "YES":
                checklist[item_index] = replacement
                print("Index " + str(item_index) + " has been updated.")
            else:
                print("Did not update.")
        else:
            print("Please select a real index.")        

    # Print all items
    elif function_code.upper() == "P":
        list_all_items()

    # Delete item
    elif function_code.upper() == "D":
        item_index = user_input("Index Number?")
        item_index = int(item_index)
        if item_index < len(checklist):
            item = checklist[item_index]
            checklist.remove(item)
            print(item + " has been removed.")
        else:
            print("Please select a real index.")  

    elif function_code.upper() == "Q":
        return False

    # Catch all
    else:
        print("Unknown Option")
    return True
    

def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")

    print(read(0))
    print(read(1))
    list_all_items()
    mark_completed(1)
    # Call your new function with the appropriate value
    select("C")
    # View the results
    list_all_items()
    # Call function with new value
    select("R")
    # View results
    list_all_items()

#test()

running = True
while running:
    selection = user_input(
        "Press C to add to list, R to read from list, U to update list, P to display list, D to delete from list and Q to quit")
    running = select(selection)