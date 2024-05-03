# -*- coding: utf-8 -*-
"""epicurious_data.py.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mSCSyJkfdF__xJupgwlR36aAWw7xPlvy
"""

import json
import pandas as pd

# Load JSON data
with open("/content/full_format_recipes[1].json", "r") as file:
    data = json.load(file)

filtered_data = []
for recipe in data:
    if all(field in recipe for field in ["protein", "fat", "calories", "sodium"]):
      protein = recipe.get("protein")
      fat = recipe.get("fat")
      calories = recipe.get("calories")
      sodium = recipe.get("sodium")
      if protein is not None and fat is not None and calories is not None and sodium is not None:
        recipe_name = recipe.get("title", "")
        ingredients = ", ".join(recipe.get("ingredients", []))
        filtered_data.append({
            "Recipe Name": recipe_name,
            "Ingredients": ingredients,
            "Protein": protein,
            "Total Fat": fat,
            "Calorie": calories,
            "Sodium": sodium
        })

# Append new data to existing data
df_new_data = pd.DataFrame(filtered_data)
existing_data = pd.read_csv('recipe_data.csv')
updated_data = pd.concat([existing_data, df_new_data], ignore_index=True)
updated_data = updated_data.reindex(columns=existing_data.columns)
updated_data.to_csv('recipe_data.csv', index=False)
updated_data.tail()