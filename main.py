import base64
import streamlit as st
from calculator import monthly_installment

# Set page configuration
st.set_page_config(
    page_title='BPs Calculator',
    layout='centered'
)

# Define functions for each calculator
def investment_calculator():
    # Investment type selection
    investment_type = st.radio(
        "Select the type of investment:",
        ("Simple Interest", "Compound Interest")
    )

    # Input form
    with st.form('data_form'):
        principal = st.number_input('Enter Principal Amount')
        rate = st.slider('Enter Annual Interest Rate (%)', 0.0, 20.0, 5.0)
        time = st.slider('Enter Time Period (in years)', 1, 20)

        # Submit button
        if st.form_submit_button('Calculate'):
            # Calculation logic
            if investment_type == "Simple Interest":
                simple_interest = principal * (1 + (rate / 100) * time)
                st.write('Your investment with simple interest will grow to:', simple_interest)
            else:
                compound_interest = principal * (1 + rate / 100) ** time
                st.write('Your investment with compound interest will grow to:', compound_interest)
                
def bond_repayment_calculator():
   
    st.title("Bond Repayment Calculator")

    # Using streamlit form to collect data from the user
    with st.form('data_form'):
        principal = st.number_input('ENTER LOAN AMOUNT R')
        period = st.slider('LOAN TERM IN YEARS', 1, 20)
        interest_rate = st.slider('VARIABLE INTEREST RATE %', 7.75, 0.25, 25.75)

        if st.form_submit_button('Calculate Monthly Installment'):
            st.write('Your Monthly Installment for the loan of R' + str(principal) + ' is R' + str(monthly_installment(principal, period, interest_rate)))
            
        
# Main function
  
def main():
    # Page title
    st.title("BPs Calculator")

    # Calculator selection
    calculator = st.radio(
        "Select a calculator:",
        ("Investment Calculator", "Bond Repayment Calculator")
    )

    # Show the selected calculator
    if calculator == "Investment Calculator":
        investment_calculator()
    else:
        bond_repayment_calculator()

if __name__ == '__main__':
    main()