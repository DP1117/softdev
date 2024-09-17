def sum2(nums):
  sum = 0
  i = 0
  for num in nums:
    if i == 2:
      break
    sum += num
    i += 1
  return sum