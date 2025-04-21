text = "H4ck3r"
alternated=""
for i in text:
     if i.islower():  #Checks if a character is lowercase
        alternated += i.upper()    #Converts a letter to uppercase.
     elif i.isupper():    #checks if the character is uppercase
        alternated+=i.lower()  #converts a character to lowercase
     else:
        alternated+=i
print(alternated)
