import streamlit as st
# Import logic from the new file
from commission_logic import (
    clear_calc,
    input_number,
    handle_operation,
    calculate_result,
    calculate_bonus_total, # Assuming you had this in a previous 'commission_logic.py'
    add_entry,
    remove_entry
)

# Set page config and inject custom CSS for margins
st.set_page_config(layout="wide", page_title="Calculators App")

# --- Custom CSS for Margins and Calculator Styling ---
st.markdown("""
<style>
    /* Centers the content and limits its maximum width */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 5rem;
        padding-right: 5rem;
        max-width: 1400px;
        margin: auto;
    }
    .stTabs {
        padding-top: 1rem;
    }
    /* Style for the calculator display area (read-only input simulation) */
    div[data-testid="stTextInput"] input {
        text-align: right;
        font-size: 2em;
        padding: 10px;
    }
    /* Adjust button height and styling for the calculator grid */
    .stButton>button {
        height: 3.5em;
        width: 100%;
        font-size: 1.2em;
        margin: 2px 0; /* Add a tiny vertical margin for spacing */
    }

    /* Optional: Fine-tune column gaps within the calculator layout */
    div[data-testid="stHorizontalBlock"] {
        gap: 0.25rem; /* Reduce the default gap between columns slightly */
    }

</style>
""", unsafe_allow_html=True)
# -----------------------------

# Initialize session state for bonus entries (Bonus Calculator)
if 'bonus_entries' not in st.session_state:
    st.session_state.bonus_entries = [{'amount': 0.0, 'percentage': 0.0}]

# Initialize session state for the standard calculator
if 'calc_display' not in st.session_state:
    st.session_state.calc_display = ""
if 'calc_history' not in st.session_state:
    st.session_state.calc_history = 0
if 'calc_operation' not in st.session_state:
    st.session_state.calc_operation = None
if 'new_input' not in st.session_state:
    st.session_state.new_input = False


def standard_calculator_ui():
    st.header("Calculator")

    # The display field is read-only
    display_value = st.session_state.calc_display if st.session_state.calc_display else "0"
    # Note: st.metric handles rounding slightly differently, but this retains original behavior
    try:
        metric_value = round(float(display_value))
    except ValueError:
        metric_value = "Error"
        
    st.metric("Result", metric_value)

    # Create a 4x4 grid using columns
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.button("7", on_click=input_number, args=(7,), use_container_width=True)
        st.button("4", on_click=input_number, args=(4,), use_container_width=True)
        st.button("1", on_click=input_number, args=(1,), use_container_width=True)
        # We pass the button clicks directly to the logic functions
        st.button("C", on_click=clear_calc, use_container_width=True)

    with col2:
        st.button("8", on_click=input_number, args=(8,), use_container_width=True)
        st.button("5", on_click=input_number, args=(5,), use_container_width=True)
        st.button("2", on_click=input_number, args=(2,), use_container_width=True)
        st.button("0", on_click=input_number, args=(0,), use_container_width=True)

    with col3:
        st.button("9", on_click=input_number, args=(9,), use_container_width=True)
        st.button("6", on_click=input_number, args=(6,), use_container_width=True)
        st.button("3", on_click=input_number, args=(3,), use_container_width=True)
        st.button("=", on_click=calculate_result, use_container_width=True)

    with col4:
        # Args are passed to the logic functions
        st.button("÷", on_click=handle_operation, args=('/'), use_container_width=True)
        st.button("×", on_click=handle_operation, args=('*'), use_container_width=True)
        st.button(r"\-", on_click=handle_operation, args=('-'), use_container_width=True)
        st.button(r"\+", on_click=handle_operation, args=('+'), use_container_width=True)


# --- Main Layout: Two Columns ---
left_column, right_column = st.columns([2, 1]) # Make left column 2x the width of the right

with left_column:
    tab1, tab2 = st.tabs(["Bonus Calculator", "Other Tab (Placeholder)"])

    with tab1:
        st.header("🌟 Bonus Calculator")
        st.text("Calculate total bonuses across multiple entries")
        st.markdown("---")
        percentage_options = list(range(5, 101, 5))

        for i, entry in enumerate(st.session_state.bonus_entries):
            col1_b, col2_b, col3_b = st.columns([4, 4, 1])
            with col1_b:
                # The input fields update session state directly via keys
                new_amount = st.number_input(f"Amount", min_value=0, step=20, key=f"amount_{i}")
            with col2_b:
                new_percentage = st.selectbox(f"Bonus %", options=percentage_options, key=f"percentage_{i}")            
            with col3_b:
                st.markdown("<br>", unsafe_allow_html=True)
                # Call logic function on click
                st.button("🗑️", key=f"remove_{i}", on_click=remove_entry, args=(i,))
            
            # This ensures the session state reflects the current inputs immediately
            st.session_state.bonus_entries[i] = {'amount': new_amount, 'percentage': new_percentage}

        st.button(r"\+ Add Metric", on_click=add_entry, use_container_width=True)
        st.markdown("---")

        if st.session_state.bonus_entries:
            # Call the bonus calculation logic function
            total_bonus = calculate_bonus_total(st.session_state.bonus_entries)
            st.metric("Total Calculated Bonus", f"${total_bonus:,.2f}")
        else:
            st.info("Add metric rows to calculate bonuses.")

    with tab2:
        st.header("Placeholder Tab")
        st.write("This tab is a placeholder for future functionality in the left column.")

with right_column:
    # Call the function that builds the standard calculator UI
    standard_calculator_ui()
