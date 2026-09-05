# Take a number from the user.

# 1.First check whether the number is positive.
# 2.If positive, check whether it is even or odd.
# 3.If negative, print "Negative number".
# 4.If zero, print "Zero".

number=int(input("Enter number : "))

if number >= 0 :

  # # Nested If else statement
  if number % 2 == 0:
    print("The number is positive")
    print(number," is even number")
    
  else:
    print("The number is negative")
#     print(number," is odd number")
else:
  print("The number is negative number")



# Question : Student Result

# Take marks of a student.

# Rules:

# If marks are 40 or above, student has passed.
# If passed:
# If marks are 75 or above → "Distinction"
# Otherwise → "Pass"
# If marks are below 40 → "Fail"
marks=int(input("Enter marks of student"))

if marks >= 40 :
  if marks >= 75:
    print("Student has Passed")
    print("Distinction")
  else:
    print("Student has Passed")
elif marks < 40:
  print("Student has failed ")
else:
  print("Wrong Input ... Try again ")






