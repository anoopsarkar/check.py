import sys

for line_num, line in enumerate(sys.stdin, 1):
  print "%i\t%s" % (line_num, line),
