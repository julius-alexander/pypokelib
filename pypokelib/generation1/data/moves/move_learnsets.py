"""Similar to the poke_lookup_table.py file, this file is used to store the moves of each Pokemon."""
# Based on the learnsets from https://pokemondb.net/pokedex/game/red-blue-yellow
# (Using Gen 1 movesets ONLY here!)
# Also, these learnsets do NOT differentiate between moves learnable by level up, TM, or HM
# They simply list all moves that CAN be learned by the Pokemon

# from pypokelib.generation1.constants.move_consts import *
from pypokelib.generation1.constants.thhm_consts import *

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
    TM03,
    TM06,
    TM08,
    TM09,
    TM10,
    TM20,
    TM21,
    TM22,
    TM31,
    TM32,
    TM33,
    TM34,
    TM44,
    TM50,
    HM01,
)
IVYSAUR_LEARNSET = BULBASAUR_LEARNSET
VENUSAUR_LEARNSET = BULBASAUR_LEARNSET + (TM15)

CHARMANDER_LEARNSET = (
    GROWL,
    SCRATCH,
    EMBER,
    LEER,
    TM20,
    SLASH,
    FLAMETHROWER,
    FIRE_SPIN,
    TM01,
    TM03,
    TM05,
    TM06,
    TM08,
    TM09,
    TM10,
    TM17,
    TM18,
    TM19,
    TM20,
    TM23,
    TM28,
    TM31,
    TM32,
    TM33,
    TM34,
    TM38,
    TM39,
    TM40,
    TM44,
    TM50,
    HM01,
    HM04,
)
CHARMELEON_LEARNSET = CHARMANDER_LEARNSET
CHARIZARD_LEARNSET = CHARMANDER_LEARNSET + (TM15, TM26, TM27)

SQUIRTLE_LEARNSET = (
    TACKLE,
    TAIL_WHIP,
    BUBBLE,
    BITE,
    WITHDRAW,
    HYDRO_PUMP,
    TM01,
    TM05,
    TM06,
    TM08,
    TM09,
    TM10,
    TM11,
    TM12,
    TM13,
    TM14,
    TM17,
    TM18,
    TM19,
    TM20,
    TM28,
    TM31,
    TM32,
    TM33,
    TM34,
    TM40,
    TM44,
    TM50,
    HM03,
    HM04,
)
WARTORTLE_LEARNSET = SQUIRTLE_LEARNSET
BLASTOISE_LEARNSET = SQUIRTLE_LEARNSET + (TM15, TM26, TM27)

CATERPIE_LEARNSET = (TACKLE, STRING_SHOT, NO_MOVE, NO_MOVE)
METAPOD_LEARNSET = HARDEN
BUTTTERFREE_LEARNSET = (
    CONFUSION,
    POISON_POWDER,
    PSYBEAM,
    SLEEP_POWDER,
    STUN_SPORE,
    SUPERSONIC,
    TM04,
    TM34,
    TM32,
    TM10,
    TM15,
    TM21,
    TM31,
    TM29,
    TM46,
    TM20,
    TM02,
    TM33,
    TM44,
    TM22,
    TM50,
    TM39,
    TM09,
    TM30,
    TM06,
    TM04,
)

WEEDLE_LEARNSET = (POISON_STING, STRING_SHOT)
KAKUNA_LEARNSET = HARDEN
BEEDRILL_LEARNSET = (
    AGILITY,
    FOCUS_ENERGY,
    FURY_ATTACK,
    PIN_MISSILE,
    TM20,
    TWINEEDLE,
    TM34,
    TM10,
    TM32,
    TM15,
    TM21,
    TM31,
    TM20,
    TM33,
    TM44,
    TM40,
    TM50,
    TM39,
    TM03,
    TM09,
    TM06,
    HM01,
)

PIDGEY_LEARNSET = (
    GUST,
    SAND_ATTACK,
    QUICK_ATTACK,
    TM04,
    WING_ATTACK,
    AGILITY,
    MIRROR_MOVE,
    TM34,
    TM10,
    TM32,
    TM31,
    TM20,
    TM02,
    TM33,
    TM44,
    TM43,
    TM50,
    TM39,
    TM09,
    TM06,
    HM02,
)
PIDGEOTTO_LEARNSET = PIDGEY_LEARNSET
PIDGEOT_LEARNSET = PIDGEY_LEARNSET + (TM15)

