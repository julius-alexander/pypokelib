"""Gimme a sec, I'm thinking..."""
from typing import NamedTuple
from dataclasses import dataclass, field


# * Option 1 - Standalone NamedTuple for each Pokemon
# BasePokemon = NamedTuple(
#     "BasePokemon",
#     [
#         ('name', str),
#         ("base_stats", dict[str, int]),
#         ("types", list[str]),
#         ("base_exp", int),
#         ("growth_rate", str),
#         ("tmhm_learnset", list[str]),
#     ],
# )


# * Option 2 - Dataclass for each Pokemon
class BasePokemonClass:
    def __init__(self) -> None:
        """Base Class for all Pokemon"""
        self.name: str
        self.base_stats: dict[str, int]
        self.types: list[str]
        self.base_exp: int = 0
        self.growth_rate: str = ""
        self.tmhm_learnset: list[str]


class Abra:
    """Base Class for all Abra"""

    def __init__(self):
        # intended to be used as "private variables"
        # ! REPLACE ALL OF THE FOLLOWING WITH CONSTANTS (EVENTUALLY)
        self.__dex_num = 63
        self.__name = "Abra"
        self.__base_stats = {"hp": 25, "atk": 20, "def": 15, "spe": 90, "spc": 105}
        self.__types = ["Psychic", ""]
        self.__base_exp = 0
        self.__growth_rate = "Medium Slow"
        self.__tmhm_learnset = ["tm01", ..., "tm50"]

        # default values, intended to be used as "public variables"
        self.level = 1
        self.current_stats = self.__base_stats
        self.learned_moves = ["Teleport"]
        self.current_moves = ["Teleport", "", "", ""]
        self.nature = "Hardy"

    def get_dex_num(self):
        """Return the Pokedex number of the Pokemon"""
        return self.__dex_num

    def get_name(self):
        """Return the name of the Pokemon"""
        return self.__name

    def get_base_stats(self):
        """Return the base stats of the Pokemon"""
        return self.__base_stats

    def get_types(self):
        """Return the type(s) of the Pokemon"""
        return self.__types

    def get_base_exp(self):
        """Return the base experience of the Pokemon"""
        return self.__base_exp

    def get_growth_rate(self):
        """Return the growth rate of the Pokemon"""
        return self.__growth_rate

    def get_tmhm_learn_set(self):
        """Return the TM/HM learnset of the Pokemon"""
        return self.__tmhm_learnset

    def __repr__(self) -> str:
        return (
            f"{self.__name} (Lv.{self.level})\n"
            f"Nature: {self.nature}\n"
            f"Stats: {self.current_stats}\n"
            f"Types: {self.__types[0]} {self.__types[1]}\n"
            f"Moves: {self.current_moves[0]} {self.current_moves[1]} \
                     {self.current_moves[2]} {self.current_moves[3]}\n"
            f"TM/HM Learnset: {self.__tmhm_learnset}\n"
        )


my_abra = Abra()
print(my_abra)

# Abra = BasePokemon(
#     "Abra",
#     {"hp": 25, "atk": 20, "def": 15, "spe": 90, "spc": 105},
#     ["psychic"],
#     0,
#     "medium slow",
#     ["tm01"],
# )


# uhhhh = {"hp": 25, "atk": 20, "def": 15, "spe": 90, "spc": 105}
# my_abra = Abra(uhhhh, ["psychic"], 0, "medium slow", ["tm01"])

# * Option 2 - One NamedTuple for all Pokemon
# Pokemon = NamedTuple('Pokemon',
#                      [
#                         ('base_stats', Base_Stats),
#                         ('types', list[str]),
#                         ('base_exp', int),
#                         ('growth_rate', str),
#                         ('tmhm_learnset', list[str])
#                     ]
#                 )
