def Calculate(nutrition_info, num_food):
    '''
        calculates total nutritional value and puts it into a list
    '''
    print("")
    print("For every food item you ate, type the number of the food, a space, and how many servings you ate.")
    print("When you are done, type \"done\".")
    total_nutrition = [0, 0, 0, 0]

    while 1:
        new_food = input("Type: ")
        if new_food.lower() == "done":
            break
        numbers = new_food.split()
        food_number = int(numbers[0])
        count = int(numbers[1])
        if (food_number < 1) or (food_number > num_food):
            continue
        i = 1
        for items in nutrition_info:
            if i == food_number:
                total_nutrition[0] += count * float(nutrition_info[items]["Calories"])
                total_nutrition[1] += count * float(nutrition_info[items]["Fat (g)"])
                total_nutrition[2] += count * float(nutrition_info[items]["Carbohydrates (g)"])
                total_nutrition[3] += count * float(nutrition_info[items]["Protein (g)"])
                break
            i += 1
    
    return total_nutrition