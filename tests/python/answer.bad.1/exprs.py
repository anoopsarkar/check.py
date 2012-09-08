import sys

valid_ops = ["-", "*", "%"]

for line_num, line in enumerate(sys.stdin, 1):
  parts = line.split()
  print >> sys.stderr, line_num, parts
  if len(parts) != 3:
    raise ValueError()
  arg1 = int(parts[0])
  arg2 = int(parts[2])
  op = parts[1]
  if op not in valid_ops:
    raise ValueError()
  print eval("%i %s %i" % (arg1, op, arg2))
