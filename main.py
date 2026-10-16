import streamlit as st
from product_class import search_name, Product
from inventory import inventory_list

st.title("Smart Inventory Tracker")

st.write("Python inventory management application that tracks product quantity, and restocks as needed.")

search_bar = st.text_input("", placeholder="Search")

if search_bar:
    result = search_name(search_bar)

    if result:
        st.write("Category: ", result.category) 
        st.write(" Item: ", result.name)
        st.write(" Stock: ", result.quantity)
    else: 
        st.warning("Product not found.")


product_header = st.header("Add a Product")

product_name = st.text_input("Item").lower()
product_quantity = st.number_input("Stock", placeholder = "0")
product_category = st.text_input("Category").lower()

add_button = st.button("Add Product")

view_inventory = st.button("View Inventory")

if add_button:
    if product_name and product_quantity and product_category:
        if product_quantity <= 0:
            st.warning("Quantity can't be 0")
        else:
            inventory_list.append(Product(product_name, product_quantity, product_category).format())
            st.success("Product added successfully!")
    else:
        st.warning("Credentials invalid")



    






