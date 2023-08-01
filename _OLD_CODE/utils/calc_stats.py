"""Main series functions for calculating PokeMon stats"""
# pylint: disable=line-too-long

from math import floor
import new_poke_instance as npi


# ? I think the following functions should be methods of PokeMon class, and possibly be combined
def set_hp_stat(curr_hp: int, level:int, hp_iv: int) -> int:
    """_summary_

    :param curr_hp: _description_
    :type curr_hp: int
    :param level: _description_
    :type level: int
    :param hp_iv: _description_
    :type hp_iv: int
    :return: _description_
    :rtype: int
    """
    return floor(0.01 * (2 * curr_hp + hp_iv) * level) + level + 10


def set_base_stat(curr_stat: int, level: int, stat_iv: int) -> int:
    """Updates (or initializes) all other stats (Attack, Defense, Special Attack, Special Defense, Speed)."""
    return floor(0.01 * (2 * curr_stat + stat_iv) * level) + 5


# ? Is there a better way to do this?
def set_nature_stats(pokemon: npi.PokeMon, nature: str):
    """Updates (or initializes) stats based on PokeMon's nature.\n
    Nature stat changes are as follows:
    - Attack +10% -> (Adamant, Brave, Lonely, Naughty)
    - Defense +10% -> (Bold, Impish, Lax, Relaxed)
    - Special Attack +10% -> (Modest, Mild, Quiet, Rash)
    - Special Defense +10% -> (Calm, Careful, Gentle, Sassy)
    - Speed +10% -> (Hasty, Jolly, Naive, Timid)\n
    =================================================================
    - Attack -10% -> (Brave, Impish, Mild, Careful, Jolly)
    - Defense -10% -> (Lonely, Lax, Quiet, Gentle, Naive)
    - Special Attack -10% -> (Adamant, Bold, Modest, Calm, Hasty)
    - Special Defense -10% -> (Brave, Impish, Mild, Careful, Jolly)
    - Speed -10% -> (Brave, Impish, Mild, Careful, Jolly)\n
    =================================================================
    - Neutral: +0%, -0% -> (Bashful, Docile, Hardy, Quirky, Serious)"""
    # ! Find a way to correctly update stats based on nature
    # May be more efficient to update stats on the fly rather than keep track of all stats perpetually
    if nature.lower() in ["adamant", "brave", "lonely", "naughty"]:
        pokemon.attack = floor(pokemon.attack * 1.1)
    elif nature.lower() in ["bold", "impish", "lax", "relaxed"]:
        pokemon.defense = floor(pokemon.defense * 1.1)
    elif nature.lower() in ["modest", "mild", "quiet", "rash"]:
        pokemon.special_attack = floor(pokemon.special_attack * 1.1)
    elif nature.lower() in ["calm", "careful", "gentle", "sassy"]:
        pokemon.special_defense = floor(pokemon.special_defense * 1.1)
    elif nature.lower() in ["hasty", "jolly", "naive", "timid"]:
        pokemon.speed = floor(pokemon.speed * 1.1)
    
    if nature.lower() in ["adamant", "bold", "modest", "calm", "hasty"]:
        pokemon.attack = floor(pokemon.attack * 0.9)
    elif nature.lower() in ["brave", "impish", "mild", "careful", "jolly"]:
        pokemon.speed = floor(pokemon.speed * 0.9)
    elif nature.lower() in ["lonely", "lax", "quiet", "gentle", "naive"]:
        pokemon.defense = floor(pokemon.defense * 0.9)
    elif nature.lower() in ["naughty", "relaxed", "rash", "sassy", "timid"]:
        pokemon.special_defense = floor(pokemon.special_defense * 0.9)

