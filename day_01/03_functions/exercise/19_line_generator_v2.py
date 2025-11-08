"""
    TODO: Create a function `line_generator` that has a parameter `number` and prints the following:
	Line 1
	Line 2
	...
	Line number
"""
def line_generator(number):
    
    for x in range(number):
        print('Line', x )
    
line_generator(5)

