max_attempt = 3
correct_password = "pass"

for attempt in range(max_attempt):
    password = input("Enter password: ")
    if password == correct_password:
        print("Access granted")
        break
