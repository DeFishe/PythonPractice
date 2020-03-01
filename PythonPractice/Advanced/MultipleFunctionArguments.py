#def foo(first, second, third, *therest):
#    print(first)
#    print(second)
#    print(third)
#    for x in therest:
#        print(x)

#foo(1,2,3,4,5,6)

#def bar(first, second, third, **options):
#    if options.get("action") == "sum":
#        print("The sum is: %d" % (first + second + third))
#    if options.get("number") == "first":
#        return first

#result = bar(1, 2, 3, action = "sum", number = "first")
#print(result)

#EXERCISE:
#Fill in the foo and bar functions so they can receive a variable amount of arguments (3 or more) 
#The foo function must return the amount of extra arguments received. The bar must return True if 
#the argument with the keyword magicnumber is worth 7, and False otherwise.

# edit the functions prototype and implementation
def foo(a, b, c, *extra):
    count = 0
    for x in extra:
        count += 1
    return count

def bar(a, b, c, **extra):
    if extra.get("magicnumber") == 6:
        return False
    if extra.get("magicnumber") == 7:
        return True


# test code
if foo(1,2,3,4) == 1:
    print("Good.")
if foo(1,2,3,4,5) == 2:
    print("Better.")
if bar(1,2,3,magicnumber = 6) == False:
    print("Great.")
if bar(1,2,3,magicnumber = 7) == True:
    print("Awesome!")