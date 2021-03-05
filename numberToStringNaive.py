

def numberToString(num):
    '''
    Takes a positive number and returns the number as you would write it in english
    Number can have up to 9 positions
    Only positive numbers
    no "and" strings are necessary
    '''
    result = ""
    mappingTenths = ["", "", "twenty", "thirty", "forty",
                     "fifty", "sixty", "seventy", "eighty", "ninety"]
    mappingUnits = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                    "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    
    # Convert number to a list
    numArray = list(str(num))

    if num < 20:
        return mappingUnits[num]
    if num >= 20 and num < 100:
        return mappingTenths[int(numArray[0])] + " " + mappingUnits[int(numArray[1])]
    if num >= 100 and num < 1000:
        return mappingUnits[int(numArray[0])] + " hundred " + mappingTenths[int(numArray[1])] + " " + mappingUnits[int(numArray[2])]
    if num >= 1000 and num < 10000:
        return mappingUnits[int(numArray[0])] + " thousand " + " " + mappingUnits[int(numArray[1])] + " hundred " + mappingTenths[int(numArray[2])] + " " + mappingUnits[int(numArray[3])]
    if num >= 10000 and num < 100000:
        if int(numArray[0]) < 2:
          thousandTenth = numArray[0] + numArray[1]
          result = mappingUnits[int(thousandTenth)]
          return result + " thousand " + mappingUnits[int(numArray[2])] + " hundred " +  mappingTenths[int(numArray[3])]  + " " + mappingUnits[int(numArray[4])]
        else:
          return mappingTenths[int(numArray[0])]+ " " + mappingUnits[int(numArray[1])] + " thousand " + mappingUnits[int(numArray[2])] + " hundred " + mappingTenths[int(numArray[3])] + " " + mappingUnits[int(numArray[4])]
    if num >= 100000 and num < 1000000:
      return mappingUnits[int(numArray[0])] + " hundred " + mappingTenths[int(numArray[1])] + " " + mappingUnits[int(numArray[2])] + " thousand " + mappingUnits[int(numArray[3])] + " hundred " + mappingTenths[int(numArray[4])] + " " + mappingUnits[int(numArray[5])]
    if num >= 1000000 and num < 10000000:
      return mappingUnits[int(numArray[0])] + " million " + mappingUnits[int(numArray[1])] + " hundred " + mappingTenths[int(numArray[2])] + " " + mappingUnits[int(numArray[3])] + " thousand " + mappingUnits[int(numArray[4])] + " hundred " + mappingTenths[int(numArray[5])] + " " + mappingUnits[int(numArray[6])]
    if num >= 10000000 and num < 100000000:
      if int(numArray[0]) < 2:
        millionTenth = numArray[0] + numArray[1]
        if int(numArray[3]) < 2:
          thousandTenth = numArray[3] + numArray[4]
          result = mappingUnits[int(thousandTenth)]
          return mappingUnits[int(millionTenth)] + " million " + mappingUnits[int(numArray[2])] + " hundred " + result + " thousand " + mappingUnits[int(numArray[5])] + " hundred " + mappingTenths[int(numArray[6])] + " " + mappingUnits[int(numArray[7])]
        else:
          return mappingUnits[int(millionTenth)] + " million " + mappingUnits[int(numArray[2])] + " hundred " + mappingTenths[int(numArray[3])] + " " + mappingUnits[int(numArray[4])] + " thousand " + mappingUnits[int(numArray[5])] + " hundred " + mappingTenths[int(numArray[6])] + " " + mappingUnits[int(numArray[7])]
      else:
        if int(numArray[3]) < 2:
          thousandTenth = numArray[3] + numArray[4]
          result = mappingUnits[int(thousandTenth)]
          return mappingTenths[int(numArray[0])]+ " " + mappingUnits[int(numArray[1])] + " million " + mappingUnits[int(numArray[2])] + " hundred " + result + " thousand " + mappingUnits[int(numArray[5])] + " hundred " + mappingTenths[int(numArray[6])] + " " + mappingUnits[int(numArray[7])]
        else:
          return mappingTenths[int(numArray[0])]+ " " + mappingUnits[int(numArray[1])] + " million " + mappingUnits[int(numArray[2])] + " hundred " + mappingTenths[int(numArray[3])] + " " + mappingUnits[int(numArray[4])] + " thousand " + mappingUnits[int(numArray[5])] + " hundred " + mappingTenths[int(numArray[6])] + " " + mappingUnits[int(numArray[7])]
    # if num >= 100000000 and num < 1000000000:
    #   if int(numArray[1]) < 2:
    #     hundrethMillionTenth = numArray[1] + numArray[2]
    #     if int(numArray[4]) < 2:
    #       hundrethThousandTenth = numArray[4] + numArray[5]
    #       result = mappingUnits[int(hundrethThousandTenth)]
    #       return mappingUnits[int(hundrethMillionTenth)] + " million " + mappingUnits[int(numArray[2])] + " hundred " + result + " thousand " + mappingUnits[int(numArray[5])] + " hundred " + mappingTenths[int(numArray[6])] + " " + mappingUnits[int(numArray[7])]
    #     else:
    #       return mappingUnits[int(hundrethMillionTenth)] + " million " + mappingUnits[int(numArray[2])] + " hundred " + mappingTenths[int(numArray[3])] + " " + mappingUnits[int(numArray[4])] + " thousand " + mappingUnits[int(numArray[5])] + " hundred " + mappingTenths[int(numArray[6])] + " " + mappingUnits[int(numArray[7])]
    #   else:
    #     if int(numArray[3]) < 2:
    #       hundrethThousandTenth = numArray[3] + numArray[4]
    #       result = mappingUnits[int(hundrethThousandTenth)]
    #       return mappingTenths[int(numArray[0])]+ " " + mappingUnits[int(numArray[1])] + " million " + mappingUnits[int(numArray[2])] + " hundred " + result + " thousand " + mappingUnits[int(numArray[5])] + " hundred " + mappingTenths[int(numArray[6])] + " " + mappingUnits[int(numArray[7])]
    #     else:
    #       return mappingTenths[int(numArray[0])]+ " " + mappingUnits[int(numArray[1])] + " million " + mappingUnits[int(numArray[2])] + " hundred " + mappingTenths[int(numArray[3])] + " " + mappingUnits[int(numArray[4])] + " thousand " + mappingUnits[int(numArray[5])] + " hundred " + mappingTenths[int(numArray[6])] + " " + mappingUnits[int(numArray[7])]
    # print(numArray);

print(numberToString(13233456))

# # 189 one hundred eighty one
# # 89 eighty one
# # 9 nine
# 999,999,999


# {} hundred {} million
# {} hundred {} thousand
# {} hundred {}


# slice 1: 999
# mappingUnits[9] = nine hundred
# mappingTenths[9] = ninety
# mappingUnits[9] = nine

# nine hundred ninety nine thousand
