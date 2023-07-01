# Aggie Platter
Python program to track nutrients at UC Davis dining commons

## Description
This program uses the BeautifulSoup and Requests python libraries to webscrape the UC Davis dining commons menus. By inputting what the user had at the dining commons, the program returns how many calories the user
consumed, as well as the number of grams of fat, carbohydrates, and protein.

## Installation
1. Type `pip install bs4` to install the BeautifulSoup library
2. Type `pip install requests` to install the Requests library

## Usage
1. Run the python script
2. Type the appropriate answers to each prompt
3. Type "done" when you are done inputting your meals

## Example Input
`tercero`</br>
`monday`</br>
`lunch`</br>
`5 2`</br>
`16 1`</br>
`done`

## Limitations
- This program only applies to UC Davis
- Some menu options have nutrient values of "N/A" and cannot be included in the calculations
- This program does not work when school is not in session because the menus are empty at those times
