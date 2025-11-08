import json
import random
from enum import Enum
from typing import Optional


class NoMorePP(ValueError):
    """Raised when there is no more PP for a move."""
    pass


class MoveMiss(ValueError):
    """Raised when a move misses."""
    pass


class Type(Enum):
    NORMAL = "Normal"
    FIRE = "Fire"
    WATER = "Water"
    ELECTRIC = "Electric"
    GRASS = "Grass"
    ICE = "Ice"
    FIGHTING = "Fighting"
    POISON = "Poison"
    GROUND = "Ground"
    FLYING = "Flying"
    PSYCHIC = "Psychic"
    BUG = "Bug"
    ROCK = "Rock"
    GHOST = "Ghost"
    DRAGON = "Dragon"
    DARK = "Dark"
    STEEL = "Steel"
    FAIRY = "Fairy"


class Move:
    """Represents a Pokémon move."""

    PHYSICAL_TYPES = {
        Type.NORMAL, Type.FIGHTING, Type.FLYING, Type.POISON, Type.GROUND,
        Type.ROCK, Type.BUG, Type.STEEL, Type.ICE, Type.DRAGON, Type.DARK
    }

    def __init__(self, name: str, type_: str, power: int, pp: int, accuracy: int):
        self.name = name
        self.type = type_
        self.power = power
        self.pp = pp
        self.accuracy = accuracy

    @property
    def usable(self) -> bool:
        return self.pp > 0

    @property
    def is_physical_type(self) -> bool:
        return Type(self.type) in self.PHYSICAL_TYPES

    def hits(self) -> bool:
        return random.random() * 100 < self.accuracy

    @classmethod
    def from_dict(cls, move: dict[str, int | str]) -> 'Move':
        return cls(
            name=move["ename"],
            type_=move["type"],
            power=move.get("power", 0) or 0,
            pp=move.get("pp", 0) or 0,
            accuracy=move.get("accuracy", 100) or 100,
        )


class Pokemon:
    def __init__(
            self,
            name: str,
            types: list[str],
            hp: int,
            attack: int,
            defense: int,
            sp_attack: int,
            sp_defense: int,
            speed: int,
            moves: Optional[list[Move]] = None
    ):
        self.name = name
        self.types = types
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.sp_attack = sp_attack
        self.sp_defense = sp_defense
        self.speed = speed
        self.moves = moves or []

    def use(self, move: Move, other: 'Pokemon', type_chart: dict) -> None:
        if not move.usable:
            raise NoMorePP()

        multiplier = random.uniform(0.85, 1.15)
        type_multiplier = 1.0
        move_type_chart = type_chart.get(move.type, {})

        for t in other.types:
            type_multiplier *= move_type_chart.get(t, 1.0)

        stat = self.attack if move.is_physical_type else self.sp_attack
        defense = other.defense if move.is_physical_type else other.sp_defense
        base_damage = move.power * stat
        damage = base_damage * multiplier * type_multiplier / defense

        other.hp -= damage
        move.pp -= 1

        if type_multiplier > 1:
            print("It's super effective! (ง🔥Д🔥)ง")
        elif type_multiplier < 1:
            print("It's not very effective... (－‸ლ)")

    def regenerate(self, amount: int = 20) -> int:
        regen = min(amount, self.max_hp - self.hp)
        self.hp += regen
        return regen

    @property
    def knocked_out(self) -> bool:
        return self.hp <= 0

    @classmethod
    def from_dict(cls, pokemon: dict[str, int | str | dict], moves: Optional[list[Move]] = None) -> 'Pokemon':
        return cls(
            name=pokemon['name']['english'],
            types=pokemon['type'],
            hp=pokemon['base']['HP'],
            attack=pokemon['base']['Attack'],
            defense=pokemon['base']['Defense'],
            sp_attack=pokemon['base']['Sp. Attack'],
            sp_defense=pokemon['base']['Sp. Defense'],
            speed=pokemon['base']['Speed'],
            moves=moves
        )


