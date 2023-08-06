"""Similar to the poke_lookup_table.py file, this file is used to store the moves of each Pokemon."""
# Based on the learnsets from https://pokemondb.net/pokedex/game/red-blue-yellow
# (Using Gen 1 movesets ONLY here!)
# Also, these learnsets do NOT differentiate between moves learnable by level up, TM, or HM
# They simply list all moves that CAN be learned by the Pokemon

from re import A
from pypokelib.generation1.constants.move_consts import *

# * Learnsets are "read-ony", so tuples are helpful here
# Note, learnsets contain (shallow!) copies of the moves
BULBASAUR_LEARNSET = (
    GROWL,
    TACKLE,
    VINE_WHIP,
    LEECH_SEED,
    GROWTH,
    RAZOR_LEAF,
    POISON_POWDER,
    SLEEP_POWDER,
    SOLAR_BEAM,             # moves learnt by level up ^
    SWORDS_DANCE,
    TOXIC,
    BODY_SLAM,
    TAKE_DOWN,
    DOUBLE_EDGE,
    RAGE,
    MEGA_DRAIN,
    SOLAR_BEAM,
    MIMIC,
    DOUBLE_TEAM,
    REFLECT,
    BIDE,
    REST,
    SUBSTITUTE,             # moves learnt by TM ^
    CUT                     # HM move
)
IVYSAUR_LEARNSET = BULBASAUR_LEARNSET
VENUSAUR_LEARNSET = BULBASAUR_LEARNSET + (HYPER_BEAM)

CHARMANDER_LEARNSET = (
    GROWL,
    SCRATCH,
    EMBER,
    LEER,
    RAGE,
    SLASH,
    FLAMETHROWER,
    FIRE_SPIN,              # moves learnt by level up <--^
    MEGA_PUNCH,
    SWORDS_DANCE,
    MEGA_KICK,
    TOXIC,
    BODY_SLAM,
    TAKE_DOWN,
    DOUBLE_EDGE,
    SUBMISSION,
    COUNTER,
    SEISMIC_TOSS,
    RAGE,
    DRAGON_RAGE,
    DIG,
    MIMIC,
    DOUBLE_TEAM,
    REFLECT,
    BIDE,
    FIRE_BLAST,
    SWIFT,
    SKULL_BASH,
    REST,
    SUBSTITUTE,             # moves learnt by TM <--^
    CUT,                    # HM move
    STRENGTH                # HM move
)
CHARMELEON_LEARNSET = CHARMANDER_LEARNSET
CHARIZARD_LEARNSET = CHARMANDER_LEARNSET + (HYPER_BEAM, EARTHQUAKE, FISSURE)

SQUIRTLE_LEARNSET = (
    TACKLE,
    TAIL_WHIP,
    BUBBLE,
    WATER_GUN,
    BITE,
    WITHDRAW,
    SKULL_BASH,
    HYDRO_PUMP,             # moves learnt by level up <--^
    MEGA_PUNCH,
    MEGA_KICK,
    TOXIC,
    BODY_SLAM,
    TAKE_DOWN,
    DOUBLE_EDGE,
    BUBBLE_BEAM,
    WATER_GUN,
    ICE_BEAM,
    BLIZZARD,
    SUBMISSION,
    COUNTER,
    SEISMIC_TOSS,
    RAGE,
    DIG,
    MIMIC,
    DOUBLE_TEAM,
    REFLECT,
    BIDE,
    SKULL_BASH,
    REST,
    SUBSTITUTE,             # moves learnt by TM <--^
    SURF,                   # HM move
    STRENGTH                # HM move
)
WARTORTLE_LEARNSET = SQUIRTLE_LEARNSET
BLASTOISE_LEARNSET = SQUIRTLE_LEARNSET + (HYPER_BEAM, EARTHQUAKE, FISSURE)

CATTERPIE_LEARNSET = (
    TACKLE,
    STRING_SHOT
)
METAPOD_LEARNSET = (HARDEN)
BUTTTERFREE_LEARNSET = (
    CONFUSION,
    POISON_POWDER,
    PSYBEAM,
    SLEEP_POWDER,
    STUN_SPORE,
    SUPERSONIC,
    WHIRLWIND,              # moves learnt by level up <--^
    BIDE,
    DOUBLE_TEAM,
    DOUBLE_EDGE,
    HYPER_BEAM,
    MEGA_DRAIN,
    MIMIC,
    PSYCHIC,
    PSYWAVE,
    RAGE,
    RAZOR_WIND,
    REFLECT,
    REST,
    SOLAR_BEAM,
    SUBSTITUTE,
    SWIFT,
    TAKE_DOWN,
    TELEPORT,
    TOXIC,
    WHIRLWIND              # moves learnt by TM <--^
)

