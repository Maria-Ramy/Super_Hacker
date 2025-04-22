#Check if a string is a palindrome (same forward and backward)
text = input("Enter text: ")
if(text == text[::-1]): # check if reverse = text
    print("It is palindrome")
else:
    print("It is not palindrome")
