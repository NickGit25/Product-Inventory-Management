import streamlit as st
from inventory_list import inventory_list, Product

def format_product(name, category):
        new_name = []
        format_name = name.split(" ")
        for word in format_name:
            format_word = word[0].upper() + word[1:]
            new_name.append(format_word)
        name = " ".join(new_name)
        category = category[0].upper() + category[1:]
        return (name, category)

def show_list(inventory_list):
   product_dict = []
   for item in inventory_list:
      print(item)

      product_dict.append({"Item" : item.name, "Count" : int(item.quantity), "Category" : item.category})
   st.table(product_dict)  


def add_product(name, quantity, category):
    if quantity <= 0:
        st.warning("Quantity can't be 0")
    else:
        name, category = format_product(name, category)
        inventory_list.append(Product(name, quantity, category))
        st.success("Product added successfully!")

def search_name(name):
    for product in inventory_list:
        if product.name.lower() == name.lower():
            return product
    return False

