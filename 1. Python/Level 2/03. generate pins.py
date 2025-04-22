#Create a script that prints every 4-digit PIN code (0000-9999)
for i in range(10000):
    print(f"{i:04d}")

# :04d is the format instruction:
# 0 → fill with zeros
# 4 → total width of 4 digits
# d → it's a decimal (integer)
