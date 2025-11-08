prices = [1_000, 10, 200, 1000, 3_000]

# Convert the numbers into half their original values
discounted_prices = [price // 2 for price in prices]
print(discounted_prices)