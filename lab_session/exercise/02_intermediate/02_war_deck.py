class Card:
    """Represents a playing card with a suit and rank."""

    def __init__(self, suit: str, rank: str):
        self.suit = suit  # e.g. "Hearts"
        self.rank = rank  # e.g. "K", "10", "A"

    def value(self) -> int:
        """
        Returns the numeric value of the card.
        TODO: Map ranks to values. 2-10 = 2-10, J = 11, Q = 12, K = 13, A = 14
        """
        pass

    def __str__(self) -> str:
        """Returns string representation like 'A of Spades'."""
        return f"{self.rank} of {self.suit}"


class Deck:
    """Represents a standard 52-card deck."""

    def __init__(self):
        self.cards: list = []  # list of Card objects
        self._create_deck()

    def _create_deck(self) -> None:
        """
        Populates the deck with 52 cards.
        TODO: Create cards for all combinations of 4 suits and 13 ranks.
        """
        pass

    def shuffle(self) -> None:
        """Randomly shuffles the deck."""
        # TODO: Shuffle self.cards
        pass

    def split(self) -> tuple:
        """
        Splits the deck into two halves.
        Returns:
            (list, list): Two lists of Card objects
        """
        pass


def play_round(card1: Card, card2: Card) -> int:
    """
    Compares two cards and determines the winner.
    Returns:
        1 if card1 wins
        2 if card2 wins
        0 if tie
    TODO: Compare using value()
    """
    pass


def play_game(deck1: list, deck2: list) -> None:
    """
    Main game loop. Runs 26 rounds and tracks score.
    TODO: Loop over both decks, compare cards, update scores, and print result.
    """
    pass


def main() -> None:
    """
    Game entry point.
    TODO:
    - Create deck
    - Shuffle
    - Split into two decks
    - Run play_game
    """
    pass


if __name__ == "__main__":
    main()