RATTATA_LEARNSET = (
    TACKLE,
    TAIL_WHIP,
    QUICK_ATTACK,
    HYPER_FANG,
    FOCUS_ENERGY,
    SUPER_FANG,
    TM34,
    TM14,
    TM08,
    TM11,
    TM28,
    TM10,
    TM32,
    TM31,
    TM20,
    TM44,
    TM50,
    TM40,
    TM39,
    TM09,
    TM25,
    TM24,
    TM06,
    TM12,
)
RATICATE_LEARNSET = RATTATA_LEARNSET + (TM15, TM13)

SPEAROW_LEARNSET = (
    GROWL,
    PECK,
    LEER,
    FURY_ATTACK,
    MIRROR_MOVE,
    AGILITY,
    DRILL_PECK,
    TM34,
    TM10,
    TM32,
    TM31,
    TM20,
    TM02,
    TM44,
    TM43,
    TM50,
    TM39,
    TM09,
    TM04,
    TM06,
    HM02,
)
FEAROW_LEARNSET = SPEAROW_LEARNSET + (TM15)

EKANS_LEARNSET = (
    LEER,
    WRAP,
    POISON_STING,
    BITE,
    GLARE,
    SCREECH,
    ACID,
    TM34,
    TM08,
    TM10,
    TM32,
    TM28,
    TM26,
    TM21,
    TM27,
    TM31,
    TM20,
    TM44,
    TM48,
    TM50,
    TM40,
    TM09,
    TM06,
    HM04,
)
ARBOK_LEARNSET = EKANS_LEARNSET + (TM15)

PIKACHU_LEARNSET = (
    GROWL,
    THUNDER_SHOCK,
    TM45,
    QUICK_ATTACK,
    TM39,
    AGILITY,
    TM25,
    TM34,
    TM08,
    TM32,
    TM10,
    TM05,
    TM01,
    TM31,
    TM16,
    TM20,
    TM33,
    TM44,
    TM19,
    TM40,
    TM50,
    TM17,
    TM09,
    TM24,
    TM06,
    HM05,
)
RAICHU_LEARNSET = PIKACHU_LEARNSET + (TM15)

SANDSHREW_LEARNSET = (
    SCRATCH,
    SAND_ATTACK,
    SLASH,
    POISON_STING,
    TM39,
    FURY_SWIPES,
    TM34,
    TM08,
    TM28,
    TM10,
    TM32,
    TM26,
    TM27,
    TM31,
    TM20,
    TM44,
    TM48,
    TM19,
    TM40,
    TM17,
    TM50,
    TM03,
    TM09,
    TM06,
    HM01,
    HM04,
)
SANDSLASH_LEARNSET = SANDSHREW_LEARNSET + (TM15)

NIDORAN_F_LEARNSET = (
    BITE,
    DOUBLE_KICK,
    FURY_SWIPES,
    GROWL,
    POISON_STING,
    SCRATCH,
    TAIL_WHIP,
    TACKLE,
    TM34,
    TM14,
    TM08,
    TM32,
    TM10,
    TM31,
    TM20,
    TM33,
    TM44,
    TM40,
    TM50,
    TM09,
    TM25,
    TM24,
    TM06,
)
NIDORINA_LEARNSET = NIDORAN_F_LEARNSET + (TM11, TM07, TM13)
NIDOQUEEN_LEARNSET = NIDORINA_LEARNSET + (
    TM18,
    TM26,
    TM38,
    TM27,
    TM15,
    TM05,
    TM01,
    TM16,
    TM48,
    TM19,
    TM17,
    TM12,
)

NIDORAN_M_LEARNSET = (
    DOUBLE_KICK,
    FOCUS_ENERGY,
    FURY_ATTACK,
    HORN_ATTACK,
    TM07,
    LEER,
    POISON_STING,
    TACKLE,
    TM34,
    TM14,
    TM08,
    TM32,
    TM10,
    TM31,
    TM20,
    TM33,
    TM44,
    TM40,
    TM50,
    TM09,
    TM25,
    TM24,
    TM06,
)
NIDORINO_LEARNSET = (TM11, TM13, TM12)
NIDOKING_LEARNSET = (
    THRASH,
    TM18,
    TM26,
    TM38,
    TM27,
    TM15,
    TM05,
    TM01,
    TM16,
    TM48,
    TM19,
    TM17,
)

