def PrintMenu(nutrition_info):
    '''
        assigns index to each menu item and prints it for user
    '''
    print("")
    print("Here is the menu for your meal.")
    i = 1
    for item in nutrition_info.keys():
        print(str(i) + ". " + item)
        i += 1
    
    return i - 1