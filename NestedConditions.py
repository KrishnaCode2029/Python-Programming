# Nested Conditions

# We already lerned about if , if else, if elif else , now we will learn about nested if
age = int(input("Enter age : "))

has_id =False

if age >= 18:
    if has_id:
        print("You can enter")
    else:
        print("ID is required")
else:
    print("You are underage")



