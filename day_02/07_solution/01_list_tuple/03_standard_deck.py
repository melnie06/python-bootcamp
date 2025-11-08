ranks = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
suits = ("Hearts", "Diamonds", "Clubs", "Spades")
# Print every possible pairing of ranks and suits

for suit in suits:
    for rank in ranks:
        print(f"{rank} of {suit}")
