import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("updated_recipe_data.csv")

# Filter data for High Blood Pressure condition and selected categories
condition = "High Blood Pressure"
categories = ["Vegetarian", "Non-vegetarian", "Vegan"]
filtered_data = data[(data["Health Condition"] == condition) & (data["Recipe Category"].isin(categories))]

# Count recipes for each category
recipe_counts = filtered_data["Recipe Category"].value_counts()

# Draw pie plot
fig, ax = plt.subplots()
ax.pie(recipe_counts, labels=recipe_counts.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the plot
st.pyplot(fig)

