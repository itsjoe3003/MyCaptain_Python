string = input("Enter a string: ")

dict1 = {}
for n in string:
  keys = dict1.keys()
  if n in keys:
    dict1[n] += 1
  else:
    dict1[n] = 1
    
print("Frequency of each characters: {}".format(dict1))
    