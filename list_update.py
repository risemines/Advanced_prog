numbers=[1,2,3,4,5]
index=0
while True:
  index=int(input("Enter an index: "))
  if index==-1 and index<0:
    print("Invalid index")
    break
  value=int(input("Enter a new value: "))
  numbers[index]=value
  print(numbers)