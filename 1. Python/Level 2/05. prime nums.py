#Find prime numbers between 1 and 100. 
for num in range(2,101):
    is_prime= True
    for j in range(2,num):
        if num%j == 0: 
          #check if any number other than 1 and itself divides i evenly
#If i divides evenly by j, it means it has another divisor (besides 1 and itself), so it’s not prime.
            is_prime=False
            break
    if is_prime:
        print(num)