CLEFAIRY_LEARNSET = (
    GROWL,
    POUND,
    SING,
    DOUBLE_SLAP,
    MINIMIZE,
    DEFENSE_CURL,
    LIGHT_SCREEN,
    TM01,
    TM05,
    TM06,
    TM08,
    TM09,
    TM10,
    TM11,
    TM12,
    TM13,
    TM14,
    TM17,
    TM18,
    TM19,
    TM20,
    TM22,
    TM24,
    TM25,
    TM29,
    TM30,
    TM31,
    TM32,
    TM33,
    TM34,
    TM35,
    TM38,
    TM40,
    TM44,
    TM45,
    TM46,
    TM49,
    TM50,
    HM04,
    HM05,
)
CLEFABLE_LEARNSET = CLEFAIRY_LEARNSET + (TM15)

VULPIX_LEARNSET = (
    EMBER,
    QUICK_ATTACK,
    ROAR,
    CONFUSE_RAY,
    TAIL_WHIP,
    FLAMETHROWER,
    FIRE_SPIN,
    TM06,
    TM08,
    TM09,
    TM10,
    TM20,
    TM28,
    TM31,
    TM32,
    TM33,
    TM34,
    TM38,
    TM39,
    TM40,
    TM44,
    TM50,
)
NINETALES_LEARNSET = VULPIX_LEARNSET + (TM15)

JIGGLYPUFF_LEARNSET = (
    SING,
    POUND,
    DISABLE,
    DEFENSE_CURL,
    DOUBLE_SLAP,
    BODY_SLAM,
    DOUBLE_EDGE,
    TM01,
    TM05,
    TM06,
    TM08,
    TM09,
    TM10,
    TM11,
    TM12,
    TM13,
    TM14,
    TM17,
    TM18,
    TM19,
    TM20,
    TM22,
    TM24,
    TM25,
    TM29,
    TM30,
    TM31,
    TM32,
    TM33,
    TM34,
    TM38,
    TM40,
    TM44,
    TM45,
    TM46,
    TM49,
    TM50,
    HM04,
    HM05,
)
WIGGLYTUFF_LEARNSET = JIGGLYPUFF_LEARNSET + (TM15)

ZUBAT_LEARNSET = (
    LEECH_LIFE,
    SUPERSONIC,
    BITE,
    WING_ATTACK,
    CONFUSE_RAY,
    HAZE,
    TM02,
    TM04,
    TM06,
    TM09,
    TM10,
    TM20,
    TM21,
    TM31,
    TM32,
    TM34,
    TM39,
    TM44,
    TM50,
)
GOLBAT_LEARNSET = ZUBAT_LEARNSET + (SCREECH, TM15)

ODDISH_LEARNSET = (
    ABSORB,
    ACID,
    SLEEP_POWDER,
    STUN_SPORE,
    POISON_POWDER,
    PETAL_DANCE,
    TM03,
    TM06,
    TM09,
    TM10,
    TM20,
    TM21,
    TM22,
    TM31,
    TM32,
    TM33,
    TM34,
    TM44,
    TM50,
)
GLOOM_LEARNSET = ODDISH_LEARNSET
VILEPLUME_LEARNSET = ODDISH_LEARNSET + (TM08, TM15)

PARAS_LEARNSET = (
    SCRATCH,
    STUN_SPORE,
    LEECH_LIFE,
    SPORE,
    SLASH,
    GROWTH,
    TM03,
    TM06,
    TM08,
    TM09,
    TM10,
    TM20,
    TM21,
    TM22,
    TM28,
    TM31,
    TM32,
    TM33,
    TM34,
    TM40,
    TM44,
    TM50,
    HM01,
)
PARASECT_LEARNSET = PARAS_LEARNSET + (TM15)

VENONAT_LEARNSET = (
    DISABLE,
    TACKLE,
    POISON_POWDER,
    LEECH_LIFE,
    STUN_SPORE,
    PSYBEAM,
    SLEEP_POWDER,
    PSYCHIC,
    TM06,
    TM09,
    TM10,
    TM20,
    TM21,
    TM22,
    TM29,
    TM31,
    TM32,
    TM33,
    TM34,
    TM44,
    TM46,
    TM50,
)
VENOMOTH_LEARNSET = VENONAT_LEARNSET + (
    TM02,
    TM04,
    TM15,
)

