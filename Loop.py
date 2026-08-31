# What is loop ?  ---> Loops are used to repeat instructions

# while loop
i=1

# WAP to print 1 to 100
# while i <= 100:
#   print("Krishna!!!")
#   i +=1

# WAP to print table of 5
# while i <= 10 :
#   print(i * 5)
#   i +=1

# WAP to print numbers from 100 to 1
i=100
# while i > 0 :
#    print(i)
#    i -= 1

# WAP to print the table of n
# n=int(input("Enter number"))
# i=1
# while i <=10:
#   print(i*n)
#   i=i+1


# WAP to print the elements of the following list using loop
# i=0
# list=[1,4,9,16,26,36,49,64,81,91,100]
# while i < len(list):
#   print(list[i])
#   i=i+1 


# Search x in tuple
tup=(1,4,9,16,25,36,49,64,81,100)
x=49
i=0
while i < len(tup):
  if tup[i]==x:
    print(f"The number {x} is found at index : {i}")
    break
  i=i+1
else:
  print(f"The number {x} is not found : ")


