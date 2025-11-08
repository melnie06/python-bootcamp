minimum_height = 138

# TODO: Ask the user for the following inputs
user_height = int(input('User height (in cm): '))

# TODO: Notify user if they can enter the ride
can_enter_ride = minimum_height < user_height
print("Can enter the ride:", can_enter_ride)
