def get_initials(line):
    names = line.split()
    initial = ''
    i = 0
    while i < len(names):
       if not names[i][0].islower():
           initial=initial+(names[i][0])
           i = i+1
       else:
           i = i+1
    return initial

if __name__ == "__main__":
    print get_initials("George Adams")
