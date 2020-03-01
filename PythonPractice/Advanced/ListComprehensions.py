#One approach:
#sentence = "the quick brown fox jumps over the lazy dog"
#words = sentence.split()
#wordLengths = []
#for word in words:
#    if word != "the":
#        wordLengths.append(len(word))
#print(words)
#print(wordLengths)

#Using a list comprehension
#sentence = "the quick brown fox jumps over the lazy dog"
#words = sentence.split()
#wordLengths = [ len(word) for word in words if word != "the" ]
#print(words)
#print(wordLengths)

#EXERCISE
#Using a list comprehension, create a new list called "newlist" out of the list "numbers", 
#which contains only the positive numbers from the list, as integers.

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [ number for number in numbers if number > 0 ]
print(newlist)