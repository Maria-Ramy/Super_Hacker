#Use a while loop to continuously ask for a password until the correct one is entered
password="<PASSWORD>"
while(True):
    user_password=input("Enter your password: ")
    if user_password==password:
        print("Welcome")
        break
    else:
        print("Wrong password")
