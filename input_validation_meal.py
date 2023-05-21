import different_meals as DM

def Meal(today_menu):
    '''
        input validation function for the type of meal
        not case-sensitive but user must type "breakfast", "lunch", or "dinner"
        calls Breakfast, Lunch, or Dinner function depending on input
    '''
    meals = today_menu.find_all("div", class_ = "")
    valid = False
    while not valid:
        valid = True
        meal = input("What meal did you eat? Type Breakfast, Lunch, or Dinner: ")
        if meal.lower() == "breakfast":
            current_meal = DM.Breakfast(meals)
        elif meal.lower() == "lunch":
            current_meal = DM.Lunch(meals)
        elif meal.lower() == "dinner":
            current_meal = DM.Dinner(meals)
        else:
            print("Please enter a valid meal type.")
            valid = False # reenter loop if not valid
    
    return current_meal