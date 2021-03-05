def numberToString(num):
    tenths = ["", "", "twenty", "thirty", "forty",
                    "fifty", "sixty", "seventy", "eighty", "ninety"]
    unitsAndTeens = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                    "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    if num < 20:
      return unitsAndTeens[num]
    if num < 100:
      return tenths[num // 10] + " " + unitsAndTeens[num % 10]
    if num < 1000:
      return unitsAndTeens[num // 100] + " hundred " + numberToString(num % 100)
    if num < 1000000:
      return numberToString(num // 1000) + " thousand " + numberToString(num % 1000)
    if num < 1000000000:
      return numberToString(num // 1000000) + " million " + numberToString(num % 1000000)
    if num < 1000000000000:
      return numberToString(num // 1000000000) + " billion " + numberToString(num % 1000000000)
    if num < 1000000000000000:
      return numberToString(num // 1000000000000) + " trillion " + numberToString(num % 1000000000000)

print(numberToString(1796225823201))