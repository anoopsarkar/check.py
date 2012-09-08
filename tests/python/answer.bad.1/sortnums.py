import sys

nums = [int(n) for n in list(sys.stdin)]
nums.sort()
for num in nums:
  if int(num) >= 16:
    sys.exit(1)
  print num
