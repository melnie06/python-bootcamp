# Expected username and password (you can change the value)
correct_username = "user"
correct_password = "pass"

admin_username = "admin"
admin_password = "admin"



# Enter username and password
username_input = input("Please provide username: ")
password_input = input("Please provide password: ")

correct_username_given = correct_username == username_input
correct_password_given = correct_password == password_input

correct_admin_user = admin_username == username_input
correct_admin_password_given = admin_password == password_input

# TODO: Notify user if credentials are valid or invalid
correct_credentials = correct_username_given and correct_password_given
admin_correct_credentials = correct_admin_user and correct_admin_password_given



if correct_credentials or admin_correct_credentials:
    print("Access Granted")
else:
    print("Access Denied")




