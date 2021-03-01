import random


# GET guess
def get_guess():
    return list(input("What's your guess?"))

# generate computer code


def generate_code():
    digits = [str(num) for num in range(10)]

    # shuffle to grab first three
    random.shuffle(digits)

    return digits[:3]


# generate clues

def generate_clues(code, user_guess):
    if user_guess == code:
        return "CODE CRACKED"

    clues = []

    for ind, num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("match")
        elif num in code:
            clues.append("close")

    if clues == []:
        return ["Nope"]
    else:
        return clues


# run game logic

print("Welcome code breaker")

secret_code = generate_code()

clue_report = []

while clue_report != "CODE CRACKED":
    guess = get_guess()
    clue_report = generate_clues(guess, secret_code)
    print("here is the result:")
    for clue in clue_report:
        print(clue)
