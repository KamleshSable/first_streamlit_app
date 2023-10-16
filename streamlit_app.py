import streamlit

streamlit.title('My Parents New Healthy Diner')


streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 and Blueberry oatmeal')
streamlit.text('🥗 Kale , Spinach and Rocket Smoothie')
streamlit.text('🐔 Hard Boiled Free-Range Egg') 
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# lets put a list here so they can pick the fruit they want to include
fruit_selected = streamlit.multiselect("Pick Some fruits:" , list(my_fruit_list.index),['Avocado' , 'Strawberries'])
fruit_to_show = my_fruit_list.loc[fruit_selected]


# display the table on the page 
streamlit.dataframe(fruit_to_show)
