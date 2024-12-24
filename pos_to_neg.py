while True:
 N=int(input("Enter a positive number: "))
 if N>=0:
   break
 else:
   print("Try again.")
for i in range(-N,N+1):
  if i!=0:
    print(i)