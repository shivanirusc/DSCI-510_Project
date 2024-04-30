import streamlit as st
import pandas as pd

# Load the data
data = pd.read_csv("updated_recipe_data.csv")

# Function to classify recipe categories
def classify_recipe(row):
    if 'soup' in row['Recipe Name'].lower():
        return 'Soup'
    elif 'salad' in row['Recipe Name'].lower():
        return 'Salad'
    elif row['Ingredients'].lower().find('cup white sugar') != -1 or row['Ingredients'].lower().find('cup brown sugar') != -1:
        return 'Sweet Dish'
    elif row['Ingredients'].lower().find('fluid') != -1:
        return 'Drink'
    else:
        return 'Meal'

# Function to filter data based on user inputs
def filter_data(ingredients, category, health_conditions, sweet_or_drink, allergy_ingredients):
    filtered_data = data.copy()
    
    # Filter by ingredients
    for ingredient in ingredients:
        filtered_data = filtered_data[filtered_data['Ingredients'].str.contains(ingredient, case=False)]
    
    # Filter out recipes containing allergy ingredients
    if allergy_ingredients:
        for allergen in allergy_ingredients:
            filtered_data = filtered_data[~filtered_data['Ingredients'].str.contains(allergen, case=False)]
    
    # Filter by recipe category
    if category:
        filtered_data = filtered_data[filtered_data['Recipe Category'].isin(category)]
    
    # Filter by health conditions
    if health_conditions:
        for condition in health_conditions:
            if condition == "High Blood Pressure":
                filtered_data = filtered_data[filtered_data["Sodium"] < 150]  # Adjust threshold as needed
            elif condition == "Diabetes":
                filtered_data = filtered_data[filtered_data["Total Carbohydrate"] < 30]  # Adjust threshold as needed
            elif condition == "Low Calorie":
                filtered_data = filtered_data[filtered_data["Calorie"] < 100]  # Adjust threshold as needed
    
    # Filter by sweet or drink
    if sweet_or_drink:
        if 'Sweet Dish' in sweet_or_drink:
            filtered_data = filtered_data[filtered_data['Recipe Category'] == 'Sweet Dish']
        if 'Drink' in sweet_or_drink:
            filtered_data = filtered_data[filtered_data['Recipe Category'] == 'Drink']
        if 'Meal' in sweet_or_drink:
            filtered_data = filtered_data[filtered_data['Recipe Category'] == 'Meal']
        if 'Soup' in sweet_or_drink:
            filtered_data = filtered_data[filtered_data['Recipe Category'] == 'Soup']
        if 'Salad' in sweet_or_drink:
            filtered_data = filtered_data[filtered_data['Recipe Category'] == 'Salad']
    
    return filtered_data[['Recipe Name', 'Ingredients']]

# Main screen inputs
st.title("Recipe Filter")

ingredients = st.text_input("Enter ingredients (comma-separated)", "")
ingredients_list = [ingredient.strip() for ingredient in ingredients.split(',')]

allergy_ingredients = st.text_input("Enter allergy or restricted ingredients (comma-separated)", "")
allergy_ingredients_list = [ingredient.strip() for ingredient in allergy_ingredients.split(',')]

category = st.multiselect("Select recipe category", ["Vegetarian", "Non-Vegetarian", "Vegan"])
health_conditions = st.multiselect("Select health conditions", ["Diabetes", "Low Blood Pressure", "High Blood Pressure", "Low Calorie"])
sweet_or_drink = st.multiselect("Select sweet or drink", ["Sweet Dish", "Drink", "Meal", "Soup", "Salad"])

# Filter button
if st.button("Submit"):
    filtered_data = filter_data(ingredients_list, category, health_conditions, sweet_or_drink, allergy_ingredients_list)
    st.table(filtered_data)
