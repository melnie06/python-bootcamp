# response = input("Proceed: ")
# if response == "Yes" or response == "yes" or response =="y":
# 	print("Proceeding")

response = input("Proceed: ")
valid_options = ("Yes", "yes", "y")
if response in valid_options:
    print("Proceeding")
