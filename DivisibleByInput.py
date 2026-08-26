# Check number is divisible by input 

number=int(input("Enter number: "))
divisible=int((input("Enter divisible")))

if number%divisible==0:
    print("The number",number," is divisible by ", divisible)
else:
    print("The number is not divisble.")

print(number/divisible);