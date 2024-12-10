nb=int(input("Number: "))
if nb%3==0:
  print("Fizz")
  if nb%5==0:
    print("FizzBuzz")
elif nb%5==0:
  print("Buzz")
