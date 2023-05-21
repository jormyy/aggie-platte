def NutritionFacts(menu_items):
    '''
        reorganizes food items into dictionary
        name and nutrition label are keys, numbers are values
    '''
    food_dictionary = {}
    for item in menu_items:
        name = item.find("span", class_ = "").text.strip()
        nutrition_divs = item.find_all("div", class_ = "")
        for div_item in nutrition_divs:
            if div_item.find("h6", class_ = "") == None:
                continue
            nutrient_items = div_item.find_all("h6", class_ = "")
            nutrient_values = div_item.find_all("p", class_ = "")
            for (nut_index, nut_value) in zip(nutrient_items, nutrient_values):
                if "Allergens" in nut_index.text: # non-numeric values aren't appended
                    break
                food_dictionary[name + " " + nut_index.text.strip()] = nut_value.text.strip()
    
    return food_dictionary

def CleanFormat(nutrition_facts):
    '''
        original dictionary has unnecessary colons and whitespace
        returns new dictionary with colons and spaces filtered out
    '''
    filtered_dict = {key: value.replace(": ", "") for key, value in nutrition_facts.items()}

    return filtered_dict