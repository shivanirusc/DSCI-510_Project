import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

# Add sidebar menu for navigation
menu = ["Main", "Recipe Finder", "Dataset Description"]  # Add "Dataset Description" option
choice = st.sidebar.selectbox("Go to", menu)

# Define function for the Dataset Description tab
def dataset_description():
    st.title("Dataset Description")
    st.write("""
    The data.csv file contains a comprehensive dataset of recipes along with various nutritional attributes and the recipe category. Here's a brief description of the columns:
    
    - Recipe Name: This column stores the names of the recipes included in the dataset. It serves as the primary identifier for each recipe.
    - Ingredients: This column lists the ingredients required to prepare each recipe. It provides insights into the components used in the recipe, allowing users to identify specific ingredients and dietary preferences.
    - Calcium: This attribute represents the calcium content present in each recipe. Calcium is an essential mineral for bone health and various bodily functions, and its presence in recipes is crucial for individuals looking to maintain adequate calcium intake.
    - Calorie: The calorie column indicates the calorie content of each recipe. Calories are a measure of the energy provided by food and are important for individuals monitoring their daily calorie intake for weight management or health reasons.
    - Cholesterol: This column denotes the cholesterol content in each recipe. Monitoring cholesterol intake is vital for individuals managing cholesterol levels to reduce the risk of heart disease and other cardiovascular conditions.
    - Dietary Fiber: Dietary fiber is essential for digestive health and helps regulate bowel movements, reduce cholesterol levels, and control blood sugar levels. This column provides information on the dietary fiber content present in each recipe.
    - Iron: Iron is a crucial mineral necessary for the formation of hemoglobin, which carries oxygen in the blood. The iron content in recipes is essential for individuals, particularly those at risk of iron deficiency or anemia.
    - Potassium: Potassium plays a vital role in maintaining fluid balance, muscle contractions, and nerve signals. The potassium content in recipes is important for individuals seeking to maintain healthy blood pressure and overall cardiovascular health.
    - Protein: Protein is an essential macronutrient that plays a key role in building and repairing tissues, supporting immune function, and providing energy. The protein content in recipes is valuable for individuals, especially those following specific dietary plans or seeking to meet protein requirements.
    - Saturated Fat: Saturated fat is a type of fat found in various foods, and excessive consumption can contribute to heart disease and other health issues. Monitoring saturated fat intake is crucial for individuals aiming to maintain heart health and overall well-being.
    - Sodium: Sodium is a mineral that regulates fluid balance and nerve function but excessive intake can lead to high blood pressure and other health problems. The sodium content in recipes is significant for individuals monitoring their sodium intake for heart health and blood pressure management.
    - Total Carbohydrate: Carbohydrates are the body's primary source of energy, and monitoring carbohydrate intake is essential for individuals managing blood sugar levels or following specific dietary plans.
    - Total Fat: Fat is an essential macronutrient that provides energy, supports cell growth, and helps absorb certain vitamins. The total fat content in recipes is valuable for individuals aiming to maintain a balanced diet and manage fat intake for overall health.
    - Vitamin C: Vitamin C is an antioxidant that supports immune function, collagen synthesis, and wound healing. The presence of vitamin C in recipes is beneficial for individuals seeking to boost their immune system and overall health.
    - Recipe Category: This column categorizes each recipe as vegetarian, non-vegetarian, or vegan. It provides insights into the dietary preferences and restrictions associated with each recipe, allowing users to filter recipes based on their dietary choices.
    """)
    st.markdown("""
    - **DATA SOURCE 1:**
    Dataset name: Epicurious - Recipes with Rating and Nutrition

    URL for website or API: https://www.kaggle.com/datasets/hugodarwood/epirecipes/data

    **Brief description of data/API:**

    The Epicurious dataset contains a collection of recipes along with their ratings and nutrition information. It includes details such as recipe titles, ingredients, preparation methods, cooking time, ratings, and nutritional content. This dataset is suitable for various culinary analyses, recipe recommendation systems, and nutritional studies.

    - **DATA SOURCE 2:**
    **API: Spoonacular API**

    URL for API documentation: https://spoonacular.com/food-api/docs

    **Brief description:**

    The Spoonacular API provides access to a range of food-related data, including ingredients, nutrition information, and more. It offers endpoints for searching and retrieving recipe information, analyzing recipes for nutrition. The API covers a wide variety of cuisines and dietary preferences, making it suitable for various food-related applications and analysis.

    - **DATA SOURCE 3:**

    URL for website to scrape or download: https://www.allrecipes.com/search

    **Brief description:**

    The website https://www.allrecipes.com/search provides a search interface for finding recipes. Users can search for recipes based on various criteria such as ingredients, dish type, nutritional values, and more. Each recipe listing typically includes the recipe name, ingredients, cooking instructions, user ratings, and sometimes nutritional information. The data available on this website represents a wide range of recipes contributed by users. It contains information about the ingredients required, the steps to prepare the dish and the nutritional values associated with every dish.
    """) 

