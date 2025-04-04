#Reverse the string “rekcah_repus”  without using built-in functions
x="rekcah_repus"
new_x=""
for i in range(len(x)-1,-1,-1):
    new_x+=x[i]
print(new_x)
