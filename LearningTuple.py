# What is tuple -> A tuple is an ordered collection of multiple values that cannot be changed after creation
# Tuple remembers the position of every element.
# Once you create it, you cannot change its elements.



# Why Do We Use Tuples?--> Tuples are useful when you have data that should not be changed.

fruits = ("Apple", "Banana", "Mango")
print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[2])

# Negative Indexing
print(fruits[-1])

# Try to updata
# fruits[0]="Orange" ------>Returns the Type Error Because of Tuple is Immuatable

# In tuple we can store different data types 
student=("Sara",78.99,20)
print(student)

# Tuple Can Contain Duplicate Values
numbers=(1,2,3,4,5,4,3,2,4,3,5,1,1,1,1,1,5,3,2,5,2,5,2,1)

# Length of tuple
print(len(numbers))

# Checking Element exits in tuple or not
print("Apple" in fruits)
print("Pineapple" in fruits)

# Tuple Slicing :- Like list , slicing on tuple is possible in similar manner we sliced list
print(numbers[0:6]);
print(numbers[:len(numbers)])
print(numbers[4:])

# Negative Slicing
print(numbers[-8:-1])

# Tuples have fewer methods than lists because tuples cannot be changed.
# count()-->Counts the number of occurrances in tuple
print(numbers.count(1))

# index() ---> Returns the index of first occurrance
print(numbers.index(5))

# Creating tuple with one element is the mistake that is often created by begineers
new_one_tuple=(100) #Python considers it an integer.
print(new_one_tuple)



# Tuple Unpacking ---> You can take values from a tuple and put them into separate variables
stu = ("Krish", 20, "Computer")
name, age, branch = stu

print(name)
print(age)
print(branch)