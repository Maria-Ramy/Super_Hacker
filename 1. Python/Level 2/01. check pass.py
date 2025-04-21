#Write a script that asks for a password and only allows access if it matches "s3cr3t"
password = "s3cr3t"
test=input("Enter ur pass: ")
if (test == password):
    print("APPROVED")
else:
    print("SORRY! TRY AGAIN")
