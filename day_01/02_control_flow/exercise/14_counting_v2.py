# # Ask the user for a starting and ending number
# start = int(input("Enter start: "))
# end = int(input("Enter end: "))

# # TODO: Print the numbers start to end
# for count1 in range(start,end):
#     print(count1)

running = True

while running:
    command = input('> ')
    
    if command == "quit":
        running = False
            