import streamlit as st

class Product: 
    def __init__(self, name, quantity, category ="Unknown"):
        self.category = category
        self.name = name
        self.quantity = quantity

    def edit_quantity(self):
        if st.session_state.show:
            st.write("Edit quantity")
            edit_amount = st.number_input(
            "Amount", 
            min_value=0, 
            step = 1,
            key = f"quantity_{self.name}",
            value = self.quantity,
            on_change = self.delete_interface
            )
        

    def delete_interface(self):
        self.quantity = st.session_state[f"quantity_{self.name}"]
        st.session_state.show = False
            

# 


