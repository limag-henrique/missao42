primeiro = int(input("Enter the first number:\n"))
segundo = int(input("Enter the second number:\n"))
mult = primeiro*segundo
print(f"{primeiro} X {segundo} = {mult}")
if (int(mult) > 0):
    print("The result is positive")
elif (int(mult) < 0):
    print("The result is negative")
else:
    print("The result is zero")




