# Write a function to flatten a list. The list contains other lists, strings, or ints.
# For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
# is flattened into [1,'a','cat',2,3,'dog',4,5] (order matters).

def flatten(aList):
  '''
  aList: a list
  Returns a copy of aList, which is a flattened version of aList
  '''
  if aList == []:
    return aList

  if len(aList) == 1:
      if type(aList[0]) == list:
          resultList = flatten(aList[0])
      else:
          resultList = aList
  elif type(aList[0]) == list:
    resultList = flatten(aList[0]) + flatten(aList[1:])
  else:
    resultList = [aList[0]] + flatten(aList[1:])
  return resultList

print(flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5]))
print(flatten([]))
print(flatten([5]))
print(flatten([[[[3,4,5]]],1,"Carlos"]))