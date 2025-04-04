#Given password = "P@ssw0rd", replace all vowels with "*"
vowels=['a','i','o','u','e','A','E','I','O','U']
password="MARIA"
new_password=""
for i in password:
    if i in vowels:
        new_password+="*"
    else:
        new_password+=i
print(new_password)
