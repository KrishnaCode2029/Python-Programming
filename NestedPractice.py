# Take a number from the user.

# 1.First check whether the number is positive.
# 2.If positive, check whether it is even or odd.
# 3.If negative, print "Negative number".
# 4.If zero, print "Zero".

number=int(input("Enter number : "))

if number >= 0 :

  # Nested If else statement
  if number % 2 == 0:
    print("The number is positive")
    print(number," is even number")
    
  else:
    print("The number is negative")
    print(number," is odd number")
else:
  print("The number is negative number")
