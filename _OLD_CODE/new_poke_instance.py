"""Creates new instances of the PokeMon class."""
from dataclasses import dataclass

#pylint: disable=line-too-long


@dataclass(frozen=True)
class Move:
    """Creates Move instance with the following attributes:"""
    name: str
    type: str
    category: str
    power: int
    accuracy: int
    pp_amt: int


@dataclass(frozen=False)
class Stats:
    """"""

    base_stats: dict[str, int]
    current_stats: dict[str, int]
    current_ivs: dict[str, int]
    current_evs: dict[str, int]
    nature: str


@dataclass(frozen=False)
class PokeMon:
    """Creates PokeMon instance with the following attributes:
    species: str
    level: int
    stats: dict
    current_stats: dict
    moves: list
    type: list"""

    species: str
    nickname: str
    level: int
    stats: Stats
    moves: list[str]
    type: list[str]

    def __str__(self):
        """Returns PokeMon instance's species."""
        return f"species: {self.species}\n " \
                "Level: {self.level}\n " \
                "Nature: {self.nature}\n " \
                "Type: {self.type}\n " \
                "Moves: {self.moves}\n " \
                "Stats: {self.stats}"


pokemon1 = PokeMon(
    "Charmander",
    "Adamant",
    5,
    Stats(
        {"hp": 39, "attack": 52, "defense": 43, "special_attack": 60, "special_defense": 50, "speed": 65},
        {"hp": 39, "attack": 52, "defense": 43, "special_attack": 60, "special_defense": 50, "speed": 65},
        {"hp": 31, "attack": 31, "defense": 31, "special_attack": 31, "special_defense": 31, "speed": 31},
        {"hp": 0, "attack": 0, "defense": 0, "special_attack": 0, "special_defense": 0, "speed": 0},
    ),
    ["Scratch", "Growl", "Ember", "Smokescreen"],
    ["Fire"],
)

print(pokemon1)


def set_stat(stat_to_set: str, level:int, stat_iv: int) -> int:
    """Updates (or initializes) HP stat of PokeMon instance."""
    if stat_to_set == "hp":
        return floor(0.01 * (2 * stat_to_set + stat_iv + 100) * level) + level + 10
    else:
        return floor(0.01 * (2 * stat_to_set + stat_iv + 100) * level) + 5
    