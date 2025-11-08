import random


class Card:
    """Represents a playing card with a suit and rank."""

    def __init__(self, suit: str, rank: str):
        self.suit = suit  # e.g. "Hearts"
        self.rank = rank  # e.g. "K", "10", "A"

    def value(self) -> int:
        """
        Returns the numeric value of the card.
        2-10 = 2-10, J = 11, Q = 12, K = 13, A = 14
        """
        rank_values = {
            "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
            "8": 8, "9": 9, "10": 10,
            "J": 11, "Q": 12, "K": 13, "A": 14
        }
        return rank_values[self.rank]

    def __str__(self) -> str:
        """Returns string representation like 'A of Spades'."""
        return f"{self.rank} of {self.suit}"


class Deck:
    """Represents a standard 52-card deck."""

    def __init__(self):
        self.cards: list[Card] = []
        self._create_deck()

    def _create_deck(self) -> None:
        """Creates cards for all combinations of 4 suits and 13 ranks."""
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
                 "J", "Q", "K", "A"]

        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self) -> None:
        """Randomly shuffles the deck."""
        random.shuffle(self.cards)

    def split(self) -> tuple[list[Card], list[Card]]:
        """
        Splits the deck into two halves.
        Returns:
            (list, list): Two lists of Card objects
        """
        half = len(self.cards) // 2
        return self.cards[:half], self.cards[half:]


def play_round(card1: Card, card2: Card) -> int:
    """
    Compares two cards and determines the winner.
    Returns:
        1 if card1 wins
        2 if card2 wins
        0 if tie
    """
    if card1.value() > card2.value():
        return 1
    elif card2.value() > card1.value():
        return 2
    else:
        return 0


def play_game(deck1: list[Card], deck2: list[Card]) -> None:
    """
    Main game loop. Runs 26 rounds and tracks score.
    """
    score1 = 0
    score2 = 0

    for i in range(26):
        card1 = deck1[i]
        card2 = deck2[i]

        print(f"Round {i + 1}:")
        print(f"  Player 1: {card1}")
        print(f"  Player 2: {card2}")

        result = play_round(card1, card2)

        if result == 1:
            print("  → Player 1 wins the round!\n")
            score1 += 1
        elif result == 2:
            print("  → Player 2 wins the round!\n")
            score2 += 1
        else:
            print("  → It's a tie!\n")

    print("Game Over!")
    print(f"Final Score: Player 1 = {score1}, Player 2 = {score2}")

    if score1 > score2:
        print("Player 1 wins the game!")
    elif score2 > score1:
        print("Player 2 wins the game!")
    else:
        print("It's a draw!")


def main() -> None:
    """Game entry point."""
    deck = Deck()
    deck.shuffle()

    deck1, deck2 = deck.split()
    play_game(deck1, deck2)


if __name__ == "__main__":
    main()
