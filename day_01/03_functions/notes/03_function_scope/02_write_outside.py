outer_variable = 10


def function():
    # Local, new variable. Not same as outer_variable outside
    outer_variable = 999
    print("Inner", outer_variable)


function()
print("Outer", outer_variable)
