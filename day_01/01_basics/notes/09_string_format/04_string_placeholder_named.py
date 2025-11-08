message = "Hello {first}. Your nickname is {second}"

name = input("Enter name: ")
nickname = input("Enter nickname: ")

formatted_message = message.format(first=name, second=nickname)
print(formatted_message)