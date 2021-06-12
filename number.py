print("This is hit number game")

answer = 1
guess = input()
trial = 1

while answer != guess:
  trial += 1
  print("You input wrong number")
  print("next challenge?")
  guess = input()
else:
  print("You good")
  print("trial_number is")
  print(trial)