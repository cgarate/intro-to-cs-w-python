def howMany(aDict):
  '''
  aDict: A dictionary, where all the values are lists.
  returns: int, how many values are in the dictionary.
  '''
  totalValues = 0
  for key in aDict:
    totalValues += len(aDict[key])

  return totalValues

print(howMany({'u': [10, 15, 5, 2, 6], 'B': [15]}))

def biggest(aDict):
  '''
  aDict: A dictionary, where all the values are lists.

  returns: The key with the largest number of values associated with it
  '''
  # Your Code Here
  maxValues = 0
  keyWithMaxValues = None
  for key in aDict:
    if len(aDict[key]) > maxValues:
      maxValues = len(aDict[key])
      keyWithMaxValues = key

  return keyWithMaxValues

print(biggest({'a': [], 'b': [1, 7, 5, 4, 3, 18, 10, 0]}))
