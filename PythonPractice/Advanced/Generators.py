import random

#def winningNumbers():
#    for i in range(6):
#        yield random.randint(1, 40)

#        yield random.randint(1, 15)

#for random_number in winningNumbers():
#    print("And the next number is %d" % random_number)

#EXERCISE
#Fibonacci sequence with genereator
#challenge: only use to variables for fib

# fill in this function
def fib():
    a, b = 1, 1
    yield a
    yield b
    for i in range(10):
        a, b = b, a + b
        yield b



# testing code
import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break