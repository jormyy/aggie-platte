def Breakfast(todays):
    '''
        looks for keyword "Breakfast" to get menu for breakfast
    '''
    for meal in todays:
        if "Breakfast" in meal.text:
            return meal

def Lunch(todays):
    '''
        looks for keyword "Lunch" to get menu for breakfast
    '''
    for meal in todays:
        if "Lunch" in meal.text:
            return meal

def Dinner(todays):
    '''
        looks for keyword "Dinner" to get menu for breakfast
    '''
    for meal in todays:
        if "Dinner" in meal.text:
            return meal