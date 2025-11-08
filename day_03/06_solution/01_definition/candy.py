class Candy:
    def __init__(self, flavor):
        self.flavor = flavor


def __eq__(self, other):
    return self.flavor == other.flavor


choco1 = Candy("chocolate")
choco2 = Candy("chocolate")
milk = Candy("milk")

print(choco1 == milk)
print(choco1 == choco2)
