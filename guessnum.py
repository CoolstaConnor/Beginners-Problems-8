import random
number = random.randint(1, 100)
guess = int(input("Enter your guess: "))
while guess != number:
    if guess < number:
        print("Your guess was too low.")
    elif guess > number:
        print("Your guess was too high.")
    guess = int(input("Enter your guess: "))
print("Correct!")