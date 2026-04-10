prices = {"apple": 50, "banana": 20, "milk": 30}
quantities = {"apple": 2, "banana": 5, "milk": 1}

total_bill = 0

for item in quantities:
    if item in prices:
        total_bill = total_bill + (prices[item] * quantities[item])

print(total_bill)