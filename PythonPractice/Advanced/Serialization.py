import json

#jsonString = json.dumps([1, 2, 3, "a", "b", "c"])
#print(jsonString)
#json.loads(jsonString) 

#EXERCISE
#Print out the JSON string with key-value pair "Me" : 800 added to it.

# fix this function, so it adds the given name
# and salary pair to salaries_json, and return it
def add_employee(salaries_json, name, salary):
    test = json.dumps(salaries_json)
    print(test)


    return salaries_json

# test code
salaries = '{"Alfred" : 300, "Jane" : 400 }'
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])