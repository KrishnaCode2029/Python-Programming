# Representation of List
marks=[87,56,99,36,90,82]

# List Slicing :- Similar to string slicing

print(marks[1]) #1 to len of list
print(marks[1:5]) #1 to 5
print(marks[:6]) #0 to 6
print(marks[-1:-5]) #-1 to -5

# Methods :-

# append:Add element at the end of the list
marks.append(89)
marks.append(81)

print("List after append")
print(marks)

# Sort list in asecding order
print("List after sort")
marks.sort()
print(marks)


# sort(reverse=true):Sort list in descending order 
print("List After Reverse")
marks.sort(reverse=True)
print(marks)

# reverse() Sort in reverse same as it is like reverse=true
print("List After Reverse")

marks.reverse()
print(marks)

# .insert(idx,element):Insert element at the specific idx
print("List After adding element at idx")

marks.insert(5,99)
print(marks)

# makrs.remove(el):Remove element from list
marks.remove(89)


# marks.pop() : Remove element from end
marks.pop()

