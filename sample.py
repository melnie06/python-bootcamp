
'''
costs = [10, 20, 30, 40, 50]

discounted_costs = []

def half_price(x):
    return x // 2

discounted_costs = [half_price(cost) for cost in costs]
print(discounted_costs)
'''


#new method (advance approach)
# discounted_costs = [cost // 2 for cost in costs]


    



#old method
# for cost in costs:
#     new_cost = cost // 2
#     discounted_costs. append(new_cost)
    
# print(discounted_costs)

costs = [10, 20, 30, 1000, 40, 50, 3000]

discounted_costs = []

def half_price(x):
    return x // 2

# discounted_costs = [half_price(cost) for cost in costs[::2]] #results for every other costs
'''
discounted_costs = [half_price(cost) for cost in costs if cost < 1000]
print(discounted_costs)
'''


# discounted_costs = [cost for cost in costs if cost < 1000]
# print(discounted_costs)

'''
numbers = ["1", "2"]
# numbers = {int(number) for number in numbers} # results is list

numbers = {number: int(number) for number in numbers} #results is dictionary

print(numbers)
'''

priorities = {'L': 'Low', 'M': 'Medium'}

tasks ={
    'clean': 'L',
    'report': 'M'
}

# tasks ={key:value for key, value in tasks.items()}
tasks = {
    key:priorities.get(value) 
    for key, value in tasks.items()
    }
print(tasks)