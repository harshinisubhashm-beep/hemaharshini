base = int(input("enter the number:"))
power = int(input("enter the power:"))

result = 1

for i in range(power):
     result = result*base

print("result -", result)