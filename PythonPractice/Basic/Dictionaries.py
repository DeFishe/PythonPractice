##Create an empty dictionary and then add key/value pairs
#phoneBookA = {}
#phoneBookA["John"] = 6037779954
#phoneBookA["Jack"] = 1019819981
#phoneBookA["Jill"] = 8245996041
##print(phoneBookA)

##Initialize dictionary with values
#phoneBookB = {
#    "John" : 6037779954,
#    "Jack" : 1019819981,
#    "Jill" : 8245996041
#}
##print(phoneBookB)

##iterate through dictionary
##for name, number in phoneBookA.items():
##    print("Phone number of %s is %d" % (name, number))

##To remove:
#del phoneBookA["John"]
##Or, my preferred
#phoneBookA.pop("Jack")
#for name, number in phoneBookA.items():
#    print("Phone number of %s is %d" % (name, number))

#EXERCISE
#Add "Jake" to the phonebook with the phone number 938273443, and remove Jill from the phonebook.

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

# write your code here
phonebook["Jake"] = 9382733443
phonebook.pop("Jill")

# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")
