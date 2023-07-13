def monthly_installment(principal, period, interest_rate):
    interest_rate_decimal = interest_rate / 100
    monthly_interest_rate = interest_rate_decimal / 12
    num_payments = period * 12

    # Calculate the monthly installment using the formula
    monthly_payment = principal * (
        monthly_interest_rate * (1 + monthly_interest_rate) ** num_payments
    ) / ((1 + monthly_interest_rate) ** num_payments - 1)

    return monthly_payment
