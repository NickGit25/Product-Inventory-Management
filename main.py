import streamlit as st

st.title("Smart Inventory Tracker")

st.write("Python inventory management application that tracks product quantity, and restocks as needed.")

st.text_area()

class Product: 
    def __init__(self, name, quantity, category ="unknown"):
        self.category = category
        self.name = name
        self.quantity = quantity

inventory_list = [
    Product("Nike Airforce 1", 25, "apparel"),
    Product("Small picture frame", 38, "decoration"),
    Product("Mini ipad", 40, "technology")
]

def search_name(name):
    for product in inventory_list:
        if product.name == name:
            return product


