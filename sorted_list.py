list=[]
while True:
  number=int(input("Enter a number: ")) 
  if number==0:
    break
  else:
    list.append(number)
    print(f"Current list: {list}")
    print(f"Sorted list: {sorted(list)}")