if choice == "Main":
  # Define the text data
  submission_text = """
  <h1><b>DSCI 510: Spring 2024 Final Project Submission</b></h1>
  """
  # Define the text with increased font size for team member details
  team_member_text = """
  ### **Name: Shivani Rajesh Shinde**  
  """

  # Explanation of how to use the web app
  explanation_text = """
  #### **1. An explanation of how to use my webapp:**  
  This project requires the following packages:
  - numpy, pandas, streamlit, requests, re (Python RegEx), plotly, matplotlib, JSON and beautifulsoup (python version: 3.11.5)  
  To visualize this project, ensure that the required packages mentioned above are installed. Next, clone the repository from the following [GitHub Repository](https://github.com/shivanirusc/DSCI-510_Project). Once the repository is cloned, execute this notebook to visualize the project.  
  You can use `allrecipe_scrapper.py`, `epicurious_data.py`, and `spoonacular_data.py` added separately to the GitHub repository to check their functions and scrap all data, or alternatively, you can directly use the CSV dataset stored in `updated_recipe_data.csv` to test the results.
  If you want to generate the datset form the python file
  - Firstly execute allrecipe_scrapper.py it will generate recipes csv file. 
  - Use this csv file and execute epicurious_data.py. It will applend the extracted data to the csv file
  - Finally execute spoonacular_data.py upload the recipes csv file and the code will append results to this file and give use final csv file that can be used for running the webapp.
  #### **2. Any major “gotchas” to the code?**
  The API key utilized to access the Spoonacular API is unique to my account. Therefore, if someone wishes to use this program, they must generate their own Rapid API Key. The link to obtain the key is provided: [RapidAPI](https://rapidapi.com/spoonacular/api/recipe-food-nutrition). Please note that the free version of the API allows only 50 requests.  
  The scope of the research is currently limited to examining health conditions such as High and Low Blood Pressure, Diabetes, or Low-calorie diets. However, there is potential to expand the research by including additional health issues for more comprehensive results.  
  As you progress through the app, I have provided clear instructions for interactive use by the grader.

  # Explanation for the Recipe Filter section
  st.markdown("""
  ##### Recipe Filter

  Instructions for using the app:

  - Enter the key ingredient you wish to search recipes for.
  - If there are any ingredients you wish to avoid, enter them in the respective field. If there are no restricted ingredients, simply enter "None".
  - Select the recipe category.
  - Choose any relevant health conditions.
  - Select the type of meal.
  - Click the submit button to view the results.

  ###### Click on Recipe Finder to open the app or you can Navigate to the Recipe Finder app using slider navigation bar""")

  # Add a hyperlink to open the new app in a new page
  st.markdown("[Recipe Finder](https://recipefilterapp.streamlit.app/)", unsafe_allow_html=True)
  
  #### **3. What did you set out to study?**
  The primary focus of my research was:  
  - Providing recipe recommendations tailored to the user desired food preferences while accommodating any dietary restrictions they may have.  
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
  st.markdown(submission_text, unsafe_allow_html=True)
  # Display the text with increased font size for team member details
  st.markdown(team_member_text, unsafe_allow_html=True)
  # Explanation of how to use the web app
  st.markdown(explanation_text, unsafe_allow_html=True)

  # Load the CSV data
  data = pd.read_csv("updated_recipe_data.csv")

  # Explanation text for the first graph
  graph_one = """
  ##### **1. Number of Recipes for Different Conditions**

  The plot visualizes the number of recipes available for different health conditions, providing insights into the distribution of recipes based on specific health criteria. 
  """
  st.markdown(graph_one, unsafe_allow_html=True)

  # Define conditions and filter the data accordingly
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
  colors = ["skyblue", "salmon", "lightgreen", "orange"]  

  # Plot the bar chart
  with st.markdown("### Number of Recipes for Different Health Conditions"):
      fig, ax = plt.subplots()
      ax.bar(conditions, recipe_counts, color=colors, edgecolor="black")
      ax.set_xlabel("Health Condition")
      ax.set_ylabel("Number of Recipes")
      ax.set_title(" ")
      st.pyplot(fig)

  # Explanation text for the second graph
  st.markdown("""
  ##### 2. Recipe categories based on Health conditions 
  This plot consists of four bar charts, each representing the number of recipes recommended for a specific health condition:

  - **High Blood Pressure:** The first bar chart shows the number of recipes recommended for individuals with high blood pressure.
  - **Diabetes:** The second bar chart illustrates the number of recipes suitable for individuals with diabetes.
  - **Low Calorie:** The third bar chart depicts the count of recipes ideal for individuals on a low-calorie diet.
  - **Low Blood Pressure:** Finally, the fourth bar chart shows the number of recipes recommended for individuals with low blood pressure.

  Each bars height represents the number of recipes available in the respective category, providing a visual comparison of recipe availability tailored to different health conditions. The x-axis labels are rotated vertically for better readability, and the chart title specifies the health condition being considered.
  """)

  # Conditions for the second graph
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
          ax.tick_params(axis='x', rotation=360)  
          st.pyplot(fig)

  # Additional text regarding difficulties encountered and future expansions
  st.markdown("""
  #### **5. Difficulties Encountered in Completing the Project**

  I did not encounter any specific difficulties in completing the project. However, I can imagine that some potential challenges might arise when dealing with data preprocessing, especially if the dataset is large or messy. Additionally, ensuring the accuracy and effectiveness of the filtering conditions for different health conditions could require some trial and error. Finally, integrating and deploying the Streamlit app might pose some challenges, especially if there are compatibility issues or if additional configurations are needed.

  #### **6. What skills did you wish you had while you were doing the project?**

  Having a better understanding of deployment techniques and DevOps practices could have helped streamline the deployment process of the Streamlit app and manage any infrastructure-related challenges more efficiently. Additionally, improving my proficiency in matplotlib would have been beneficial, as I found it time-consuming to arrange plot elements, especially when dealing with subplots. With more experience, I could have created plots more effectively and efficiently.

  #### **7. What would you do “next” to expand or augment the project?**

  - Expanding the range of health conditions included in the filtering criteria to provide users with a more comprehensive selection of dietary options tailored to various health concerns.
  - Implementing a multi-parameter approach to health condition filtering, allowing users to specify different health metrics such as total fats, sugar content, cholesterol levels, and more to refine their recipe search results.
  - Enabling users to include multiple key ingredients in their filtering criteria, enhancing the versatility of the search functionality and accommodating a wider range of culinary preferences and dietary needs.
  """) 
