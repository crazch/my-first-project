import random

target = random.randint(1, 100)

chances = 10
while True:
  print(f"You Have {chances} chances left")
  try:
    guess = int(input("Enter Number(1-100): "))
  except ValueError:
      print("Invalid!")
      continue
  chances -= 1

  if guess > target:
    print("Too High")
  elif guess < target:
    print("Too low")
  else:
    print("You Guessed it!")
    break
  
  if chances == 0:
    print("No Chances Left")
    break