import pandas as pd
import streamlit as st

# Function to parse genre string
def parse_genre_string(genre_string):
    # Remove the leading and trailing square brackets
    genre_string = genre_string.strip('[]')
    # Remove any single quotes from the string
    genre_string = genre_string.replace("'", "")
    # Remove any leading or trailing whitespace
    genre_string = genre_string.strip()
    # Split the string by comma and space to get individual genres
    genres_list = genre_string.split(", ")
    return genres_list

# Function to process user inputs and return matching book titles
def book_response(df, user_inputs):
    user_inputs = [input.lower() for input in user_inputs]
    list_of_titles = []

    for index, row in df.iterrows():
        row_genres = parse_genre_string(row['genres'])  # Parse genres for the current row
        for user_input in user_inputs:
            if any(user_input in genre for genre in row_genres):
                list_of_titles.append(row['title'])
                break  # Break the inner loop if a match is found for current user input

    return list_of_titles[:10]  # Return only the top 10 matching titles

# Load the dataset
df = pd.read_csv('book_and_genres(1).csv')

# Streamlit UI
st.title('Book Recommendation System')

# Sidebar for user input
user_inputs = st.sidebar.text_input("Enter genres (comma-separated):")
if user_inputs:
    user_inputs = user_inputs.split(',')
    matching_titles = book_response(df, user_inputs)
    st.subheader("Recommended Books:")
    for title in matching_titles:
        st.write(title)
