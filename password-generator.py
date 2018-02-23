import random
import time
from termcolor import colored

print(colored("DISCLAIMER: This program is not to be used in real world applications. As such, the author takes responsibility in any adverse consequences that may arise from misusing the program. Although every measure has been taken to ensure the randomness of the generated passwords, there is no guarantee that they will as described. Use at your own risk.\n", 'red'))

charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789[]{}@#<>?%&"
amount = input("How many passwords would you like to generate? ")
length = input("How long would you like the passwords to be? ")
go_again = True

def gen():
  time.sleep(0.75)
  print("Generating", end='')
  time.sleep(0.5)
  print(".", end='')
  time.sleep(0.5)
  print(".", end='')
  time.sleep(0.5)
  print(".")
  time.sleep(2)
  print()
  print("Finished. Generated " + str(amount) +" random passwords of length " + str(length) + ".")
  print()
  time.sleep(1.5)

print()

while go_again:
  gen()
  for i in range(0, int(amount)):
    password = ""
    for x in range(0, int(length)):
      password += random.choice(charset)
    print("Password #" + str(i + 1) + ": " + password)
  
  again = input("\nWould you like to [generate] another set of passwords, [change] the parameters or [quit]?").lower()
  if again == "quit" or again == "q":
    go_again = False
  elif again == "change" or again == "c":
    amount = input("How many passwords would you like to generate? ")
    length = input("How long would you like the passwords to be? ")
    print()
  elif again == "generate" or again == "g":
    print()
  else:
    print()
    time.sleep(2)
    print(colored("Unable to validate response. To prevent possible Python attack, security protocols terminated the program.", 'red'))
    go_again = False
