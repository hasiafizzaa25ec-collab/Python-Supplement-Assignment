# Problem 79: Calculate compound interest
# Find and fix the error
def compound_interest(principal, rate, time, n):
    # Compound interest formula: A = P*(1 + r/(n*100))^(n*t)
    # Return interest only
    amount = principal * (1 + rate / (n * 100)) ** (n * time)
    return amount - principal

p = 1000  # Principal amount
r = 5     # Annual interest rate in %
t = 2     # Time in years
n = 4     # Compounding frequency per year
print("Compound Interest:", round(compound_interest(p, r, t, n), 2))