class Battle:
    def __init__(self, player: Pokemon, type_chart: dict):
        self.player = player
        self.enemy = random_pokemon()
        self.type_chart = type_chart

    def player_turn(self):
        print(f"\nYour Pokémon: {self.player.name} (HP: {round(self.player.hp, 1)})")
        print(f"Enemy Pokémon: {self.enemy.name} (HP: {round(self.enemy.hp, 1)})")

        usable_moves = [m for m in self.player.moves if m.usable]

        if not usable_moves:
            print(f"{self.player.name} has no usable moves and skips a turn!")
            return

        print("\nChoose your move:")
        for i, move in enumerate(self.player.moves):
            print(
                f"{i + 1}. {move.name} (Type: {move.type}, PP: {move.pp}, Power: {move.power}, Acc: {move.accuracy}%)")

        while True:
            try:
                choice = int(input("Enter move number: ")) - 1
                if 0 <= choice < len(self.player.moves):
                    selected_move = self.player.moves[choice]
                    print(f"\n{self.player.name} used {selected_move.name}!")
                    if not selected_move.usable:
                        raise NoMorePP()
                    if not selected_move.hits():
                        selected_move.pp -= 1
                        raise MoveMiss()
                    self.player.use(selected_move, self.enemy, self.type_chart)
                    return
                else:
                    print("Invalid move number.")
            except ValueError:
                print("Please enter a valid number.")
            except NoMorePP:
                print("That move has no more PP!")
            except MoveMiss:
                print(f"{self.player.name}'s move missed!")
                return

    def enemy_turn(self):
        usable_moves = [m for m in self.enemy.moves if m.usable]
        if not usable_moves:
            print(f"\nEnemy {self.enemy.name} has no usable moves!")
            return

        move = random.choice(usable_moves)
        print(f"\nEnemy {self.enemy.name} used {move.name}!")
        if move.hits():
            self.enemy.use(move, self.player, self.type_chart)
        else:
            move.pp -= 1
            print(f"Enemy {self.enemy.name}'s {move.name} missed!")

    def run(self):
        print(f"\nA wild {self.enemy.name} appeared!\n")
        while not self.enemy.knocked_out and not self.player.knocked_out:
            self.player_turn()
            if self.enemy.knocked_out:
                print(f"\nEnemy {self.enemy.name} fainted! You win!")
                return
            self.enemy_turn()
            if self.player.knocked_out:
                print(f"\n{self.player.name} fainted! You lose!")
                return


def available_moves(moves_database: list[Move], types: list[str]) -> list[Move]:
    return [move for move in moves_database if move.type in types]


def load_moves(filepath: str = "moves.json") -> list[Move]:
    with open(filepath, encoding='utf-8') as file:
        return [Move.from_dict(move) for move in json.load(file)]


def load_pokemon(filepath: str = "pokedex.json") -> list[Pokemon]:
    with open(filepath, encoding='utf-8') as file:
        return [Pokemon.from_dict(p) for p in json.load(file)]


def load_type_chart(filepath: str = "type_chart.json") -> dict:
    with open(filepath, encoding="utf-8") as file:
        return json.load(file)


def random_pokemon(move_db_fp: str = "moves.json", poke_db_fp: str = "pokedex.json") -> Pokemon:
    pokemon_database = load_pokemon(poke_db_fp)
    move_database = load_moves(move_db_fp)
    pokemon = random.choice(pokemon_database)
    compatible_moves = available_moves(move_database, pokemon.types)
    move_count = random.randint(4, 6)
    pokemon.moves = random.sample(compatible_moves, k=min(move_count, len(compatible_moves)))
    return pokemon


def main():
    print("Welcome to the Python Pokémon Battle Simulator!")

    type_chart = load_type_chart()
    move_database = load_moves()
    pokemon_database = load_pokemon()
    random.shuffle(pokemon_database)

    print("\nChoose your Pokémon:")
    for i, p in enumerate(pokemon_database[:10]):
        print(f"{i + 1}. {p.name} (Types: {', '.join(p.types)})")

    while True:
        try:
            choice = int(input("Enter Pokémon number: ")) - 1
            if 0 <= choice < len(pokemon_database[:10]):
                player_pokemon = pokemon_database[choice]
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a number.")

    compatible = available_moves(move_database, player_pokemon.types)
    move_count = random.randint(4, 6)
    player_pokemon.moves = random.sample(compatible, k=min(move_count, len(compatible)))

    print(f"\nYou chose {player_pokemon.name} with the following moves:")
    for m in player_pokemon.moves:
        print(f"- {m.name} (Type: {m.type}, Power: {m.power}, Accuracy: {m.accuracy}%)")

    while not player_pokemon.knocked_out:
        battle = Battle(player_pokemon, type_chart)
        battle.run()
        if not player_pokemon.knocked_out:
            regen = player_pokemon.regenerate()
            print(f"\n{player_pokemon.name} regains {round(regen, 1)} HP. (Current HP: {round(player_pokemon.hp, 1)})")


if __name__ == "__main__":
    main()
