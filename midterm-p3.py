# def Square(x):
#   return SquareHelper(abs(x), x)


# def SquareHelper(n, x):
#   if n == 0:
#       return 0
#   return SquareHelper(n-1, x) + x

# Square(-9)


# Problem 3
def closest_power(base, num):
  import math
  '''
  base: base of the exponential, integer > 1
  num: number you want to be closest to, integer > 0

  Find the integer exponent such that base**exponent is closest to num.
  Note that the base**exponent may be either greater or smaller than num.
  In case of a tie, return the smaller value.
  Returns the exponent.
  '''
  # Your code here
  num = int(num)
  if num == 1:
    return 0
  if num == base:
    return 1

  delta0 = num - base
  result = 1

  if num > 1:
    for exponent in range(1, num):
      baseToPower = base**exponent
      delta1 = abs(num - baseToPower)
      if abs(delta1) == abs(delta0):
        result = exponent - 1
      elif delta1 < delta0:
        delta0 = delta1
        result = exponent
        print("exponent "+str(exponent))

  return result

print(closest_power(15,8))
