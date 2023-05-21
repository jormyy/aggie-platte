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

day_index = IV.WhatDay()
today_menu = TodayMenu(day_index, soup)
this_meal = Meal(today_menu)
print(this_meal)
# menu_items = today_menu.find_all("li", class_ = "trigger")
# for item in menu_items:
#     print(item.find("span", class_ = "").text.strip())