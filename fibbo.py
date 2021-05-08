#initializing the first two terms of the series
first = 0
second = 1

#getting the series limit from user
num = int(input("Enter how many numbers should be displayed from the series: "))

#initializing counter variable
x = 0

#loop to display the successive terms of the fibonacci series
while x<num:
  print(first,end=" ")
  next = first + second
  first = second
  second = next
  x+=1

