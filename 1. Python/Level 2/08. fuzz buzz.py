#Print numbers 1-100, replacing multiples of 3 with "Fizz", multiples of 5 with "Buzz", 
#and both with "FizzBuzz".
arr=[]
for i in range(1,101):
    if (i % 3 == 0 and i % 5 == 0): #must be placed first upper
        arr.append("FUZZ BUZZ")
    elif (i%3==0):
        arr.append("FUZZ")
    elif(i%5==0):
        arr.append("BUZZ")
    else:
        arr.append(i)
print(arr)

# You're checking for i % 3 == 0 and i % 5 == 0 before i % 15 == 0. But any number 
# divisible by 15 is also divisible by 3, so "Fizz" will be printed instead of "FizzBuzz"
# For example:
# When i = 15:
# 15 % 3 == 0 → True, so it prints "Fizz" and skips checking for FizzBuzz.
