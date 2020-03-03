#def PrintNumber(n):
#    print(n)

#def AttemptProblemCode():
#    list = (1, 2, 3, 4, 5)

#    for i in range(20):
#        try:
#            PrintNumber(list[i])
#        except IndexError:
#            PrintNumber(0)

#AttemptProblemCode()

#EXERCISE
#Handle all the exceptions. Think back to the previous lessons to return the last name of the actor.

# Setup
actor = {"name": "John Cleese", "rank": "awesome"}

# Function to modify!!!
def get_last_name():
    try:
        return actor["last_name"]
    except KeyError:
        print("Invalid key")
        return "error"

# Test code
get_last_name()
print("All exceptions caught! Good job!")
print("The actor's last name is %s" % get_last_name())