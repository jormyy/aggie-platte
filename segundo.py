import requests
from bs4 import BeautifulSoup
import input_validation as IV

html_text = requests.get("https://housing.ucdavis.edu/dining/menus/dining-commons/segundo/").text
soup = BeautifulSoup(html_text, "lxml")

def TodayMenu(index, website):
    day_id = "tab" + str(index) + "content"
    menu = website.find("div", id = day_id)
    
    return menu

def Meal(today_menu):
    meals = today_menu.find_all("div", class_ = "")
    valid = False
    while not valid:
        valid = True
        meal = input("What meal did you eat? ")
        if meal.lower() == "breakfast":
            current_meal = Breakfast(meals)
        elif meal.lower() == "lunch":
            current_meal = Lunch(meals)
        elif meal.lower() == "dinner":
            current_meal = Dinner(meals)
        else:
            print("Please enter a valid meal type.")
            valid = False
    
    return current_meal
        
def Breakfast(todays):
    for meal in todays:
        if "Breakfast" in meal.text:
            return meal

def Lunch(todays):
    for meal in todays:
        if "Lunch" in meal.text:
            return meal

def Dinner(todays):
    for meal in todays:
        if "Dinner" in meal.text:
            return meal

def Items(the_meal):
    items = []
    possible_items = the_meal.find_all("li", class_ = "trigger")
    for food_item in possible_items:
        if "N/A" not in food_item.text:
            items.append(food_item)
    
    return items

def NutritionFacts(menu_items):
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
                if "Allergens" in nut_index.text:
                    break
                food_dictionary[name + " " + nut_index.text.strip()] = nut_value.text.strip()
    
    return food_dictionary

day_index = IV.WhatDay()
today_menu = TodayMenu(day_index, soup)
this_meal = Meal(today_menu)
menu_items = Items(this_meal)
nutrition_facts = NutritionFacts(menu_items)
print(nutrition_facts)