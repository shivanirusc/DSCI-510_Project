import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Define the text data
submission_text = """
<h1><b>DSCI 510: Spring 2024 Final Project Submission</b></h1>
"""
# Define the text with increased font size
team_member_text = """
### **Name: Shivani Rajesh Shinde**  
"""

explanation_text = """
#### **1. An explanation of how to use my webapp:**  
This project requires the following packages:
- numpy, pandas, streamlit, requests, re (Python RegEx), and beautifulsoup (python version: 3.11.5)  
To visualize this project, ensure that the required packages mentioned above are installed. Next, clone the repository from the following [GitHub Repository](https://github.com/shivanirusc/DSCI-510_Project). Once the repository is cloned, execute this notebook to visualize the project.  
You can use `allrecipe_scrapper.py`, `epicurious_data.py`, and `spoonacular_data.py` added separately to the GitHub repository to check their functions and scrap all data, or alternatively, you can directly use the CSV dataset stored in `updated_recipe_data.csv` to test the results.

#### **2. Any major “gotchas” to the code?**
The API key utilized to access the Spoonacular API is unique to my account. Therefore, if someone wishes to use this program, they must generate their own Rapid API Key. The link to obtain the key is provided: [RapidAPI](https://rapidapi.com/spoonacular/api/recipe-food-nutrition). Please note that the free version of the API allows only 50 requests.  
The scope of the research is currently limited to examining health conditions such as High and Low Blood Pressure, Diabetes, or Low-calorie diets. However, there is potential to expand the research by including additional health issues for more comprehensive results.  
As you progress through the app, I have provided clear instructions for interactive use by the grader.

#### **3. What did you set out to study?**
The primary focus of my research was:  
- Providing recipe recommendations tailored to the user's desired food preferences while accommodating any dietary restrictions they may have.  
- Ensuring that users receive recipes suitable for their specific health conditions.  
I adhered to the original plan outlined in milestone 1 and successfully achieved the expected results.

#### **4. What did you Discover/what were your conclusions ?**

The dataset I utilized contains various attributes including Recipe names, Ingredients, Calcium, Calorie, Cholesterol, Dietary Fiber, Iron, Potassium, Protein, Saturated Fat, Sodium, Total Carbohydrate, Total Fat, and Vitamin C. Conducting research on nutritional aspects suitable for individuals with conditions such as High/Low Blood Pressure and Diabetes, or those seeking low-calorie options, I developed a web application.
Key features of the Recipe Finder web app include:

- Users can select their preferred key ingredient for cooking.
- The option to specify any allergens or ingredients they wish to avoid.
- Selection of dish types such as soup, drink, meal, or dessert.
- Choice of recipe categories: Vegetarian, Non-vegetarian, or Vegan.

Upon submission of these preferences, the app generates a list of 10 recipes along with their respective ingredients, providing users with cooking options tailored to their needs.

"""
# Render the text in Streamlit app
st.markdown(submission_text,unsafe_allow_html=True)
# Display the text with increased font size
st.markdown(team_member_text, unsafe_allow_html=True)
st.markdown(explanation_text, unsafe_allow_html=True)

# Load the CSV data
data = pd.read_csv("updated_recipe_data.csv")

# Define conditions
conditions = {
    "High Blood Pressure": data[data["Sodium"] < 150],
    "Diabetes": data[data["Total Carbohydrate"] < 30],
    "Low Calorie": data[data["Calorie"] < 100],
    "Low Blood Pressure": data[data["Cholesterol"] < 150]
}

# Count the number of recipes for each condition
recipe_counts = {condition: len(filtered_data) for condition, filtered_data in conditions.items()}

# Create a DataFrame from the recipe counts
recipe_counts_df = pd.DataFrame(list(recipe_counts.items()), columns=["Condition", "Recipe Count"])

# Plotly chart
fig = px.bar(recipe_counts_df, x="Condition", y="Recipe Count", title="Number of Recipes for Different Conditions")
fig.update_layout(xaxis_title="Condition", yaxis_title="Recipe Count")

# Display the chart
st.plotly_chart(fig)

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

# Function to create bar chart with custom styling
def custom_bar_chart(data_dict):
    for key, value in data_dict.items():
        st.write(f"### {key} condition:")
        # Define the CSS styling as a string
        custom_css = """
        <style>
        .stHorizontalBarChart > div > div > div > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(1) {
        background-color: #f0f0f0 !important;
        }
        .stHorizontalBarChart > div > div > div > div:nth-child(1) > div > div:nth-child(2) > div:nth-child(1) {
        background-color: #ffffff !important;
        }
        </style>
        """

        # Use the html component to inject the CSS styling
        st.html(custom_css)
        # Plot bar chart
        st.bar_chart(value)

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

    # Create data dictionary for bar chart
    data_dict = {category: count for category, count in zip(recipe_categories, recipe_counts)}

    # Plot bar chart with custom styling
    custom_bar_chart({condition: data_dict})
