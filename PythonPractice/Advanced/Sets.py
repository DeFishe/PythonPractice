#sets are lists with no duplicate entries
#noRepeats = set("my name is Darian and Darian is my name".split())
#print(noRepeats)

#a = set(["John", "Jacob", "Jingle"])
#b = set(["Jingle", "Debbie", "Francis"])
#print(a.intersection(b))

#print(a.difference(b))
#print(b.difference(a))

#print(a.symmetric_difference(b))
#print(b.symmetric_difference(a))

#print(a.difference(b))
#print(b.difference(a))

#print(a.union(b))

#EXERCISE
#In the exercise below, use the given lists to print out a set containing all the participants 
#from event A which did not attend event B.

a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.difference(b))