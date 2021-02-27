def isNumber(arg):
  '''
  Determines if the arg received is of type 'int' or 'float'
  Returns a boolean
  '''
  argType = type(arg)
  if argType == int or argType == float:
    return True
  else:
    return False

def polysum(numberOfSides, sideLength):
  '''
  Problem Definition:
  * A regular polygon has 'n' number of sides. Each side has length 's'.
  * The area of a regular polygon is:  0.25∗𝑛∗𝑠2 / 𝑡𝑎𝑛(𝜋/𝑛)
  * The perimeter of a polygon is equal to the length of the boundary of the polygon (or n * s)

  Write a function called polysum that takes 2 arguments, n and s.
  This function should sum the area and square of the perimeter of the regular polygon.
  The function returns the sum, rounded to 4 decimal places.
  '''
  import math
  if isNumber(numberOfSides) and isNumber(sideLength):
    polygonArea = (0.25 * numberOfSides * sideLength**2) / math.tan(math.pi / numberOfSides)
    polygonPerimeter = numberOfSides * sideLength
    areaPlusSquareOfPerimeter = polygonPerimeter**2 + polygonArea
    return round(areaPlusSquareOfPerimeter, 4)
  else:
    return 0

