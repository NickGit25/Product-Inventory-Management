import streamlit as st
from functions import search_name, show_list, add_product, format_product
from inventory_list import inventory_list
from product_class import Product

def close_list():
    st.session_state.view = False
    st.write("The three")

st.title("Smart Inventory Tracker")

st.write("Python inventory management application that tracks product quantity, and restocks as needed.")

search_bar = st.text_input("", placeholder="Search")

if search_bar:
    result = search_name(search_bar)

    product_info = st.empty()

    if result:

        if "editing" not in st.session_state:
            st.session_state.editing = False

        if "show" not in st.session_state:
            st.session_state.show = True

        
        if st.button("Edit Count"):
            st.session_state.editing = True
            st.session_state.show = True

        if st.session_state.editing:
            result.edit_quantity()
            

        with product_info.container():
            st.write("Category: ", result.category) 
            st.write(" Item: ", result.name)
            st.write(" Stock: ", result.quantity)
    else: 
        st.warning("Product not found.")


product_header = st.header("Add a Product")

product_name = st.text_input("Item").lower()
product_quantity = st.number_input("Stock", placeholder = "0", step = 0)
product_category = st.text_input("Category").lower()

# product = Product(product_name, product_quantity, product_category)

add_button = st.button("Add Product")

view_inventory = st.button("View Inventory")

close_inventory = st.button("Close Inventory", on_click=close_list)


if "view" not in st.session_state:
    st.session_state.view = False

if view_inventory:
    st.session_state.view = True

if st.session_state.view:
    show_list(inventory_list)
    st.write("The one")

# if close_inventory:
#     close_list()
#     st.write("The two")

if add_button:
    if product_name and product_quantity and product_category:
        format_product(product_name, product_category)
        add_product(product_name, product_quantity, product_category)
    else:
        st.warning("Credentials invalid")



    