DIGLETT_LEARNSET = (
    SCRATCH,
    GROWL,
    DIG,
    SAND_ATTACK,
    SLASH,
    EARTHQUAKE,
    TM06,
    TM08,
    TM09,
    TM10,
    TM20,
    TM26,
    TM27,
    TM28,
    TM31,
    TM32,
    TM34,
    TM44,
    TM48,
    TM50,
)
DUGTRIO_LEARNSET = DIGLETT_LEARNSET + (TM15)

MEOWTH_LEARNSET = (
    SCRATCH,
    GROWL,
    BITE,
    SCREECH,
    FURY_SWIPES,
    SLASH,
    TM06,
    TM08,
    TM09,
    TM10,
    TM11,
    TM12,
    TM16,
    TM20,
    TM24,
    TM25,
    TM31,
    TM32,
    TM34,
    TM39,
    TM40,
    TM44,
    TM50,
)
PERSIAN_LEARNSET = MEOWTH_LEARNSET + (TM15)

PSYDUCK_LEARNSET = (
    SCRATCH,
    TAIL_WHIP,
    DISABLE,
    CONFUSION,
    FURY_SWIPES,
    HYDRO_PUMP,
    TM01,
    TM05,
    TM06,
    TM08,
    TM09,
    TM10,
    TM11,
    TM12,
    TM13,
    TM14,
    TM16,
    TM17,
    TM18,
    TM19,
    TM20,
    TM28,
    TM30,
    TM31,
    TM32,
    TM34,
    TM39,
    TM40,
    TM44,
    TM50,
    HM03,
    HM04,
)
GOLDUCK_LEARNSET = PSYDUCK_LEARNSET + (TM15)

MANKEY_LEARNSET = (
    SCRATCH,
    KARATE_CHOP,
    FURY_SWIPES,
    FOCUS_ENERGY,
    THRASH,
    LEER,
    TM01,
    TM05,
    TM06,
    TM08,
    TM09,
    TM10,
    TM16,
    TM17,
    TM18,
    TM19,
    TM20,
    TM24,
    TM25,
    TM28,
    TM31,
    TM32,
    TM34,
    TM35,
    TM39,
    TM40,
    TM44,
    TM48,
    TM50,
    HM04
)
PRIMEAPE_LEARNSET = MANKEY_LEARNSET + (TM15)

GROWLITHE_LEARNSET = (
    BITE,
    ROAR,
    EMBER,
    LEER,
    AGILITY,
    FLAMETHROWER,
    TM06,
    TM08,
    TM09,
    TM10,
    TM20,
    TM23,
    TM28,
    TM31,
    TM32,
    TM33,
    TM34,
    TM38,
    TM39,
    TM40,
    TM44,
    TM50
)
ARCANINE_LEARNSET = GROWLITHE_LEARNSET + (
    TM15,
    TM30
)

POLIWAG_LEARNSET = (
    BUBBLE,
    HYPNOSIS,
    DOUBLE_SLAP,
    BODY_SLAM,
    AMNESIA,
    HYDRO_PUMP,
    TM03,
    TM06,
    TM08,
    TM09,
    TM10,
    TM11,
    TM12,
    TM13,
    TM14,
    TM20,
    TM29,
    TM31,
    TM32,
    TM34,
    TM40,
    TM44,
    TM46,
    TM50,
    HM03
)
POLIWHIRL_LEARNSET = POLIWAG_LEARNSET + (
    TM01,
    TM05,
    TM17,
    TM18,
    TM19,
    TM26,
    TM27,
    TM35,
    HM04
)
POLIWRATH_LEARNSET = POLIWHIRL_LEARNSET + (
    TM01,
    TM05,
    TM06,
    TM08,
    TM09,
    TM10,
    TM11,
    TM12,
    TM13,
    TM14,
    TM15,
    TM17,
    TM18,
    TM19,
    TM20,
    TM26,
    TM27,
    TM29,
    TM31,
    TM32,
    TM34,
    TM35,
    TM40,
    TM44,
    TM46,
    TM50,
    HM03,
    HM04
)

