class Counter:
    def __init__(self):
        self.value = 0


counter = Counter()
print("Counter:", counter.value)

counter.value += 1
print("Counter:", counter.value)
