# -*- coding: utf-8 -*-
"""spoonacular_data.py.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XXZI2YD10veOHo3J7Z2wavL6ofFjKLYW
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def extract_recipe_data(url):
  # Define query parameters for the complex search
  querystring = {
    "query": "pasta",
    "cuisine": "italian",
    "excludeCuisine": "greek",
    "diet": "vegetarian",
    "intolerances": "gluten",
    "equipment": "pan",
    "includeIngredients": "tomato,cheese",
    "excludeIngredients": "eggs",
    "type": "main course",
    "instructionsRequired": "true",
    "fillIngredients": "false",
    "addRecipeInformation": "true",
    "titleMatch": "Crock Pot",
    "maxReadyTime": "20",
    "ignorePantry": "true",
    "sort": "calories",
    "sortDirection": "asc",
    "minCarbs": "10",
    "maxCarbs": "100",
    "minProtein": "10",
    "maxProtein": "100",
    "minCalories": "50",
    "maxCalories": "800",
    "minFat": "10",
    "maxFat": "100",
    "minAlcohol": "0",
    "maxAlcohol": "100",
    "minCaffeine": "0",
    "maxCaffeine": "100",
    "minCopper": "0",
    "maxCopper": "100",
    "minCalcium": "0",
    "maxCalcium": "100",
    "minCholine": "0",
    "maxCholine": "100",
    "minCholesterol": "0",
    "maxCholesterol": "100",
    "minFluoride": "0",
    "maxFluoride": "100",
    "minSaturatedFat": "0",
    "maxSaturatedFat": "100",
    "minVitaminA": "0",
    "maxVitaminA": "100",
    "minVitaminC": "0",
    "maxVitaminC": "100",
    "minVitaminD": "0",
    "maxVitaminD": "100",
    "minVitaminE": "0",
    "maxVitaminE": "100",
    "minVitaminK": "0",
    "maxVitaminK": "100",
    "minVitaminB1": "0",
    "maxVitaminB1": "100",
    "minVitaminB2": "0",
    "maxVitaminB2": "100",
    "minVitaminB5": "0",
    "maxVitaminB5": "100",
    "minVitaminB3": "0",
    "maxVitaminB3": "100",
    "minVitaminB6": "0",
    "maxVitaminB6": "100",
    "minVitaminB12": "0",
    "maxVitaminB12": "100",
    "minFiber": "0",
    "maxFiber": "100",
    "minFolate": "0",
    "maxFolate": "100",
    "minFolicAcid": "0",
    "maxFolicAcid": "100",
    "minIodine": "0",
    "maxIodine": "100",
    "minIron": "0",
    "maxIron": "100",
    "minMagnesium": "0",
    "maxMagnesium": "100",
    "minManganese": "0",
    "maxManganese": "100",
    "minPhosphorus": "0",
    "maxPhosphorus": "100",
    "minPotassium": "0",
    "maxPotassium": "100",
    "minSelenium": "0",
    "maxSelenium": "100",
    "minSodium": "0",
    "maxSodium": "100",
    "minSugar": "0",
    "maxSugar": "100",
    "minZinc": "0",
    "maxZinc": "100",
    "offset": "0",
    "number": "10",
    "limitLicense": "false",
    "ranking": "2"
  }

  # Define headers for the request
  headers = {
    "X-RapidAPI-Key": "649fa95507mshbfc3619a5fd6d8ap161b2fjsnd47df8345004",
    "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
  }

  # Define the URL2
  url2 = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/479101/information"

  # Define headers
  headers2 = {
    "X-RapidAPI-Key": "649fa95507mshbfc3619a5fd6d8ap161b2fjsnd47df8345004",
    "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
  }

  # Make the GET request
  response2 = requests.get(url2, headers=headers2)

  # Check if the request was successful
  if response2.status_code == 200:
      # Extract JSON data
      json_data = response2.json()

      # Extract recipe name and ingredients
      recipe_name = json_data['title']
      ingredients_list = [ingredient['original'] for ingredient in json_data['extendedIngredients']]
      ingredients = ', '.join(ingredients_list)

  # Make the GET request
  response = requests.get(url, headers=headers, params=querystring)

  # Check if the request was successful
  if response.status_code == 200:
      # Extract JSON data
      json_data = response.json()

      # Check if the JSON data contains results
      if 'results' in json_data:
          recipes = []
          for result in json_data['results']:
              recipe_name = result['title']
              if 'nutrition' in result:
                  nutrition = result['nutrition']
                  # Extracting required nutrition data
                  nutrition_data = {
                    'Calcium': nutrition['nutrients'][7]['amount'],
                    'Calories': nutrition['nutrients'][0]['amount'],
                    'Cholesterol': nutrition['nutrients'][6]['amount'],
                    'Dietary Fiber': nutrition['nutrients'][3]['amount'],
                    'Iron': nutrition['nutrients'][4]['amount'],
                    'Potassium': nutrition['nutrients'][len(nutrition)- 5]['amount'],
                    'Protein': nutrition['nutrients'][1]['amount'],
                    'Saturated Fat': nutrition['nutrients'][11]['amount'],
                    'Sodium': nutrition['nutrients'][len(nutrition)-3]['amount'],
                    'Total Carbohydrate': nutrition['nutrients'][3]['amount'],
                    'Total Fat': nutrition['nutrients'][3]['amount'],
                    'Vitamin C': nutrition['nutrients'][13]['amount']
                  }
              else:
                nutrition_data = {
                    'Calcium': None,
                    'Calorie': None,
                    'Cholesterol': None,
                    'Dietary Fiber': None,
                    'Iron': None,
                    'Potassium': None,
                    'Protein': None,
                    'Saturated Fat': None,
                    'Sodium': None,
                    'Total Carbohydrate': None,
                    'Total Fat': None,
                    'Vitamin C': None,
                    'Calories': None
                }
          return {'Recipe Name': recipe_name, 'Ingredients': ingredients, **nutrition_data}
  return None

# Generate list of URLs with IDs ranging from 470000 to 470050
base_url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/"
urls = [base_url + str(i) + "/information" for i in range(470000, 470050)]

# List to store extracted data
all_recipes = []

# Loop over each URL
for url in urls:
    recipe_data = extract_recipe_data(url)
    if recipe_data:
        all_recipes.append(recipe_data)

# Create a DataFrame
df = pd.DataFrame(all_recipes)

# Append new data to existing data
new_updated_data = pd.concat([updated_data, df], ignore_index=True)

# Store updated DataFrame to CSV
new_updated_data.to_csv('recipe_data.csv', index=False)

# Display updated DataFrame
new_updated_data.tail()

recipe_data = pd.read_csv("recipe_data.csv")

# Function to determine recipe category based on ingredients
def determine_recipe_category(ingredients):
    if "milk" in ingredients.lower() and not any(item in ingredients.lower() for item in ["fish", "chicken", "beef", "meat", "eggs"]):
        return "Vegetarian"
    elif not any(item in ingredients.lower() for item in ["fish", "chicken", "beef", "eggs", "milk", "products", "meat"]):
        return "Vegan"
    else:
        return "Non-Vegetarian"

# Apply the function to create the new column
recipe_data["Recipe Category"] = recipe_data["Ingredients"].apply(determine_recipe_category)

# Save the updated DataFrame to a new CSV file
recipe_data.to_csv("updated_recipe_data.csv", index=False)

data = pd.read_csv("updated_recipe_data.csv")
df = pd.DataFrame(data)