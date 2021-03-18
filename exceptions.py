def fancy_divide(list_of_numbers, index):
  denom = list_of_numbers[index]
  return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
  try:
    result = item / denom
  except ZeroDivisionError:
    result = 0
    return result
  else:
    return result