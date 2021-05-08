list1 = [12,-7,5,64,-14]
list2 = []
count=0
for x in list1:
  if(x>0):
    list2.insert(count,x)
    count+=1
  else:
    continue

print("Positive numbers of this list are: {}".format(list2))