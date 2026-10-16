import streamlit as st
from inventory import inventory_list

def search_name(name):
    for product in inventory_list:
        if product.name.lower() == name.lower():
            return product
    return False

class Product: 
    def __init__(self, name, quantity, category ="Unknown"):
        self.category = category
        self.name = name
        self.quantity = quantity

    def format(self):
        new_name = []
        format_name = self.name.split(" ")
        for word in format_name:
            format_word = word[0].upper() + word[1:]
            new_name.append(format_word)
        self.name = " ".join(new_name)
        self.category = self.category[0].upper() + self.category[1:]

