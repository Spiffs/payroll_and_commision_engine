# calculator_logic.py

import streamlit as st

# --- Bonus Calculator Logic ---

def calculate_bonus_total(entries):
    """Calculates the total bonus from a list of amount/percentage dictionaries."""
    total = 0
    for entry in entries:
        amount = entry.get('amount', 0.0)
        percentage = entry.get('percentage', 0.0)
        # Ensure types are correct before calculation
        if isinstance(amount, (int, float)) and isinstance(percentage, (int, float)):
            total += amount * (percentage / 100.0)
    return total

def add_entry():
    """Adds a new row to the bonus entries session state."""
    # This function is called as an on_click callback from app.py
    st.session_state.bonus_entries.append({'amount': 0.0, 'percentage': 0.0})

def remove_entry(index):
    """Removes a specific row from the bonus entries session state."""
    # This function is called as an on_click callback from app.py
    if 0 <= index < len(st.session_state.bonus_entries):
        st.session_state.bonus_entries.pop(index)

# --- Standard Calculator Logic & Callbacks ---

def clear_calc():
    """Resets the standard calculator's session state."""
    # This function is called as an on_click callback from app.py
    st.session_state.calc_display = ""
    st.session_state.calc_history = 0
    st.session_state.calc_operation = None
    st.session_state.new_input = False

def input_number(value):
    """Handles number inputs for the standard calculator."""
    # This function is called as an on_click callback from app.py
    if st.session_state.new_input:
        st.session_state.calc_display = str(value)
        st.session_state.new_input = False
    else:
        if st.session_state.calc_display == "0" or st.session_state.calc_display == "":
            st.session_state.calc_display = str(value)
        else:
            st.session_state.calc_display += str(value)
    # Optional: Debug print retained from original
    # print(st.session_state.calc_display)

def handle_operation(operation):
    """Handles operation inputs (+, -, *, /) for the standard calculator."""
    # This function is called as an on_click callback from app.py
    if st.session_state.calc_display:
        if st.session_state.calc_operation and not st.session_state.new_input:
            # If an operation is already pending and user clicks another, calculate first
            calculate_result()
        
        try:
            st.session_state.calc_history = float(st.session_state.calc_display)
        except ValueError:
             # Handle case where display might be "Error"
            st.session_state.calc_display = ""
            st.session_state.calc_history = 0

        st.session_state.calc_operation = operation
        st.session_state.new_input = True

def calculate_result():
    """Performs the final calculation when the '=' button is clicked."""
    # This function is called as an on_click callback from app.py
    if st.session_state.calc_operation and st.session_state.calc_display:
        try:
            num1 = st.session_state.calc_history
            num2 = float(st.session_state.calc_display)
            result = 0

            if st.session_state.calc_operation == '+':
                result = num1 + num2
            elif st.session_state.calc_operation == '-':
                result = num1 - num2
            elif st.session_state.calc_operation == '*':
                result = num1 * num2
            elif st.session_state.calc_operation == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    st.session_state.calc_display = "Error"
                    return
            
            # Use a helper to format the result nicely
            st.session_state.calc_display = str(round(result, 5))
            st.session_state.calc_history = result
            st.session_state.calc_operation = None
            st.session_state.new_input = True

        except ValueError:
            st.session_state.calc_display = "Error"
