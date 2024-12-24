numbers=[1,2,3,4,5]
while True:
 print("Menu:")
 print("  1.Append")
 print("  2.Insert")
 print("  3.Pop")
 print("  4.Remove")
 print("  5.Quit")
 choice=int(input("Choose an option: "))

 if choice==1:
  value=int(input("Enter a new value: "))
  numbers.append(value)
  print(f"Updated list: {numbers}")

 elif choice==2:
  index=int(input("Enter an index: "))
  value=int(input("Enter a new value: "))
  numbers.insert(index,value)
  print(f"Updated list: {numbers}")

 elif choice==3:
  numbers.pop()
  print(f"Updated list: {numbers}")

 elif choice==4:
  element=int(input("Enter an element to remove: "))
  numbers.remove(element)
  print(f"Updated list: {numbers}")

 elif choice==5:
  print("Have a nice day!")
  break
 else:
  print("Invalid input")
 