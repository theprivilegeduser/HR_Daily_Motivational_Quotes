import random

quotes = [
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "Success is not the key to happiness. Happiness is the key to success. – Albert Schweitzer",
    "Your limitation—it’s only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Dream it. Wish it. Do it.",
    # Add more quotes here
]

def get_random_quote():
    return random.choice(quotes)

if __name__ == "__main__":
    print(get_random_quote())
