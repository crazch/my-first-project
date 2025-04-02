import random

target = random.randint(1, 100)

while True:
  try:
    guess = int(input("Enter Number(1-100): "))
  except ValueError:
      print("Invalid!")
      continue

  if guess > target:
    print("Too High")
  elif guess < target:
    print("Too low")
  else:
    print("You Guessed it!")
    break