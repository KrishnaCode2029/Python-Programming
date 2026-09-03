# Range Function :- Sets Range 
# Syntax :- range(start,end,step/iteration)

# It helps to organize initialization,Condition,Iteration like for in Typed Languages,
# Range function returns a sequences of numbers starting from 0 by defalut and increments by 1(by default) and 
# stop before a specified number.

for el in range(5):  #Only Stop Value
  print(el)


print("--------------------")

for el in range(1,5): #Start and Stop Value
  print(el)

print("--------------------")


for el in range(1,100,2): #Start and Stop Value with Iteration
  print(el)

# seq = range(5)
seq=range(5)
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])
print(seq[4])
