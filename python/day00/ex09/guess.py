import random

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number, in less than 10 attempts.")
print("Type 'exit' to end the game.")
print("Good luck!")


ans = random.randint(1, 99)
guess = 0
n = 1
while n <= 10:
    print("\nWhat's your guess between 1 and 99?")
    guess = input(">> ")
    try:
        guess = int(guess)
    except ValueError:
        if guess == "exit":
            print("Too bad!")
            break
        if guess == "":
            print("Enter a number.")
        else:
            print("That's not a number.")
    else:
        if guess > ans:
            print("Too high!")
        elif guess < ans:
            print("Too low!")
        else:
            if n == 1:
                print("hmm, soothsayer? or some kind of luck?")
            elif ans == 42:
                print("Yeaaaaaaah")
            else:
                print("Congrats, you've got it!")
                print(f"You won in {n} attempts.")
            n = 10
        n += 1
