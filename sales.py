sales = {
    "cost_value": 31.87,
    "sell_value": 45.00,
    "inventory" : 1000  
}

print()
print()
print()
print()
profit = round((sales["sell_value"]-sales["cost_value"])*sales["inventory"])
print("The profit is " + "$" + str(profit))