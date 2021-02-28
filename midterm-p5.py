# Write a Python function that returns a list of keys in aDict with the value target.
# The list of keys you return should be sorted in increasing order. The keys and values
# in aDict are both integers. (If aDict does not contain the value target, you should
# return an empty list.)

# This function takes in a dictionary and an integer and returns a list.

def keysWithValue(aDict, target):
  '''
  aDict: a dictionary
  target: an integer
  '''
  # Your code here
  listResult = []
  for key in aDict:
    if aDict[key] == target:
      listResult.append(key)
  return sorted(listResult)

testDict = {1: 2, 10: 7, 3: 7, 2: 6, 19: 2}
print(keysWithValue(testDict, 20))