ABRA_LEARNSET = (
    TM01,
    TM05,
    TM06,
    TM08,
    TM09,
    TM10,
    TM17,
    TM18,
    TM19,
    TM20,
    TM29,
    TM30,
    TM31,
    TM32,
    TM33,
    TM34,
    TM35,
    TM40,
    TM44,
    TM45,
    TM46,
    TM49,
    TM50,
    HM05
)
KADABRA_LEARNSET = (
    CONFUSION,
    DISABLE,
    PSYBEAM,
    RECOVER,
    TM01,
    TM05,
    TM06,
    TM08,
    TM09,
    TM10,
    TM17,
    TM18,
    TM19,
    TM20,
    TM28,
    TM29,
    TM30,
    TM31,
    TM32,
    TM33,
    TM34,
    TM35,
    TM40,
    TM44,
    TM45,
    TM46,
    TM49,
    TM50,
    HM05
)
ALAKAZAM_LEARNSET = (
    CONFUSION,
    DISABLE,
    PSYBEAM,
    RECOVER,
    TM01,
    TM05,
    TM06,
    TM08,
    TM09,
    TM10,
    TM15,
    TM17,
    TM18,
    TM19,
    TM20,
    TM28,
    TM29,
    TM30,
    TM31,
    TM32,
    TM33,
    TM34,
    TM35,
    TM40,
    TM44,
    TM45,
    TM46,
    TM49,
    TM50,
    HM05
)

MACHOP_LEARNSET = (
    KARATE_CHOP,
    LOW_KICK,
    LEER,
    FOCUS_ENERGY,
    TM01,
    TM05,
    TM06,
    TM08,
    TM09,
    TM10,
    TM17,
    TM18,
    TM19,
    TM20,
    TM26,
    TM27,
    TM28,
    TM31,
    TM32,
    TM34,
    TM35,
    TM38,
    TM40,
    TM44,
    TM48,
    TM50,
    HM04
)
MACHOKE_LEARNSET = (
    KARATE_CHOP,
    LOW_KICK,
    LEER,
    FOCUS_ENERGY,
    TM01,
    TM05,
    TM06,
    TM08,
    TM09,
    TM10,
    TM17,
    TM18,
    TM19,
    TM20,
    TM26,
    TM27,
    TM28,
    TM31,
    TM32,
    TM34,
    TM35,
    TM38,
    TM40,
    TM44,
    TM48,
    TM50,
    HM04
)
MACHAMP_LEARNSET = (
    KARATE_CHOP,
    LOW_KICK,
    LEER,
    FOCUS_ENERGY,
    TM01,
    TM05,
    TM06,
    TM08,
    TM09,
    TM10,
    TM15,
    TM17,
    TM18,
    TM19,
    TM20,
    TM26,
    TM27,
    TM28,
    TM31,
    TM32,
    TM34,
    TM35,
    TM38,
    TM40,
    TM44,
    TM48,
    TM50,
    HM04
)

BELLSPROUT_LEARNSET = (
    ACID,
    GROWTH,
    POISON_POWDER,
    RAZOR_LEAF,
    SLAM,
    SLEEP_POWDER,
    STUN_SPORE,
    VINE_WHIP,
    WRAP,
    TM03,
    TM06,
    TM09,
    TM10,
    TM20,
    TM21,
    TM22,
    TM31,
    TM32,
    TM33,
    TM34,
    TM44,
    TM50,
    HM01
)
WEEPINBELL_LEARNSET = (
    ACID,
    GROWTH,
    POISON_POWDER,
    RAZOR_LEAF,
    SLAM,
    SLEEP_POWDER,
    STUN_SPORE,
    VINE_WHIP,
    WRAP,
    TM03,
    TM06,
    TM09,
    TM10,
    TM20,
    TM21,
    TM22,
    TM31,
    TM32,
    TM33,
    TM34,
    TM44,
    TM50,
    HM01
)
VICTREEBEL_LEARNSET = (
    ACID,
    GROWTH,
    POISON_POWDER,
    RAZOR_LEAF,
    SLAM,
    SLEEP_POWDER,
    STUN_SPORE,
    VINE_WHIP,
    WRAP,
    TM03,
    TM06,
    TM08,
    TM09,
    TM10,
    TM15,
    TM20,
    TM21,
    TM22,
    TM31,
    TM32,
    TM33,
    TM34,
    TM44,
    TM50,
    HM01
)

