"""Defines Pokemon class and its methods"""
from typing import NamedTuple

from pypokelib.generation1.constants.move_consts import *
from .poke_lookup_table import POKEDEX, get_mon

# * Option 2 - Base Class for each Pokemon
class Pokemon:
    """Base Class for all Pokemon"""

    def __init__(self, species_or_dex: str | int):
        """Initialize the Pokemon class"""
        if isinstance(species_or_dex, str):
            self._name = str((species_or_dex).title())
            self._dex_num = get_mon(self._name)

        elif isinstance(species_or_dex, int):
            if species_or_dex < 1 or species_or_dex > 151:
                raise ValueError("Invalid Pokedex number.\n" \
                                f"Generation 1 Pokedex numbers range from 1 to 151.")
            self._dex_num = species_or_dex
            self._name = get_mon(self._dex_num)
        
        else:
            raise TypeError("Parameter must be of type str or int.")

        # intended to be used as "private variables"
        self._base_stats = POKEDEX[self._dex_num].base_stats
        self._types = POKEDEX[self._dex_num].types
        self._base_exp = POKEDEX[self._dex_num].base_exp
        self._growth_rate = POKEDEX[self._dex_num].growth_rate
        self._tmhm_learnset = POKEDEX[self._dex_num].tmhm_learnset

        # default values, intended to be used as "public variables"
        self.level = 1
        self.current_stats = self._base_stats
        self.learned_moves: tuple[BaseMoves] = POKEDEX[self._dex_num].tmhm_learnset
        self.current_moves = [NO_MOVE, NO_MOVE, NO_MOVE, NO_MOVE]
        self.nature = "Hardy"
        self.set_base_moves()
    
    def set_base_moves(self) -> None:
        """Set the base (Lvl. 1) moves of the Pokemon"""
        if len(self.learned_moves) == 0:
            self.current_moves = [NO_MOVE, NO_MOVE, NO_MOVE, NO_MOVE]
        elif len(self.learned_moves) == 1:
            self.current_moves = [self.learned_moves[0], NO_MOVE, NO_MOVE, NO_MOVE]
        elif len(self.learned_moves) == 2:
            self.current_moves = [self.learned_moves[0], self.learned_moves[1], NO_MOVE, NO_MOVE]
        elif len(self.learned_moves) == 3:
            self.current_moves = [self.learned_moves[0], self.learned_moves[1], self.learned_moves[2], NO_MOVE]
        elif len(self.learned_moves) >= 4:
            self.current_moves = [self.learned_moves[0], self.learned_moves[1], self.learned_moves[2], self.learned_moves[3]]


    def get_dex_num(self) -> int:
        """Return the Pokedex number of the Pokemon"""
        return self._dex_num

    def get_name(self) -> str:
        """Return the name of the Pokemon"""
        return self._name

    def get_base_stats(self) -> NamedTuple:
        """Return the base stats of the Pokemon"""
        return self._base_stats

    def get_types(self) -> list[str]:
        """Return the type(s) of the Pokemon"""
        return self._types

    def get_base_exp(self) -> int:
        """Return the base experience of the Pokemon"""
        return self._base_exp

    def get_growth_rate(self) -> str:
        """Return the growth rate of the Pokemon"""
        return self._growth_rate

    def get_tmhm_learn_set(self) -> list[str]:
        """Return the TM/HM learnset of the Pokemon"""
        return self._tmhm_learnset

    def get_nature(self):
        """Return the nature of the Pokemon"""
        return self.nature
    
    def reset_stats(self) -> None:
        """Reset the current stats of the Pokemon to its base stats"""
        self.current_stats = self._base_stats

    def __repr__(self) -> str:
        return (
            f"{self._name} (Lv.{self.level})\n"
            f"Stats: {self.current_stats}\n"
            f"Nature: {self.nature}\n"
            f"Types: {self._types[0]} {self._types[1]}\n"
            f"Moves: [{self.current_moves[0].name}] [{self.current_moves[1].name}] " \
            f"[{self.current_moves[2].name}] [{self.current_moves[3].name}]\n"
        )
