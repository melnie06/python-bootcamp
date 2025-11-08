message = "Hello {}. Your nickname is {}"

name = input("Enter name: ")
nickname = input("Enter nickname: ")

formatted_message = message.format(name, nickname)
print(formatted_message)