TENTACOOL_LEARNSET = (
    ACID,
    SUPERSONIC,
    WRAP,
    POISON_STING,
    WATER_GUN,
    CONSTRICT,
    BARRIER,
    SCREECH,
    HYDRO_PUMP,
    TM03,
    TM06,
    TM09,
    TM10,
    TM11,
    TM12,
    TM13,
    TM14,
    TM20,
    TM21,
    TM31,
    TM32,
    TM33,
    TM34,
    TM40,
    TM44,
    TM50,
    HM03
)
TENTACRUEL_LEARNSET = (
    ACID,
    SUPERSONIC,
    WRAP,
    POISON_STING,
    WATER_GUN,
    CONSTRICT,
    BARRIER,
    SCREECH,
    HYDRO_PUMP,
    TM03,
    TM06,
    TM09,
    TM10,
    TM11,
    TM12,
    TM13,
    TM14,
    TM15,
    TM20,
    TM21,
    TM31,
    TM32,
    TM33,
    TM34,
    TM40,
    TM44,
    TM50,
    HM03,
    HM01
)

GEODUDE_LEARNSET = (
    TACKLE,
    DEFENSE_CURL,
    ROCK_THROW,
    HARDEN,
    TM01,
    TM06,
    TM08,
    TM09,
    TM10,
    TM17,
    TM18,
    TM19,
    TM20,
    TM26,
    TM27,
    TM28,
    TM31,
    TM32,
    TM34,
    TM35,
    TM36,
    TM38,
    TM44,
    TM47,
    TM48,
    TM50,
    HM04
)
GRAVELER_LEARNSET = (
    TACKLE,
    DEFENSE_CURL,
    ROCK_THROW,
    HARDEN,
    TM01,
    TM06,
    TM08,
    TM09,
    TM10,
    TM17,
    TM18,
    TM19,
    TM20,
    TM26,
    TM27,
    TM28,
    TM31,
    TM32,
    TM34,
    TM35,
    TM36,
    TM38,
    TM44,
    TM47,
    TM48,
    TM50,
    HM04
)
GOLEM_LEARNSET = (
    TACKLE,
    DEFENSE_CURL,
    ROCK_THROW,
    HARDEN,
    TM01,
    TM05,
    TM06,
    TM08,
    TM09,
    TM10,
    TM15,
    TM17,
    TM18,
    TM19,
    TM20,
    TM26,
    TM27,
    TM28,
    TM31,
    TM32,
    TM34,
    TM35,
    TM36,
    TM38,
    TM44,
    TM47,
    TM48,
    TM50,
    HM04
)

PONYTA_LEARNSET = (
    EMBER,
    TAIL_WHIP,
    STOMP,
    GROWL,
    FIRE_SPIN,
    TAKE_DOWN,
    AGILITY,
    TM06,
    TM07,
    TM08,
    TM09,
    TM10,
    TM20,
    TM31,
    TM32,
    TM33,
    TM34,
    TM38,
    TM39,
    TM40,
    TM44,
    TM50
)
RAPIDASH_LEARNSET = (
    EMBER,
    TAIL_WHIP,
    STOMP,
    GROWL,
    FIRE_SPIN,
    TAKE_DOWN,
    AGILITY,
    TM06,
    TM07,
    TM08,
    TM09,
    TM10,
    TM15,
    TM20,
    TM31,
    TM32,
    TM33,
    TM34,
    TM38,
    TM39,
    TM40,
    TM44,
    TM50
)

SLOWPOKE_LEARNSET = (
    CONFUSION,
    DISABLE,
    HEADBUTT,
    GROWL,
    WATER_GUN,
    AMNESIA,
    PSYCHIC,
    TM06,
    TM08,
    TM09,
    TM10,
    TM11,
    TM12,
    TM13,
    TM14,
    TM16,
    TM20,
    TM26,
    TM27,
    TM28,
    TM29,
    TM30,
    TM31,
    TM32,
    TM33,
    TM34,
    TM38,
    TM39,
    TM40,
    TM44,
    TM45,
    TM46,
    TM49,
    TM50,
    HM03,
    HM04,
    HM05
)
SLOWBRO_LEARNSET = (
    CONFUSION,
    DISABLE,
    HEADBUTT,
    GROWL,
    WATER_GUN,
    AMNESIA,
    PSYCHIC,
    TM01,
    TM05,
    TM06,
    TM08,
    TM09,
    TM10,
    TM11,
    TM12,
    TM13,
    TM14,
    TM15,
    TM16,
    TM17,
    TM18,
    TM19,
    TM20,
    TM26,
    TM27,
    TM28,
    TM29,
    TM30,
    TM31,
    TM32,
    TM33,
    TM34,
    TM38,
    TM39,
    TM40,
    TM44,
    TM45,
    TM46,
    TM49,
    TM50,
    HM03,
    HM04,
    HM05
)

