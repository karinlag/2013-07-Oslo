areacodes = {} # Create an empty dictionary
f = open("phonenums.txt") # Open the text file
for line in f: # iterate through the text file, one line at a time (think of the file as a list of lines)
    if "4" in line:
        continue
    ac = line.split('-')[0] # Split phone number, first element is the area code
    if not ac in areacodes: # Check if it is already in the dictionary
      areacodes[ac] = 1 # If not, add it to the dictionary
    else:
      areacodes[ac] += 1 # Add one to the dictionary entry

#print areacodes # Print the answer

for ac, nos in areacodes.iteritems():
    print ac + "\t" + str(nos)
