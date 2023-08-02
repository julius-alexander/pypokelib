"""Gimme a sec, I'm thinking..."""

# * Option 2 - Base Class for each Pokemon
class Pokemon:
    """Base Class for all Pokemon"""

    def __init__(self, species_or_dex: str | int):
        """Initialize the Pokemon class"""
        if isinstance(species_or_dex, str):
            self.__name = species_or_dex
        elif isinstance(species_or_dex, int):
            self.__dex_num = species_or_dex
        else:
            raise TypeError("Parameter must be of type str or int.")

        # intended to be used as "private variables"

        # ! REPLACE ALL OF THE FOLLOWING WITH CONSTANTS (EVENTUALLY)
        self.__dex_num = 63
        self.__name = ""
        self.__base_stats = {"hp": 25, "atk": 20, "def": 15, "spe": 90, "spc": 105}
        self.__types = ["Psychic", ""]
        self.__base_exp = 0
        self.__growth_rate = "Medium Slow"
        self.__tmhm_learnset = ["tm01", ..., "tm50"]
        # ! REPLACE ALL OF THE FOLLOWING WITH CONSTANTS (EVENTUALLY)

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

    def get_level(self):
        """Return the level of the Pokemon"""
        return self.level

    def get_current_stats(self):
        """Return the current stats of the Pokemon"""
        return self.current_stats

    def get_learned_moves(self):
        """Return the learned moves of the Pokemon"""
        return self.learned_moves

    def get_current_moves(self):
        """Return the current moves of the Pokemon"""
        return self.current_moves

    def get_nature(self):
        """Return the nature of the Pokemon"""
        return self.nature

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
