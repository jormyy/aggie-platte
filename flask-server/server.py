### Integrate HTML With Flask
### HTTP verb GET And POST
from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
from which_dc import WhichDC
from input_validation_day import WhatDay
from specific_day import TodayMenu
from input_validation_meal import Meal
import different_meals as DM
from food_items import Items
from nutrition_facts import NutritionFacts
from write_to_json import WriteTojson

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/segundo.html')
def segundo():
    url = "https://housing.ucdavis.edu/dining/menus/dining-commons/segundo/"
    html_text = requests.get(url).text
    global soup 
    soup = BeautifulSoup(html_text, "lxml")
    return render_template("segundo.html")

@app.route('/tercero.html')
def tercero():
    url = "https://housing.ucdavis.edu/dining/menus/dining-commons/tercero/#"
    html_text = requests.get(url).text
    global soup 
    soup = BeautifulSoup(html_text, "lxml")
    return render_template("tercero.html")

@app.route('/cuarto.html')
def cuarto():
    url = "https://housing.ucdavis.edu/dining/menus/dining-commons/cuarto/"
    html_text = requests.get(url).text
    global soup 
    soup = BeautifulSoup(html_text, "lxml")
    return render_template("cuarto.html")

@app.route('/sunday.html')
def sunday():
    day_index = 1
    day_id = "tab" + str(day_index) + "content"
    global menu 
    menu = soup.find("div", id = day_id)
    return render_template("sunday.html")

@app.route('/monday.html')
def monday():
    day_index = 2
    day_id = "tab" + str(day_index) + "content"
    global menu 
    menu = soup.find("div", id = day_id)
    return render_template("monday.html")

@app.route('/tuesday.html')
def tuesday():
    day_index = 3
    day_id = "tab" + str(day_index) + "content"
    global menu 
    menu = soup.find("div", id = day_id)
    return render_template("tuesday.html")

@app.route('/wednesday.html')
def wednesday():
    day_index = 4
    day_id = "tab" + str(day_index) + "content"
    global menu 
    menu = soup.find("div", id = day_id)
    return render_template("wednesday.html")

@app.route('/thursday.html')
def thursday():
    day_index = 5
    day_id = "tab" + str(day_index) + "content"
    global menu 
    menu = soup.find("div", id = day_id)
    return render_template("thursday.html")

@app.route('/friday.html')
def friday():
    day_index = 6
    day_id = "tab" + str(day_index) + "content"
    global menu 
    menu = soup.find("div", id = day_id)
    return render_template("friday.html")

@app.route('/saturday.html')
def saturday():
    day_index = 7
    day_id = "tab" + str(day_index) + "content"
    global menu 
    menu = soup.find("div", id = day_id)
    return render_template("saturday.html")

@app.route('/breakfast.html')
def breakfast():
    this_meal = DM.Breakfast(menu)
    menu_items = Items(this_meal) # gets every menu item that has nutrient facts
    nutrition_facts = NutritionFacts(menu_items) # organizes menu items in a dictionary
    WriteTojson(nutrition_facts) # writes all the facts into a json file
    return render_template("breakfast.html")

@app.route('/lunch.html')
def lunch():
    this_meal = DM.Lunch(menu)
    menu_items = Items(this_meal) # gets every menu item that has nutrient facts
    nutrition_facts = NutritionFacts(menu_items) # organizes menu items in a dictionary
    WriteTojson(nutrition_facts) # writes all the facts into a json file
    return render_template("lunch.html")

@app.route('/dinner.html')
def dinner():
    this_meal = DM.Dinner(menu)
    menu_items = Items(this_meal) # gets every menu item that has nutrient facts
    nutrition_facts = NutritionFacts(menu_items) # organizes menu items in a dictionary
    WriteTojson(nutrition_facts) # writes all the facts into a json file
    return render_template("dinner.html")

@app.route('/menu.html')
def menu():
    with open("food.json", "r") as file:
        return render_template("menu.html", q=file.readlines())
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)