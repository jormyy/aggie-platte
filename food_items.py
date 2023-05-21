def Items(the_meal):
    '''
        looks for every food item on the menu
        items without nutrition facts are filtered out
        returns list of food items with nutrition facts
    '''
    items = []
    possible_items = the_meal.find_all("li", class_ = "trigger")
    for food_item in possible_items:
        if "N/A" not in food_item.text: # filters out food that doesn't provide nutrition facts
            items.append(food_item)
    
    return items