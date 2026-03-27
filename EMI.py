# EMI Calculator
def calculate_emi(P, annual_rate, years):
    R = annual_rate / (12 * 100)   # monthly interest rate
    N = years * 12                 # total months

    EMI = (P * R * (1 + R)**N) / ((1 + R)**N - 1)
    return EMI
# User Input
P = float(input("Enter Principal Amount: "))
rate = float(input("Enter Annual Interest Rate (%): "))
years = int(input("Enter Loan Tenure (Years): "))

emi = calculate_emi(P, rate, years)

print(f"\nMonthly EMI: ₹{emi:.2f}")