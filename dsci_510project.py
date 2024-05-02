import streamlit as st
import pandas as pd
import numpy as np

# Load the data
data = pd.read_csv("updated_recipe_data.csv")

# Function to classify recipe categories
def classify_recipe(row):
    if 'soup' in row['Recipe Name'].lower():
        return 'Soup'
    elif 'salad' in row['Recipe Name'].lower():
        return 'Salad'
    elif 'cup white sugar' in row['Ingredients'].lower() or 'cup brown sugar' in row['Ingredients'].lower():
        return 'Sweet Dish'
    elif 'fluid' in row['Ingredients'].lower():
        return 'Drink'
    else:
        return 'Meal'

# Function to filter data based on user inputs
def filter_data(ingredient, category, health_conditions, sweet_or_drink, allergy_ingredients):
    filtered_data = data.copy()
    
    # Filter by ingredient
    if ingredient:
        filtered_data = filtered_data[filtered_data['Ingredients'].str.contains(f"\\b{ingredient}\\b", case=False, regex=True)]
    
    # Filter out recipes containing allergy ingredients
    if allergy_ingredients:
        for allergen in allergy_ingredients:
            filtered_data = filtered_data[~filtered_data['Ingredients'].str.contains(allergen.strip(), case=False)]
    
    # Filter by recipe category
    if category:
        filtered_data = filtered_data[filtered_data["Recipe Category"].isin(category)]
    
    # Filter by health conditions
    if health_conditions:
        for condition in health_conditions:
            if condition == "High Blood Pressure":
                filtered_data = filtered_data[filtered_data["Sodium"] < 150]  # Adjust threshold as needed
            elif condition == "Diabetes":
                filtered_data = filtered_data[filtered_data["Total Carbohydrate"] < 30]  # Adjust threshold as needed
            elif condition == "Low Calorie":
                filtered_data = filtered_data[filtered_data["Calorie"] < 100]  # Adjust threshold as needed
    
    # Filter by sweet or drink or soup or meal
    if sweet_or_drink:
        filtered_data = filtered_data[filtered_data.apply(classify_recipe, axis=1).isin(sweet_or_drink)]
    
    return filtered_data[['Recipe Name', 'Ingredients']]

# Load background image
background_image = 'https://i.imgur.com/AUtA6b0.jpeg'

# Display background image
st.image(background_image, use_column_width=True)

st.title("Recipe Filter")

st.subheader("Enter Your Preferences")

# Input fields
ingredient = st.text_input("Enter an ingredient", "")
allergy_ingredients = st.text_input("Enter allergy or restricted ingredients (comma-separated)", "")
allergy_ingredients_list = [ingredient.strip() for ingredient in allergy_ingredients.split(',')]
category = st.multiselect("Select recipe category", ["Vegetarian", "Non-Vegetarian", "Vegan"])
health_conditions = st.multiselect("Select health conditions", ["Diabetes", "Low Blood Pressure", "High Blood Pressure", "Low Calorie"])
sweet_or_drink = st.multiselect("Select sweet or drink or soup or meal", ["Sweet Dish", "Drink", "Meal", "Soup"])

# Filter button
if st.button("Find Recipes"):
    st.subheader("Filtered Recipes")
    filtered_data = filter_data(ingredient, category, health_conditions, sweet_or_drink, allergy_ingredients_list)
    if filtered_data.empty:
        st.write("No recipes found matching the criteria.")
    else:
        st.table(filtered_data)

# Conditions
conditions = {
    "High Blood Pressure": "Sodium < 150",
    "Diabetes": "Total Carbohydrate < 30",
    "Low Calorie": "Calorie < 100",
    "Low Blood Pressure": "Cholesterol < 150"
}

# Plot bar charts for each condition
for condition, filter_condition in conditions.items():
    # Filter data based on condition
    if condition == "High Blood Pressure":
        filtered_data = data[data["Sodium"] < 150]
    elif condition == "Diabetes":
        filtered_data = data[data["Total Carbohydrate"] < 30]
    elif condition == "Low Calorie":
        filtered_data = data[data["Calorie"] < 100]
    elif condition == "Low Blood Pressure":
        filtered_data = data[data["Cholesterol"] < 150]

    # Count recipes for each category
    recipe_categories = filtered_data["Recipe Category"].unique()
    recipe_counts = np.zeros(len(recipe_categories))
    for i, category in enumerate(recipe_categories):
        recipe_counts[i] = filtered_data[filtered_data["Recipe Category"] == category].shape[0]

    # Plot bar chart
    st.write(f"Recipes for {condition} condition:")
    st.bar_chart({recipe_categories[i]: recipe_counts[i] for i in range(len(recipe_categories))})
