def get_initials(full_name):
   names = full_name.split()
   initial = ''
   i = 0
   while i < len(names):
      initial=initial+(names[i][0]) #From each part of the name we get the first letter
      i = i+1
   return initial
