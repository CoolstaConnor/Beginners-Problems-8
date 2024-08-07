import random
num = random.randint(1,100)
guess = int(input("Guess a number between 1-100!"))
def range():
    if guess < 1 or guess > 100:
        print("Pick a number within the range 1-100.")
        exit()
    if guess == num:
        print("Correct!")
        quit()
    if guess > num:
        print("Your guess is too high.")
    if guess < num:
        print("Your guess is too low.")
range()
while num != guess:
    guess = int(input("Guess a number between 1-100!"))
    range()