"""Defines Pokemon class and its methods"""
import sys
import poke_lookup_table as plt
import time

sys.path.append("./generation1/constants")

# * Option 2 - Base Class for each Pokemon
class Pokemon:
    """Base Class for all Pokemon"""

    def __init__(self, species_or_dex: str | int):
        """Initialize the Pokemon class"""
        if isinstance(species_or_dex, str):
            self._name = str((species_or_dex).title())
            self._dex_num = plt.get_mon(self._name)
        elif isinstance(species_or_dex, int):
            self._dex_num = species_or_dex
            self._name = plt.get_mon(self._dex_num)    # * not sure yet!
        else:
            raise TypeError("Parameter must be of type str or int.")

        # intended to be used as "private variables"
        self._base_stats = plt.POKEDEX[self._dex_num].base_stats
        self._types = plt.POKEDEX[self._dex_num].types
        self._base_exp = plt.POKEDEX[self._dex_num].base_exp
        self._growth_rate = plt.POKEDEX[self._dex_num].growth_rate
        self._tmhm_learnset = plt.POKEDEX[self._dex_num].tmhm_learnset

        # default values, intended to be used as "public variables"
        self.level = 1
        self.current_stats = self._base_stats
        self.learned_moves = plt.POKEDEX[self._dex_num].tmhm_learnset[0]
        self.current_moves = [plt.POKEDEX[self._dex_num].tmhm_learnset, "-", "-", "-"]
        self.nature = "Hardy"

    def get_dex_num(self):
        """Return the Pokedex number of the Pokemon"""
        return self._dex_num

    def get_name(self):
        """Return the name of the Pokemon"""
        return self._name

    def get_base_stats(self):
        """Return the base stats of the Pokemon"""
        return self._base_stats

    def get_types(self):
        """Return the type(s) of the Pokemon"""
        return self._types

    def get_base_exp(self):
        """Return the base experience of the Pokemon"""
        return self._base_exp

    def get_growth_rate(self):
        """Return the growth rate of the Pokemon"""
        return self._growth_rate

    def get_tmhm_learn_set(self):
        """Return the TM/HM learnset of the Pokemon"""
        return self._tmhm_learnset

    def get_nature(self):
        """Return the nature of the Pokemon"""
        return self.nature

    def __repr__(self) -> str:
        return (
            f"{self._name} (Lv.{self.level})\n"
            f"Stats: {self.current_stats}\n"
            f"Nature: {self.nature}\n"
            f"Types: {self._types[0]} {self._types[1]}\n"
            f"Moves: {self.current_moves[0]} {self.current_moves[1]} " \
            f"{self.current_moves[2]} {self.current_moves[3]}\n" \
            f"TM/HM Learnset: {self._tmhm_learnset}\n"
        )


def call_str():
    time1 = time.time()
    for i in range(500_000):
        my_bulbasaur = Pokemon("Bulbasaur")
    time2 = time.time()
    return time2 - time1

def call_int():
    time1 = time.time()
    for i in range(500_000):
        my_bulbasaur = Pokemon(1)
    time2 = time.time()
    return time2 - time1
