# Numbers don't require a type to be declared
myInt = 7
print(myInt)
myFloat = 7.4
print(myFloat)
# Another method to declare a float
myFloat = float(7)
print(myFloat)
# Strings can use double quotes or single quotes. I will stick with double.
myString = "Hello World"
print(myString)
# Can assign two things in the same statement.
a,b = 3,4
print(a,b)

if myString == "Hello World":
    print("String: %s" % myString)
if isinstance(myFloat, float):
    print("Float: %f" % myFloat)
if isinstance(myInt, int):
    print("Int: %d" % myInt)
