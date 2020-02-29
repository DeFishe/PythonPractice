#x = 2
#print(x == 2)
#print(x == 3)
#print(x < 3)

#name = "John"
#age = 23
#if name == "John" and age == 23:
#    print("Your name is John and you are 23 years old.")

#if name == "John" or name == "Rick":
#    print("Your name is either John or Rick")

#print("Enter your name.")
#nameToFind = input()
#nameOptions = [ "John", "Jacob"]
#if nameToFind in nameOptions:
#    print("Your name, %s, is a match." % nameToFind)
#elif nameToFind in nameOptions:
#    print("Your name is, %s, is a match." % nameToFindB)
#else:
#    print("Your name wasn't on the list.")

#x = [1,2,3]
#y = [1,2,3]
#print(x == y) # Prints out True
#print(x is y) # Prints out False

#not instead of ! for inverting values

# Change the variables in the first section, so that each if statement resolves as True.
number = 20
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")