WEEDLE_LEARNSET = (
    POISON_STING,
    STRING_SHOT
)
KAKUNA_LEARNSET = (HARDEN)
BEEDRILL_LEARNSET = (
    AGILITY,
    FOCUS_ENERGY,
    FURY_ATTACK,
    PIN_MISSILE,
    RAGE,
    TWINEEDLE,            # moves learnt by level up <--^
    BIDE,
    DOUBLE_EDGE,
    DOUBLE_TEAM,
    HYPER_BEAM,
    MEGA_DRAIN,
    MIMIC,
    RAGE,
    REFLECT,
    REST,
    SKULL_BASH,
    SUBSTITUTE,
    SWIFT,
    SWORDS_DANCE,
    TAKE_DOWN,
    TOXIC,              # moves learnt by TM <--^
    CUT                 # HM move
)

PIDGEY_LEARNSET = (
    GUST,
    SAND_ATTACK,
    QUICK_ATTACK,
    WHIRLWIND,
    WING_ATTACK,
    AGILITY,
    MIRROR_MOVE,            # moves learnt by level up <--^
    BIDE,
    DOUBLE_EDGE,
    DOUBLE_TEAM,
    MIMIC,
    RAGE,
    RAZOR_WIND,
    REFLECT,
    REST,
    SKY_ATTACK,
    SUBSTITUTE,
    SWIFT,
    TAKE_DOWN,
    TOXIC,                  # moves learnt by TM <--^
    FLY                     # HM move
)
PIDGEOTTO_LEARNSET = PIDGEY_LEARNSET
PIDGEOT_LEARNSET = PIDGEY_LEARNSET + (HYPER_BEAM)

RATTATA_LEARNSET = (
    TACKLE,
    TAIL_WHIP,
    QUICK_ATTACK,
    HYPER_FANG,
    FOCUS_ENERGY,
    SUPER_FANG,             # moves learnt by level up <--^
    BIDE,
    BLIZZARD,
    BODY_SLAM,
    BUBBLE_BEAM,
    DIG,
    DOUBLE_EDGE,
    DOUBLE_TEAM,
    MIMIC,
    RAGE,
    REST,
    SUBSTITUTE,
    SKULL_BASH,
    SWIFT,
    TAKE_DOWN,
    THUNDER,
    THUNDERBOLT,
    TOXIC,                  # moves learnt by TM <--^
    WATER_GUN
)
RATICATE_LEARNSET = RATTATA_LEARNSET + (HYPER_BEAM, ICE_BEAM)

SPEAROW_LEARNSET = (
    GROWL,
    PECK,
    LEER,
    FURY_ATTACK,
    MIRROR_MOVE,
    AGILITY,
    DRILL_PECK,             # moves learnt by level up <--^
    BIDE,
    DOUBLE_EDGE,
    DOUBLE_TEAM,
    MIMIC,
    RAGE,
    RAZOR_WIND,
    REST,
    SKY_ATTACK,
    SUBSTITUTE,
    SWIFT,
    TAKE_DOWN,
    WHIRLWIND,             
    TOXIC,                  # moves learnt by TM <--^
    FLY                     # HM move
)
FEAROW_LEARNSET = SPEAROW_LEARNSET + (HYPER_BEAM)

EKANS_LEARNSET = (
    LEER,
    WRAP,
    POISON_STING,
    BITE,
    GLARE,
    SCREECH,
    ACID,                   # moves learnt by level up <--^
    BIDE,
    BODY_SLAM,
    DOUBLE_EDGE,
    DOUBLE_TEAM,
    DIG,
    EARTHQUAKE,
    MEGA_DRAIN,
    FISSURE,
    MIMIC,
    RAGE,
    REST,
    ROCK_SLIDE,
    SUBSTITUTE,
    SKULL_BASH,
    TAKE_DOWN,
    TOXIC,                  # moves learnt by TM <--^
    STRENGTH                # HM move
)
ARBOK_LEARNSET = EKANS_LEARNSET + (HYPER_BEAM)

