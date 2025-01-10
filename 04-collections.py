# Collections
print('\n===== Collections ====')

# List
print('\n===== List ====')
myFruitList = ["apple", "banana", "cherry"]
print('Full list:', myFruitList)
print('Type of myFruitList:', type(myFruitList))

# Accessing to list elements
print('First element of myFruitList:', myFruitList[0])
print('Second element of myFruitList:', myFruitList[1])
print('Third element of myFruitList:', myFruitList[2])
print('Last element of myFruitList:', myFruitList[-1])
# print('Fourth element of myFruitList:', myFruitList[3]) # This code throws an error
# print('Fourth element of myFruitList:', myFruitList[-4]) # This code throws an error

# Mutate list elements
myFruitList[2] = 'orange'
print('Full list:', myFruitList)

# Tuple
print('\n===== Tuples ====')
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print('Full tuple:', myFinalAnswerTuple)
print('Type of myFinalAnswerTuple:', type(myFinalAnswerTuple))

# Accessing to tuple elements
print('First element of myFinalAnswerTuple:', myFinalAnswerTuple[0])
print('Second element of myFinalAnswerTuple:', myFinalAnswerTuple[1])
print('Third element of myFinalAnswerTuple:', myFinalAnswerTuple[2])
print('Last element of myFinalAnswerTuple:', myFinalAnswerTuple[-1])

# Tuple can't be mutated
# myFinalAnswerTuple[2] = 'orange' # This code throws an exception

# Dictionary
print('\n===== Dictionary ====')
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple",
  "Paulo 2" : "pineapple 2"
}
print('Full dictionary:', myFavoriteFruitDictionary)
print('Type of myFavoriteFruitDictionary:', type(myFavoriteFruitDictionary))

# Accessing to tuple elements
print('First element of myFavoriteFruitDictionary:', myFavoriteFruitDictionary['Akua'])
print('Second element of myFavoriteFruitDictionary:', myFavoriteFruitDictionary['Saanvi'])
print('Third element of myFavoriteFruitDictionary:', myFavoriteFruitDictionary['Paulo'])
print('Fourth element of myFavoriteFruitDictionary:', myFavoriteFruitDictionary['Paulo 2'])