MAGNEMITE_LEARNSET = (
    TACKLE,
    SONIC_BOOM,
    THUNDER_SHOCK,
    SUPERSONIC,
    THUNDER_WAVE,
    SWIFT,
    SCREECH,
    TM06,
    TM09,
    TM10,
    TM20,
    TM24,
    TM25,
    TM30,
    TM31,
    TM32,
    TM33,
    TM34,
    TM39,
    TM44,
    TM45,
    TM50,
    HM05
)
MAGNETON_LEARNSET = (
    TACKLE,
    SONIC_BOOM,
    THUNDER_SHOCK,
    SUPERSONIC,
    THUNDER_WAVE,
    SWIFT,
    SCREECH,
    TM06,
    TM09,
    TM10,
    TM15,
    TM20,
    TM24,
    TM25,
    TM30,
    TM31,
    TM32,
    TM33,
    TM34,
    TM39,
    TM44,
    TM45,
    TM50,
    HM05
)

FARFETCHD_LEARNSET = ()

DODUO_LEARNSET = ()
DODRIO_LEARNSET = ()

SEEL_LEARNSET = ()
DEWGONG_LEARNSET = ()

GRIMER_LEARNSET = ()
MUK_LEARNSET = ()

SHELLDER_LEARNSET = ()
CLOYSTER_LEARNSET = ()

GASTLY_LEARNSET = ()
HAUNTER_LEARNSET = ()
GENGAR_LEARNSET = ()

ONIX_LEARNSET = ()

DROWZEE_LEARNSET = ()
HYPNO_LEARNSET = ()

KRABBY_LEARNSET = ()
KINGLER_LEARNSET = ()

VOLTORB_LEARNSET = ()
ELECTRODE_LEARNSET = ()

EXEGGCUTE_LEARNSET = ()
EXEGGUTOR_LEARNSET = ()

CUBONE_LEARNSET = ()
MAROWAK_LEARNSET = ()

HITMONLEE_LEARNSET = ()
HITMONCHAN_LEARNSET = ()

LICKITUNG_LEARNSET = ()

KOFFING_LEARNSET = ()
WEEZING_LEARNSET = ()

RHYHORN_LEARNSET = ()
RHYDON_LEARNSET = ()

CHANSEY_LEARNSET = ()

TANGELA_LEARNSET = ()

KANGASKHAN_LEARNSET = ()

HORSEA_LEARNSET = ()
SEADRA_LEARNSET = ()

GOLDEEN_LEARNSET = ()
SEAKING_LEARNSET = ()

STARYU_LEARNSET = ()
STARMIE_LEARNSET = ()

MR_MIME_LEARNSET = ()

SCYTHER_LEARNSET = ()

JYNX_LEARNSET = ()

ELECTABUZZ_LEARNSET = ()

MAGMAR_LEARNSET = ()

PINSIR_LEARNSET = ()

TAUROS_LEARNSET = ()

MAGIKARP_LEARNSET = ()
GYARADOS_LEARNSET = ()

LAPRAS_LEARNSET = ()

DITTO_LEARNSET = ()

EEVEE_LEARNSET = ()
VAPOREON_LEARNSET = ()
JOLTEON_LEARNSET = ()
FLAREON_LEARNSET = ()

PORYGON_LEARNSET = ()

OMANYTE_LEARNSET = ()
OMASTAR_LEARNSET = ()

KABUTO_LEARNSET = ()
KABUTOPS_LEARNSET = ()

AERODACTYL_LEARNSET = ()

SNORLAX_LEARNSET = ()

ARTICUNO_LEARNSET = ()

ZAPDOS_LEARNSET = ()

MOLTRES_LEARNSET = ()

DRATINI_LEARNSET = ()
DRAGONAIR_LEARNSET = ()
DRAGONITE_LEARNSET = ()

MEWTWO_LEARNSET = ()

MEW_LEARNSET = ()
