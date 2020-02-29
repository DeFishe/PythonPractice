number = 1 + 2 - 3 * 4 / 5
print(number)
print(11 % 3)
#VERY INTERESTING two asterisks raise by a power
squared = 7 ** 2
cubed = 7 ** 3
print(squared)
print(cubed)
#standard concatenation works in python. Not going to do it... 
#BUT you can multiply a string to create repetition. MIND_BLOWN = true
print("Hello\n" * 10)
#can join lists with addition operators!!!
list_one = [1,2,3]
list_two = [4,5,6]
list_three = list_one + list_two
for x in list_three:
    print("%d" % x)
print(list_three)

print([1,2,3] * 3)

x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list
print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))