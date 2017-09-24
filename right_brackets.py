counter = 0
x = 0
array = input("Write your brackets ")

for x in range(len(array)):
  if(counter<0):
    break
  elif(array[x] == ")"):
    counter = counter-1
  elif (array[x] == "("):
    counter = counter+1
  x=x+1
  
if (counter !=0):
  print("NO")
else:
  print("YES")