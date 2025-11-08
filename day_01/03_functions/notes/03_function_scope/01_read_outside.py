outer_variable = 10


def function():
    print("Inner", outer_variable)


function()
print("Outer", outer_variable)
