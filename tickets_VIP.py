name=input("Please enter your name: ")
if name=='VIP':
  print("Enjoy the show for free!")
else:
  nb_tickets=int(input("How many tickets would you like? "))
  total=nb_tickets*15.50
  print("The total cost is {total}")
  print("Enjoy your tickets!")