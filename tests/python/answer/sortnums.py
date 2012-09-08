import sys

nums = [int(n) for n in list(sys.stdin)]
nums.sort()
for num in nums:
  print num
