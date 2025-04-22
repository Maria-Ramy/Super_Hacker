# Simulate a login attempt system that locks after 3 failed attempts
username="maria_ramy"
password="<PASSWORD>"
count=0
while count<3:
    user=input("Enter username:")
    pas=input("Enter password:")
    if user==username and pas==password:
        print("Welcome")
        break
    else:
        print("Wrong username or password")
        count+=1
