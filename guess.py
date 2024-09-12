import random
def guess_number_game(attempt_limit, minRange, maxRange):
    try:
        number_to_guess = random.randint(minRange, maxRange)
        correctly_guessed = False
        attempts = 0

        print("Welcome to the Number guessing game")

        print(f"I have selected a nunmber from {minRange} - {maxRange}, can you guess it? You have {attempt_limit} attempts to correctly guess my number.")

        while attempts < attempt_limit and not correctly_guessed:
            guess = int(input("Please add your guess: "))

            if guess == number_to_guess:
                attempts+=1
                correctly_guessed = True
                print(f"You have guessed my number {number_to_guess} correctly, congratulations! It took you {attempts} out of {attempt_limit} to guess my number!")
                return

            if guess > number_to_guess:
                print(f"Your guess {guess} is greater than the number I am thinking of")        
            elif guess < number_to_guess:
                print(f"Your guess {guess} is less than the number I am thinking of")

            attempts+=1
            print(f"Your guess {guess} was incorrect, please try again. You have {attempt_limit-attempts} attempts left to correctly guess my number")


        if attempts >= attempt_limit: 
            print(f"You have reached the limit of attempts you have to guess my number. My number was {number_to_guess}")
            return
        
    except ValueError:
        print("Invalid input, please input a valid number")
        return

guess_number_game(10, 1, 10)