elif choice == "Recipe Finder":
    # Load data
    data = pd.read_csv("updated_recipe_data.csv")

    # Set the title of the Streamlit app
    st.title("Recipe Filter")

    # Function to classify recipe categories
    def classify_recipe(row):
        # Check if the recipe name contains keywords to classify it into a category
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
        # Make a copy of the original data
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

    # Section for user input
    st.subheader("Enter Your Preferences")

    # Input fields for user preferences
    ingredient = st.text_input("Enter an ingredient", "")
    allergy_ingredients = st.text_input("Enter allergy or restricted ingredients (Enter None if no restricted ingredients)", "")
    allergy_ingredients_list = [ingredient.strip() for ingredient in allergy_ingredients.split(',')]
    category = st.multiselect("Select recipe category", ["Vegetarian", "Non-Vegetarian", "Vegan"])
    health_conditions = st.multiselect("Select health conditions", ["Diabetes", "Low Blood Pressure", "High Blood Pressure", "Low Calorie"])
    sweet_or_drink = st.multiselect("Select Meal Type", ["Sweet Dish", "Drink", "Meal", "Soup"])

    # Button to trigger filtering of recipes
    if st.button("Find Recipes"):
        st.subheader("Filtered Recipes")
        # Filter the data based on user preferences
        filtered_data = filter_data(ingredient, category, health_conditions, sweet_or_drink, allergy_ingredients_list)
        # Display the filtered recipes in a table format
        if filtered_data.empty:
            st.write("No recipes found matching the criteria.")
        else:
            # Restrict the resulting recipes to 10
            filtered_data = filtered_data.head(10)
            st.table(filtered_data) 
elif choice == "Dataset Description":
    dataset_description()  # Call the function for the "Dataset Description" tab
