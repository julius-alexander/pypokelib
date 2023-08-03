"""Pokemon Generation 1 look-up table, for constant time access to Pokemon data."""
import sys
sys.path.append("./generation1/constants")
import dex_consts as dc                         # pylint: disable=E0401, wrong-import-position


DEX_HELPER_STR_TO_NUM = {
    "Bulbasaur": 1,
    "Ivysaur": 2,
    "Venusaur": 3,
    "Charmander": 4,
    "Charmeleon": 5,
    "Charizard": 6,
    "Squirtle": 7,
    "Wartortle": 8,
    "Blastoise": 9,
    "Caterpie": 10,
    "Metapod": 11,
    "Butterfree": 12,
    "Weedle": 13,
    "Kakuna": 14,
    "Beedrill": 15,
    "Pidgey": 16,
    "Pidgeotto": 17,
    "Pidgeot": 18,
    "Rattata": 19,
    "Raticate": 20,
    "Spearow": 21,
    "Fearow": 22,
    "Ekans": 23,
    "Arbok": 24,
    "Pikachu": 25,
    "Raichu": 26,
    "Sandshrew": 27,
    "Sandslash": 28,
    "Nidoran♀": 29,
    "Nidorina": 30,
    "Nidoqueen": 31,
    "Nidoran♂": 32,
    "Nidorino": 33,
    "Nidoking": 34,
    "Clefairy": 35,
    "Clefable": 36,
    "Vulpix": 37,
    "Ninetales": 38,
    "Jigglypuff": 39,
    "Wigglytuff": 40,
    "Zubat": 41,
    "Golbat": 42,
    "Oddish": 43,
    "Gloom": 44,
    "Vileplume": 45,
    "Paras": 46,
    "Parasect": 47,
    "Venonat": 48,
    "Venomoth": 49,
    "Diglett": 50,
    "Dugtrio": 51,
    "Meowth": 52,
    "Persian": 53,
    "Psyduck": 54,
    "Golduck": 55,
    "Mankey": 56,
    "Primeape": 57,
    "Growlithe": 58,
    "Arcanine": 59,
    "Poliwag": 60,
    "Poliwhirl": 61,
    "Poliwrath": 62,
    "Abra": 63,
    "Kadabra": 64,
    "Alakazam": 65,
    "Machop": 66,
    "Machoke": 67,
    "Machamp": 68,
    "Bellsprout": 69,
    "Weepinbell": 70,
    "Victreebel": 71,
    "Tentacool": 72,
    "Tentacruel": 73,
    "Geodude": 74,
    "Graveler": 75,
    "Golem": 76,
    "Ponyta": 77,
    "Rapidash": 78,
    "Slowpoke": 79,
    "Slowbro": 80,
    "Magnemite": 81,
    "Magneton": 82,
    "Farfetch'd": 83,
    "Doduo": 84,
    "Dodrio": 85,
    "Seel": 86,
    "Dewgong": 87,
    "Grimer": 88,
    "Muk": 89,
    "Shellder": 90,
    "Cloyster": 91,
    "Gastly": 92,
    "Haunter": 93,
    "Gengar": 94,
    "Onix": 95,
    "Drowzee": 96,
    "Hypno": 97,
    "Krabby": 98,
    "Kingler": 99,
    "Voltorb": 100,
    "Electrode": 101,
    "Exeggcute": 102,
    "Exeggutor": 103,
    "Cubone": 104,
    "Marowak": 105,
    "Hitmonlee": 106,
    "Hitmonchan": 107,
    "Lickitung": 108,
    "Koffing": 109,
    "Weezing": 110,
    "Rhyhorn": 111,
    "Rhydon": 112,
    "Chansey": 113,
    "Tangela": 114,
    "Kangaskhan": 115,
    "Horsea": 116,
    "Seadra": 117,
    "Goldeen": 118,
    "Seaking": 119,
    "Staryu": 120,
    "Starmie": 121,
    "Mr. Mime": 122,
    "Scyther": 123,
    "Jynx": 124,
    "Electabuzz": 125,
    "Magmar": 126,
    "Pinsir": 127,
    "Tauros": 128,
    "Magikarp": 129,
    "Gyarados": 130,
    "Lapras": 131,
    "Ditto": 132,
    "Eevee": 133,
    "Vaporeon": 134,
    "Jolteon": 135,
    "Flareon": 136,
    "Porygon": 137,
    "Omanyte": 138,
    "Omastar": 139,
    "Kabuto": 140,
    "Kabutops": 141,
    "Aerodactyl": 142,
    "Snorlax": 143,
    "Articuno": 144,
    "Zapdos": 145,
    "Moltres": 146,
    "Dratini": 147,
    "Dragonair": 148,
    "Dragonite": 149,
    "Mewtwo": 150,
    "Mew": 151,
}

