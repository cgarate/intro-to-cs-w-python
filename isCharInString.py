def isSameChar(charA, charB):
  return ord(charA) == ord(charB)

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    import math

    # Base cases
    if aStr == "":
      return False
    elif len(aStr) == 1:
      if isSameChar(char, aStr[0]):
        return True
      else:
        return False

    lowerStr = aStr.lower()
    lowerChar = char.lower()
    sizeOfString = len(lowerStr)
    top = sizeOfString
    bottom = 0

    middleOfTheStringPosition = math.floor(len(aStr) / 2)
    characterCodeInTheMiddle = ord(lowerStr[middleOfTheStringPosition])
    charCode = ord(lowerChar)

    if isSameChar(lowerChar, lowerStr[middleOfTheStringPosition]):
      return True
    else:
      # Compare character codes (a = 97 < b = 98) to determine new boundaries
      if charCode > characterCodeInTheMiddle:
        bottom = middleOfTheStringPosition
        return isIn(lowerChar, lowerStr[bottom + 1:])
      else:
        top = middleOfTheStringPosition
        return isIn(lowerChar, lowerStr[:top])

print(isIn("z", "Aclors"))