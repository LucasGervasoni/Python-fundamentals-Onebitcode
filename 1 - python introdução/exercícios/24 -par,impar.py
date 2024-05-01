def check_num(numbers):
  pairs = []
  odd = []
  for number in numbers:
    if number % 2 == 0:
      pairs.append(number)
    else:
      odd.append(number)
  return pairs, odd
print(check_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))