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


# New section to display fruitvice api resource
streamlit.header("Fruityvice Fruit Advice!")


fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"kiwi")

# take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it the screen as a table
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The Fruit Load List Contains:")
streamlit.dataframe(my_data_rows)

# allow the end user to add a fruit to the list
add_my_fruit = requests.get("https://fruityvice.com/api/fruit/"+"jackfruit")
# take the json version of the response and normalize it
add_my_fruit_normalized = pandas.json_normalize(add_my_fruit.json())
streamlit.dataframe(add_my_fruit_normalized)
