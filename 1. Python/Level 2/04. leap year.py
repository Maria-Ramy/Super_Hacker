#Check if a given year is a leap year.
year=int(input("Enter a year: "))
if(year % 4 ==0 and year % 100 !=0) or (year%400 ==0) :
    print("LEAP YEAR")
else:
    print("NOT LEAP :)")
    
# year % 4 == 0 → divisible by 4 ✅
# year % 100 != 0 → not a century year ❌ (unless...)
# year % 400 == 0 → it’s okay if divisible by 400 ✅
