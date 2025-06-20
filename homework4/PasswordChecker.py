correct_password="GeraltOfRivia"
for i in range(3):
    password = input("Enter your password: ")
    if password == correct_password:
        print("Access granted")
        break
else :
    print("Access denied")