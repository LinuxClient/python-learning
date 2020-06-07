def flatten(list):
  result = []

  for item in list:
    if isinstance(item, list):
      result += flatten(item)
    else:
      result.append(item)
  return result


array = [1, 2, [1, 2], [[1]]]
flattened = flatten(array)
print(flattened)