# TODO - Remember to update learnset in dex_consts.py                       # pylint: disable=fixme
POKEDEX = {
    1: dc.BULBASAUR_DEX_ENTRY,
    2: dc.IVYSAUR_DEX_ENTRY,
    3: dc.VENUSAUR_DEX_ENTRY,
    4: dc.CHARMANDER_DEX_ENTRY,
    5: dc.CHARMELEON_DEX_ENTRY,
    6: dc.CHARIZARD_DEX_ENTRY,
    7: dc.SQUIRTLE_DEX_ENTRY,
    8: dc.WARTORTLE_DEX_ENTRY,
    9: dc.BLASTOISE_DEX_ENTRY,
    10: dc.CATERPIE_DEX_ENTRY,
    11: dc.METAPOD_DEX_ENTRY,
    12: dc.BUTTERFREE_DEX_ENTRY,
    13: dc.WEEDLE_DEX_ENTRY,
    14: dc.KAKUNA_DEX_ENTRY,
    15: dc.BEEDRILL_DEX_ENTRY,
    16: dc.PIDGEY_DEX_ENTRY,
    17: dc.PIDGEOTTO_DEX_ENTRY,
    18: dc.PIDGEOT_DEX_ENTRY,
    19: dc.RATTATA_DEX_ENTRY,
    20: dc.RATICATE_DEX_ENTRY,
    21: dc.SPEAROW_DEX_ENTRY,
    22: dc.FEAROW_DEX_ENTRY,
    23: dc.EKANS_DEX_ENTRY,
    24: dc.ARBOK_DEX_ENTRY,
    25: dc.PIKACHU_DEX_ENTRY,
    26: dc.RAICHU_DEX_ENTRY,
    27: dc.SANDSHREW_DEX_ENTRY,
    28: dc.SANDSLASH_DEX_ENTRY,
    29: dc.NIDORAN_F_DEX_ENTRY,
    30: dc.NIDORINA_DEX_ENTRY,
    31: dc.NIDOQUEEN_DEX_ENTRY,
    32: dc.NIDORAN_M_DEX_ENTRY,
    33: dc.NIDORINO_DEX_ENTRY,
    34: dc.NIDOKING_DEX_ENTRY,
    35: dc.CLEFAIRY_DEX_ENTRY,
    36: dc.CLEFABLE_DEX_ENTRY,
    37: dc.VULPIX_DEX_ENTRY,
    38: dc.NINETALES_DEX_ENTRY,
    39: dc.JIGGLYPUFF_DEX_ENTRY,
    40: dc.WIGGLYTUFF_DEX_ENTRY,
    41: dc.ZUBAT_DEX_ENTRY,
    42: dc.GOLBAT_DEX_ENTRY,
    43: dc.ODDISH_DEX_ENTRY,
    44: dc.GLOOM_DEX_ENTRY,
    45: dc.VILEPLUME_DEX_ENTRY,
    46: dc.PARAS_DEX_ENTRY,
    47: dc.PARASECT_DEX_ENTRY,
    48: dc.VENONAT_DEX_ENTRY,
    49: dc.VENOMOTH_DEX_ENTRY,
    50: dc.DIGLETT_DEX_ENTRY,
    51: dc.DUGTRIO_DEX_ENTRY,
    52: dc.MEOWTH_DEX_ENTRY,
    53: dc.PERSIAN_DEX_ENTRY,
    54: dc.PSYDUCK_DEX_ENTRY,
    55: dc.GOLDUCK_DEX_ENTRY,
    56: dc.MANKEY_DEX_ENTRY,
    57: dc.PRIMEAPE_DEX_ENTRY,
    58: dc.GROWLITHE_DEX_ENTRY,
    59: dc.ARCANINE_DEX_ENTRY,
    60: dc.POLIWAG_DEX_ENTRY,
    61: dc.POLIWHIRL_DEX_ENTRY,
    62: dc.POLIWRATH_DEX_ENTRY,
    63: dc.ABRA_DEX_ENTRY,
    64: dc.KADABRA_DEX_ENTRY,
    65: dc.ALAKAZAM_DEX_ENTRY,
    66: dc.MACHOP_DEX_ENTRY,
    67: dc.MACHOKE_DEX_ENTRY,
    68: dc.MACHAMP_DEX_ENTRY,
    69: dc.BELLSPROUT_DEX_ENTRY,
    70: dc.WEEPINBELL_DEX_ENTRY,
    71: dc.VICTREEBEL_DEX_ENTRY,
    72: dc.TENTACOOL_DEX_ENTRY,
    73: dc.TENTACRUEL_DEX_ENTRY,
    74: dc.GEODUDE_DEX_ENTRY,
    75: dc.GRAVELER_DEX_ENTRY,
    76: dc.GOLEM_DEX_ENTRY,
    77: dc.PONYTA_DEX_ENTRY,
    78: dc.RAPIDASH_DEX_ENTRY,
    79: dc.SLOWPOKE_DEX_ENTRY,
    80: dc.SLOWBRO_DEX_ENTRY,
    81: dc.MAGNEMITE_DEX_ENTRY,
    82: dc.MAGNETON_DEX_ENTRY,
    83: dc.FARFETCHD_DEX_ENTRY,
    84: dc.DODUO_DEX_ENTRY,
    85: dc.DODRIO_DEX_ENTRY,
    86: dc.SEEL_DEX_ENTRY,
    87: dc.DEWGONG_DEX_ENTRY,
    88: dc.GRIMER_DEX_ENTRY,
    89: dc.MUK_DEX_ENTRY,
    90: dc.SHELLDER_DEX_ENTRY,
    91: dc.CLOYSTER_DEX_ENTRY,
    92: dc.GASTLY_DEX_ENTRY,
    93: dc.HAUNTER_DEX_ENTRY,
    94: dc.GENGAR_DEX_ENTRY,
    95: dc.ONIX_DEX_ENTRY,
    96: dc.DROWZEE_DEX_ENTRY,
    97: dc.HYPNO_DEX_ENTRY,
    98: dc.KRABBY_DEX_ENTRY,
    99: dc.KINGLER_DEX_ENTRY,
    100: dc.VOLTORB_DEX_ENTRY,
    101: dc.ELECTRODE_DEX_ENTRY,
    102: dc.EXEGGCUTE_DEX_ENTRY,
    103: dc.EXEGGUTOR_DEX_ENTRY,
    104: dc.CUBONE_DEX_ENTRY,
    105: dc.MAROWAK_DEX_ENTRY,
    106: dc.HITMONLEE_DEX_ENTRY,
    107: dc.HITMONCHAN_DEX_ENTRY,
    108: dc.LICKITUNG_DEX_ENTRY,
    109: dc.KOFFING_DEX_ENTRY,
    110: dc.WEEZING_DEX_ENTRY,
    111: dc.RHYHORN_DEX_ENTRY,
    112: dc.RHYDON_DEX_ENTRY,
    113: dc.CHANSEY_DEX_ENTRY,
    114: dc.TANGELA_DEX_ENTRY,
    115: dc.KANGASKHAN_DEX_ENTRY,
    116: dc.HORSEA_DEX_ENTRY,
    117: dc.SEADRA_DEX_ENTRY,
    118: dc.GOLDEEN_DEX_ENTRY,
    119: dc.SEAKING_DEX_ENTRY,
    120: dc.STARYU_DEX_ENTRY,
    121: dc.STARMIE_DEX_ENTRY,
    122: dc.MR_MIME_DEX_ENTRY,
    123: dc.SCYTHER_DEX_ENTRY,
    124: dc.JYNX_DEX_ENTRY,
    125: dc.ELECTABUZZ_DEX_ENTRY,
    126: dc.MAGMAR_DEX_ENTRY,
    127: dc.PINSIR_DEX_ENTRY,
    128: dc.TAUROS_DEX_ENTRY,
    129: dc.MAGIKARP_DEX_ENTRY,
    130: dc.GYARADOS_DEX_ENTRY,
    131: dc.LAPRAS_DEX_ENTRY,
    132: dc.DITTO_DEX_ENTRY,
    133: dc.EEVEE_DEX_ENTRY,
    134: dc.VAPOREON_DEX_ENTRY,
    135: dc.JOLTEON_DEX_ENTRY,
    136: dc.FLAREON_DEX_ENTRY,
    137: dc.PORYGON_DEX_ENTRY,
    138: dc.OMANYTE_DEX_ENTRY,
    139: dc.OMASTAR_DEX_ENTRY,
    140: dc.KABUTO_DEX_ENTRY,
    141: dc.KABUTOPS_DEX_ENTRY,
    142: dc.AERODACTYL_DEX_ENTRY,
    143: dc.SNORLAX_DEX_ENTRY,
    144: dc.ARTICUNO_DEX_ENTRY,
    145: dc.ZAPDOS_DEX_ENTRY,
    146: dc.MOLTRES_DEX_ENTRY,
    147: dc.DRATINI_DEX_ENTRY,
    148: dc.DRAGONAIR_DEX_ENTRY,
    149: dc.DRAGONITE_DEX_ENTRY,
    150: dc.MEWTWO_DEX_ENTRY,
    151: dc.MEW_DEX_ENTRY
}


def get_mon(specname: str | int) -> str | int:
    """Return the Pokedex number of the Pokemon with the given name."""
    if isinstance(specname, str):
        return DEX_HELPER_STR_TO_NUM[specname]
    if isinstance(specname, int):
        return POKEDEX[specname].name
    raise TypeError("Invalid type given. Must be str or int.")


# ! Fix directory/package structure!!!!
