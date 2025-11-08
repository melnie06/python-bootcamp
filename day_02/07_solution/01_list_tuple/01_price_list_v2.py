prices = [10_000, 20, 3_000, 3, -200, 1_000]

# Print the first, third, and last item
print("Current Price:", prices[0])
print("Current Price:", prices[2])
print("Current Price:", prices[-1])

# Change the first, third, and last values to half the price
prices[0] //= 2
prices[2] //= 2
prices[-1] //= 2

# Print the first, third, and last item again to see new price
print("New Price:", prices[0])
print("Item Price:", prices[2])
print("Item Price:", prices[-1])
