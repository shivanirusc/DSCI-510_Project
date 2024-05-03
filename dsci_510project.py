import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
import urllib.request

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
- numpy, pandas, streamlit, requests, re (Python RegEx), plotly, matplotlib, seaborn and beautifulsoup (python version: 3.11.5)  
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

graph_one = """
##### **1. Number of Recipes for Different Conditions**

The plot visualizes the number of recipes available for different health conditions, providing insights into the distribution of recipes based on specific health criteria. 
"""
st.markdown(graph_one, unsafe_allow_html=True)


# Define conditions
conditions = {
    "High Blood Pressure": data[data["Sodium"] < 150],
    "Diabetes": data[data["Total Carbohydrate"] < 30],
    "Low Calorie": data[data["Calorie"] < 100],
    "Low Blood Pressure": data[data["Cholesterol"] < 150]
}

# Count the number of recipes for each condition
recipe_counts = {condition: len(filtered_data) for condition, filtered_data in conditions.items()}

# Extract conditions and counts
conditions = list(recipe_counts.keys())
recipe_counts = list(recipe_counts.values())

# Define colors for each condition
colors = ["skyblue", "salmon", "lightgreen", "orange"]  # You can define custom colors if needed

# Plot
with st.markdown("### Number of Recipes for Different Health Conditions"):
    fig, ax = plt.subplots()
    ax.bar(conditions, recipe_counts, color=colors, edgecolor="black")
    ax.set_xlabel("Health Condition")
    ax.set_ylabel("Number of Recipes")
    ax.set_title(" ")
    st.pyplot(fig)

st.markdown("""
##### 2. Recipe categories based on Health conditions 
This plot consists of four bar charts, each representing the number of recipes recommended for a specific health condition:

- **High Blood Pressure:** The first bar chart shows the number of recipes recommended for individuals with high blood pressure.
- **Diabetes:** The second bar chart illustrates the number of recipes suitable for individuals with diabetes.
- **Low Calorie:** The third bar chart depicts the count of recipes ideal for individuals on a low-calorie diet.
- **Low Blood Pressure:** Finally, the fourth bar chart shows the number of recipes recommended for individuals with low blood pressure.

Each bar's height represents the number of recipes available in the respective category, providing a visual comparison of recipe availability tailored to different health conditions. The x-axis labels are rotated vertically for better readability, and the chart title specifies the health condition being considered.
""")

# Conditions
conditions = {
    "High Blood Pressure": "Sodium < 150",
    "Diabetes": "Total Carbohydrate < 30",
    "Low Calorie": "Calorie < 100",
    "Low Blood Pressure": "Cholesterol < 150"
}

# Define colors for bars
colors = ['skyblue', 'salmon', 'lightgreen', 'lightcoral']

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

    # Plot bar chart with custom styling
    with st.markdown(f"### Recipes for {condition} condition"):
        fig, ax = plt.subplots()
        ax.bar(recipe_categories, recipe_counts, color=colors, edgecolor='black')
        ax.set_ylabel("Recipe Count")
        ax.set_xlabel("Recipe Category")
        ax.set_title(f"Recipes for {condition} condition")
        ax.tick_params(axis='x', rotation=360)  # Rotate x-axis labels vertically
        st.pyplot(fig)

st.markdown("""
##### Recipe Filter
Please click the button below to explore the live demonstration of the web app.

Instructions for using the app:

- Enter the key ingredient you wish to search recipes for.
- If there are any ingredients you wish to avoid, enter them in the respective field. If there are no restricted ingredients, simply enter "None".
- Select the recipe category.
- Choose any relevant health conditions.
- Select the type of meal.
- Click the submit button to view the results.""")

# Button to open the recipe filter app
if st.button("Open Recipe Filter App"):
    st.markdown("Loading...")

    # Import the Streamlit app file from GitHub
    url = "https://raw.githubusercontent.com/shivanirusc/DSCI-510_Project/main/recipe_filter_app.py"
    response = urllib.request.urlopen(url)
    code = response.read().decode()

    # Execute the code
    exec(code)

st.markdown("""
#### **5. Difficulties Encountered in Completing the Project**

I didn't encounter any specific difficulties in completing the project. However, I can imagine that some potential challenges might arise when dealing with data preprocessing, especially if the dataset is large or messy. Additionally, ensuring the accuracy and effectiveness of the filtering conditions for different health conditions could require some trial and error. Finally, integrating and deploying the Streamlit app might pose some challenges, especially if there are compatibility issues or if additional configurations are needed.
"""
