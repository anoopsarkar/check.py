import sys

if len(sys.argv) != 3:
  print >> sys.stderr, "usage: %s CHAR REPLACEMENT" % (sys.argv[0])
  sys.exit(1)
to_repace = sys.argv[1]
replacement = sys.argv[2]

while True:
  char = sys.stdin.read(1)
  if not char:
    break
  if char == to_repace:
    char = replacement
  sys.stdout.write(char)
