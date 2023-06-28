def PrintNutrition(total_nutrition):
    '''
        prints total nutritional value
    '''
    for i in range(4): # rounds each nutrition fact to tenths place
        total_nutrition[i] = round(total_nutrition[i], 1)
    print("")
    print("You consumed a total of " + str(total_nutrition[0]) + " calories, " + str(total_nutrition[1])
          + " grams of fat, " + str(total_nutrition[2]) + " grams of carbohydrates, and " + str(total_nutrition[3])
          + " grams of protein.")