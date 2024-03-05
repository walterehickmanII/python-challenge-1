
while True:
    user_input = menu_selection("main")
    if user_input == "1":
        print("You chose Option 1")
    elif user_input == "2":
        print("You chose Option 2")
    elif user_input == "3":
        while True:
            sub_input = menu_selection("sub")
            if sub_input == "a":
                print("You chose Sub-option 1")
            elif sub_input == "b":
                print("You chose Sub-option 2")
            elif sub_input == "c":
                break
            else:
                print("Invalid selection")
    elif user_input == "4":
        print("Exiting...")
        break
    else:
        print("Invalid selection")