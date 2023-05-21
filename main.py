import requests
from bs4 import BeautifulSoup
from which_dc import WhichDC
from input_validation_day import WhatDay
from specific_day import TodayMenu
from input_validation_meal import Meal
from food_items import Items
from nutrition_facts import NutritionFacts
from write_to_json import WriteTojson

if __name__ == "__main__":
    url = WhichDC()
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, "lxml")

    day_index = WhatDay() # gets day of week and assigns index to it
    today_menu = TodayMenu(day_index, soup) # uses day_index and html_text to get menu of the day
    this_meal = Meal(today_menu) # gets breakfast, lunch, or dinner menu
    menu_items = Items(this_meal) # gets every menu item that has nutrient facts
    nutrition_facts = NutritionFacts(menu_items) # organizes menu items in a dictionary
    WriteTojson(nutrition_facts) # writes all the facts into a json file