total=int(input("Total amount: "))
nb_items=int(input("Number of items: "))
day=input("Day of the week: ")
if day in ['saturday', 'sunday']:
  discount=0.20
else:
  discount=0.10
if nb_items>5:
  discount=discount+0.05
price=total*(1-discount)
print(f"Total price after discount {price}")