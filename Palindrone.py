# Check if a list is palindrome


my_list = [1, 2, 3, 2, 1]

new_list=my_list.copy()

new_list.reverse()

if my_list==new_list:
   print("The list is palindrome")
else:
   print("The list is not palindrome")
