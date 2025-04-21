#Print all numbers from 1 to 100 except numbers divisible by 4
for i in range(1,100):
    if (i % 4 == 0):
        continue
    else:
      print(i)
      
#OR

new_list=[]
for i in range(1,100):
    if (i % 4 == 0):
        continue
    else:
      new_list.append(i)
print(new_list)
