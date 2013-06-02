import sys
from namehandler import get_initials

def main():
  f = open(sys.argv[1])
  for l in f:
     print get_initials(l)
  f.close()


if __name__ == "__main__":
   main()
