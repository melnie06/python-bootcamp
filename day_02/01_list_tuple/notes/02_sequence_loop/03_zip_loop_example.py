names = ('Google', 'Jollibee', 'Nvidia')
balances = (10_000, 20_000, 3_000)
indices = (1, 2, 3)

for name, balance, index in zip(names, balances, indices):
    print(f"| {index}\t| {name}\t| {balance}\tPHP\t|")
