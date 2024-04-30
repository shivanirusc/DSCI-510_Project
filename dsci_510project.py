import streamlit as st
import pandas as pd

# Load the data
data = pd.read_csv("updated_recipe_data.csv")

# Function to filter data based on user inputs
def filter_data(ingredients, category, health_condition, dietary_restriction, dietary_conditions, sweet_or_drink):
    filtered_data = data.copy()
    
    # Filter by ingredients
    if ingredients:
        filtered_data = filtered_data[filtered_data['Ingredients'].str.contains('|'.join(ingredients), case=False)]
    
    # Filter by recipe category
    if category:
        filtered_data = filtered_data[filtered_data['Recipe Category'].isin(category)]
    
    # Filter by health condition
    if health_condition:
        if health_condition == "High Blood Pressure":
            filtered_data = filtered_data[filtered_data["Sodium"] < 150]  # Adjust threshold as needed
        elif health_condition == "Diabetes":
            filtered_data = filtered_data[filtered_data["Total Carbohydrate"] < 30]  # Adjust threshold as needed
    
    # Filter by dietary restriction
    if dietary_restriction:
        if dietary_restriction == "Low Sodium":
            filtered_data = filtered_data[filtered_data["Sodium"] < 100]  # Adjust threshold as needed
        elif dietary_restriction == "Low Cholesterol":
            filtered_data = filtered_data[filtered_data["Cholesterol"] < 50]  # Adjust threshold as needed
    
    # Filter by dietary conditions
    if dietary_conditions:
        for condition in dietary_conditions:
            additional_ingredient = st.text_input(f"Enter additional ingredient for {condition}:", key=condition.lower())
            if additional_ingredient:
                filtered_data = filtered_data[filtered_data['Ingredients'].str.contains(additional_ingredient, case=False)]
    
    # Filter by sweet or drink
    if sweet_or_drink:
        if 'Sweet Dish' in sweet_or_drink:
            filtered_data = filtered_data[filtered_data['Ingredients'].str.contains('cup white sugar|cup brown sugar', case=False)]
        if 'Drink' in sweet_or_drink:
            filtered_data = filtered_data[filtered_data['Ingredients'].str.contains('fluid', case=False)]
    
    return filtered_data[['Recipe Name', 'Ingredients']]

# Sidebar inputs
st.sidebar.title("Filter Options")
ingredients = st.sidebar.text_input("Enter ingredients (comma-separated)", "")
category = st.sidebar.multiselect("Select recipe category", data['Recipe Category'].unique())
health_condition = st.sidebar.selectbox("Select health condition", ["High Blood Pressure", "Diabetes"])
dietary_restriction = st.sidebar.selectbox("Select dietary restriction", ["Low Sodium", "Low Cholesterol"])
dietary_conditions = st.sidebar.multiselect("Select dietary conditions", ["Diabetes", "Low Blood Pressure", "High Blood Pressure", "Other"])
sweet_or_drink = st.sidebar.multiselect("Select sweet or drink", ["Sweet Dish", "Drink"])

# Filter button
if st.sidebar.button("Submit"):
    filtered_data = filter_data(ingredients.split(','), category, health_condition, dietary_restriction, dietary_conditions, sweet_or_drink)
    st.table(filtered_data)
