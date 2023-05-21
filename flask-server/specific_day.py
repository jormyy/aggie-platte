def TodayMenu(index, website):
    '''
        uses user-inputted day to assign an index to it
        uses that index to get the menu for the user-inputted day
    '''
    day_id = "tab" + str(index) + "content"
    menu = website.find("div", id = day_id)
    
    return menu