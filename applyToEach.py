def factorBy(factor):
  def multiply (number):
    return factor * number
  return multiply

def applyToEach(L, f):
  '''
  L: list
  f: function
  '''
  for i in range(len(L)):
    L[i] = f(L[i])
  return L

testList = [1, -4, 8, -9]
factorBy5 = factorBy(5)

print(applyToEach(testList, factorBy5))
