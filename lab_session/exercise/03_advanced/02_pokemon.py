class Move:
    """
    Represents a Pokémon move.

    Attributes:
        name: The name of the move.
        type: The type of the move (e.g., Fire, Water).
        power: The base damage of the move.
        pp: The number of times the move can be used.
    """

    def __init__(self, name: str, type_: str, power: int, pp: int):
        # TODO: Initialize attributes
        pass

    @property
    def usable(self) -> bool:
        """
        Returns True if the move has PP remaining.
        """
        # TODO: Return True if PP > 0
        pass


class Pokemon:
    """
    Represents a Pokémon and its stats.

    Attributes:
        name: The Pokémon's name.
        types: A list of types (e.g., ["Fire"], ["Water", "Flying"]).
        hp: Current health points.
        attack: Physical attack stat.
        defense: Physical defense stat.
        sp_attack: Special attack stat.
        sp_defense: Special defense stat.
        speed: Determines turn order.
        moves: A list of Move objects the Pokémon can use.
    """

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
            moves: list[Move],
    ):
        # TODO: Store all the provided stats
        pass

    def use(self, move: Move, other: 'Pokemon') -> None:
        """
        Use a move against another Pokémon.

        Rules:
        - If move type is one of the following:
          ["Normal", "Fighting", "Flying", "Poison", "Ground", "Rock",
           "Bug", "Steel", "Ice", "Dragon", "Dark"]
          → Use this formula:
            damage = (move.power * self.attack) / other.defense
        - Otherwise:
            damage = (move.power * self.sp_attack) / other.sp_defense

        - Reduce target's HP by damage
        - Subtract 1 from move.pp

        Notes:
        - Don't apply damage if the move has 0 PP left.
        """
        # TODO: Implement move logic based on type and stats
        pass

    @property
    def knocked_out(self) -> bool:
        """
        Returns True if the Pokémon has 0 or less HP.
        """
        # TODO: Return True if hp <= 0
        pass


# --------------------------
# Step 3: Battle Simulation
# --------------------------

def battle(player: Pokemon):
    """
    Runs a basic turn-based battle.

    Steps:
    1. Randomly generate an enemy Pokémon with random moves.
    2. Let the player choose a move to use.
        - If all moves have 0 PP, skip player's turn.
    3. Let the enemy randomly pick and use a usable move.
    4. Repeat until one Pokémon is knocked out.
    5. Print result (win or lose).

    Tips:
    - Use `input()` to let user select a move.
    - Use `random.choice()` for enemy move selection.
    - Print health after each round for clarity.
    """
    # TODO: Build the game loop following the rules above
    pass


# --------------------------
# Optional Challenge Section
# --------------------------

"""
CHALLENGES (If you want extra XP):

1. Multiple Rounds
    - Can you let the player fight a series of enemy Pokémon?
    - Each round ends when one Pokémon is knocked out.
    - Heal the player a bit after each win?

2. Random Pokémon and Moves
    - Load data from `pokedex.json` and `moves.json`.
    - Randomly select Pokémon and assign them appropriate moves.

3. Damage Randomization
    - Add randomness to damage: e.g., multiply by a random float between 0.85 and 1.0.
    - Makes battles less predictable.

4. Type Effectiveness (Bonus Hard Mode)
    - Add basic type effectiveness logic (e.g., Fire > Grass).
    - You'll need a type effectiveness table (dict of dicts or matrix).
"""

# --------------------------
# Main Game Entry Point
# --------------------------

if __name__ == "__main__":
    # TODO: Let user choose a Pokémon and assign 4-6 moves manually or randomly.
    # Example:
    # - Load data (optional)
    # - Build a Pokemon object
    # - Call battle(player)

    # Placeholder example to test code later
    # player = Pokemon("Bulbasaur", ["Grass", "Poison"], 100, 49, 49, 65, 65, 45, [])
    # battle(player)
    pass
