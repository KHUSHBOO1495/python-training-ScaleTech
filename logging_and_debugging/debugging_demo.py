def calculate_tax(amount):
    tax = amount * 0.18
    return tax

def calculate_total(price):
    breakpoint()
    tax = calculate_tax(price)
    total = price + tax
    return total

result = calculate_total(1000)
print(result)
