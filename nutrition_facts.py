def NutritionFacts(menu_items):
    '''
        reorganizes food items into dictionary
        names are keys, nutrient type and numbers are values
            nutrient types are keys, numbers are values
    '''
    food_dictionary = {}
    for item in menu_items: # iterate through menu items
        name = item.find("span", class_ = "").text.strip()
        nutrition_divs = item.find_all("div", class_ = "")

        for div_item in nutrition_divs: # iterate through divs until it finds nutrition facts
            if div_item.find("h6", class_ = "") == None:
                continue

            nutrient_items = div_item.find_all("h6", class_ = "")
            nutrient_values = div_item.find_all("p", class_ = "")
            values_dictionary = {}

            for (nut_index, nut_value) in zip(nutrient_items, nutrient_values): # iterate through nutrition facts and put into dictionary
                if "Allergens" in nut_index.text: # non-numeric values aren't appended
                    food_dictionary[name] = values_dictionary # dictionary of dictionaries
                    break
                values_dictionary[nut_index.text.strip()] = nut_value.text.strip().replace(": ", "") # filters out unnecessary characters
    
    return food_dictionary