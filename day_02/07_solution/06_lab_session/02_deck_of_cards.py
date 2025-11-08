import random


def create_deck():
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return [f'{rank}{suit}' for suit in suits for rank in ranks]


def draw_top(deck):
    return deck.pop(0)


def draw_bottom(deck):
    return deck.pop(-1)


def draw_random(deck):
    drawn = random.choice(deck)
    deck.remove(drawn)
    return drawn


def show(deck):
    print('Deck:', ', '.join(deck))


def add_top(deck, other):
    for card in other:
        deck.insert(0, card)


def add_bottom(deck: list[str], other: list[str]):
    deck.extend(other)


def add_random(deck, other):
    for card in other:
        idx = random.randint(0, len(deck))
        deck.insert(idx, card)


def load(filename: str) -> list[str]:
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]


def save(deck: list[str], filename: str):
    with open(filename, 'w') as f:
        for card in deck:
            f.write(card + '\n')
