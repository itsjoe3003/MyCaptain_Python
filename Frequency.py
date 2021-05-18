'''To find the frequency of characters in a string'''

def most_frequent(string):              #definition of the most_frequent() function

  dict1 = {}
  for n in string:
    keys = dict1.keys()
    if n in keys:
      dict1[n] += 1
    else:
      dict1[n] = 1
    
  
  #temporary typecasting to list for easy sorting of the elements
  temp_list = list(dict1.items())       

  temp = 0                         

#loop to sort the elements in decreasing order of frequency of characters
  for x in range(0,len(temp_list)):     
    for y in range(0,len(temp_list)-1):
      if (temp_list[y][1]<temp_list[y+1][1]):
        temp = temp_list[y]
        temp_list[y] = temp_list[y+1]
        temp_list[y+1] = temp

  
  #displaying the elements in dictionary format
  print("Frequency of each characters(in decreasing order): \n{}".format(dict(temp_list)))    
    


string = input("Enter a string: ")  
most_frequent(string)                      #function call