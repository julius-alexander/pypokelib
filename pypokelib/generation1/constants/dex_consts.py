"""Defines PokeDex constants for the PokeDex in terms of dex entries, as follows:\n
=============================================================\n
name: str
base_stats: NamedTuple[str, int]
types: list[str]
base_exp: int
growth_rate: str
tmhm_learnset: list[str]
"""  # pylint: disable=too-many-lines
from typing import NamedTuple
from pypokelib.generation1.data.moves import move_learnsets as ml
from pypokelib.generation1.constants.move_consts import BaseMoves

BaseStats = NamedTuple(
    "BaseStats",
    [
        ("total", int),
        ("hp", int),
        ("atk", int),
        ("defe", int),
        ("sp_atk", int),
        ("sp_def", int),
        ("spd", int),
    ],
)

FullPokeEntry = NamedTuple(
    "FullPokeEntry",
    [
        ("name", str),
        ("base_stats", BaseStats),
        ("types", list[str]),
        ("base_exp", int),
        ("growth_rate", str),
        ("tmhm_learnset", tuple[BaseMoves]),
    ],
)


MISSINGNO_ENTRY = FullPokeEntry(
    name="MissingNo.",
    base_stats=BaseStats(0, 0, 0, 0, 0, 0, 0),
    types=["Bird", "Normal"],
    base_exp=None,
    growth_rate=None,
    tmhm_learnset=(),
)
BULBASAUR_DEX_ENTRY = FullPokeEntry(
    name="Bulbasaur",
    base_stats=BaseStats(318, 45, 49, 49, 65, 65, 45),
    types=["Grass", "Poison"],
    base_exp=64,
    growth_rate="Medium Slow",
    tmhm_learnset=ml.BULBASAUR_LEARNSET
)
IVYSAUR_DEX_ENTRY = FullPokeEntry(
    name="Ivysaur",
    base_stats=BaseStats(405, 60, 62, 63, 80, 80, 60),
    types=["Grass", "Poison"],
    base_exp=142,
    growth_rate="Medium Slow",
    tmhm_learnset=ml.IVYSAUR_LEARNSET
)
VENUSAUR_DEX_ENTRY = FullPokeEntry(
    name="Venusaur",
    base_stats=BaseStats(525, 80, 82, 83, 100, 100, 80),
    types=["Grass", "Poison"],
    base_exp=236,
    growth_rate="Medium Slow",
    tmhm_learnset=ml.VENUSAUR_LEARNSET
)
CHARMANDER_DEX_ENTRY = FullPokeEntry(
    name="Charmander",
    base_stats=BaseStats(309, 39, 52, 43, 60, 50, 65),
    types=["Fire", ""],
    base_exp=62,
    growth_rate="Medium Slow",
    tmhm_learnset=ml.CHARMANDER_LEARNSET
)
CHARMELEON_DEX_ENTRY = FullPokeEntry(
    name="Charmeleon",
    base_stats=BaseStats(405, 58, 64, 58, 80, 65, 80),
    types=["Fire", ""],
    base_exp=142,
    growth_rate="Medium Slow",
    tmhm_learnset=ml.CHARMELEON_LEARNSET
)
CHARIZARD_DEX_ENTRY = FullPokeEntry(
    name="Charizard",
    base_stats=BaseStats(534, 78, 84, 78, 109, 85, 100),
    types=["Fire", "Flying"],
    base_exp=240,
    growth_rate="Medium Slow",
    tmhm_learnset=ml.CHARIZARD_LEARNSET
)
SQUIRTLE_DEX_ENTRY = FullPokeEntry(
    name="Squirtle",
    base_stats=BaseStats(314, 44, 48, 65, 50, 64, 43),
    types=["Water", ""],
    base_exp=63,
    growth_rate="Medium Slow",
    tmhm_learnset=ml.SQUIRTLE_LEARNSET
)
WARTORTLE_DEX_ENTRY = FullPokeEntry(
    name="Wartortle",
    base_stats=BaseStats(405, 59, 63, 80, 65, 80, 58),
    types=["Water", ""],
    base_exp=142,
    growth_rate="Medium Slow",
    tmhm_learnset=ml.WARTORTLE_LEARNSET
)
BLASTOISE_DEX_ENTRY = FullPokeEntry(
    name="Blastoise",
    base_stats=BaseStats(530, 79, 83, 100, 85, 105, 78),
    types=["Water", ""],
    base_exp=239,
    growth_rate="Medium Slow",
    tmhm_learnset=ml.BLASTOISE_LEARNSET
)
CATERPIE_DEX_ENTRY = FullPokeEntry(
    name="Caterpie",
    base_stats=BaseStats(195, 45, 30, 35, 20, 20, 45),
    types=["Bug", ""],
    base_exp=39,
    growth_rate="Medium Fast",
    tmhm_learnset=ml.CATERPIE_LEARNSET
)
METAPOD_DEX_ENTRY = FullPokeEntry(
    name="Metapod",
    base_stats=BaseStats(205, 50, 20, 55, 25, 25, 30),
    types=["Bug", ""],
    base_exp=72,
    growth_rate="Medium Fast",
    tmhm_learnset=ml.METAPOD_LEARNSET
)
BUTTERFREE_DEX_ENTRY = FullPokeEntry(
    name="Butterfree",
    base_stats=BaseStats(395, 60, 45, 50, 90, 80, 70),
    types=["Bug", "Flying"],
    base_exp=178,
    growth_rate="Medium Fast",
    tmhm_learnset=ml.BUTTERFREE_LEARNSET
)
WEEDLE_DEX_ENTRY = FullPokeEntry(
    name="Weedle",
    base_stats=BaseStats(195, 40, 35, 30, 20, 20, 50),
    types=["Bug", "Poison"],
    base_exp=39,
    growth_rate="Medium Fast",
    tmhm_learnset=ml.WEEDLE_LEARNSET
)
KAKUNA_DEX_ENTRY = FullPokeEntry(
    name="Kakuna",
    base_stats=BaseStats(205, 45, 25, 50, 25, 25, 35),
    types=["Bug", "Poison"],
    base_exp=72,
    growth_rate="Medium Fast",
    tmhm_learnset=ml.KAKUNA_LEARNSET
)
BEEDRILL_DEX_ENTRY = FullPokeEntry(
    name="Beedrill",
    base_stats=BaseStats(395, 65, 80, 40, 45, 80, 75),
    types=["Bug", "Poison"],
    base_exp=178,
    growth_rate="Medium Fast",
    tmhm_learnset=ml.BEEDRILL_LEARNSET
)
PIDGEY_DEX_ENTRY = FullPokeEntry(
    name="Pidgey",
    base_stats=BaseStats(251, 40, 45, 40, 35, 35, 56),
    types=["Normal", "Flying"],
    base_exp=50,
    growth_rate="Medium Slow",
    tmhm_learnset=ml.PIDGEY_LEARNSET
)
PIDGEOTTO_DEX_ENTRY = FullPokeEntry(
    name="Pidgeotto",
    base_stats=BaseStats(349, 63, 60, 55, 50, 50, 71),
    types=["Normal", "Flying"],
    base_exp=122,
    growth_rate="Medium Slow",
    tmhm_learnset=ml.PIDGEOTTO_LEARNSET
)
PIDGEOT_DEX_ENTRY = FullPokeEntry(
    name="Pidgeot",
    base_stats=BaseStats(479, 83, 80, 75, 70, 70, 101),
    types=["Normal", "Flying"],
    base_exp=211,
    growth_rate="Medium Slow",
    tmhm_learnset=ml.PIDGEOT_LEARNSET
)
RATTATA_DEX_ENTRY = FullPokeEntry(
    name="Rattata",
    base_stats=BaseStats(253, 30, 56, 35, 25, 35, 72),
    types=["Normal", ""],
    base_exp=51,
    growth_rate="Medium Fast",
    tmhm_learnset=ml.RATTATA_LEARNSET
)
RATICATE_DEX_ENTRY = FullPokeEntry(
    name="Raticate",
    base_stats=BaseStats(413, 55, 81, 60, 50, 70, 97),
    types=["Normal", ""],
    base_exp=145,
    growth_rate="Medium Fast",
    tmhm_learnset=ml.RATICATE_LEARNSET
)
SPEAROW_DEX_ENTRY = FullPokeEntry(
    name="Spearow",
    base_stats=BaseStats(262, 40, 60, 30, 31, 31, 70),
    types=["Normal", "Flying"],
    base_exp=52,
    growth_rate="Medium Fast",
    tmhm_learnset=ml.SPEAROW_LEARNSET
)
FEAROW_DEX_ENTRY = FullPokeEntry(
    name="Fearow",
    base_stats=BaseStats(442, 65, 90, 65, 61, 61, 100),
    types=["Normal", "Flying"],
    base_exp=155,
    growth_rate="Medium Fast",
    tmhm_learnset=ml.FEAROW_LEARNSET
)
EKANS_DEX_ENTRY = FullPokeEntry(
    name="Ekans",
    base_stats=BaseStats(288, 35, 60, 44, 40, 54, 55),
    types=["Poison", ""],
    base_exp=58,
    growth_rate="Medium Fast",
    tmhm_learnset=ml.EKANS_LEARNSET
)
ARBOK_DEX_ENTRY = FullPokeEntry(
    name="Arbok",
    base_stats=BaseStats(448, 60, 95, 69, 65, 79, 80),
    types=["Poison", ""],
    base_exp=153,
    growth_rate="Medium Fast",
    tmhm_learnset=ml.ARBOK_LEARNSET
)
PIKACHU_DEX_ENTRY = FullPokeEntry(
    name="Pikachu",
    base_stats=BaseStats(320, 35, 55, 40, 50, 50, 90),
    types=["Electric", ""],
    base_exp=82,
    growth_rate="Medium Fast",
    tmhm_learnset=ml.PIKACHU_LEARNSET
)
RAICHU_DEX_ENTRY = FullPokeEntry(
    name="Raichu",
    base_stats=BaseStats(485, 60, 90, 55, 90, 80, 110),
    types=["Electric", ""],
    base_exp=122,
    growth_rate="Medium Fast",
    tmhm_learnset=ml.RAICHU_LEARNSET
)
SANDSHREW_DEX_ENTRY = FullPokeEntry(
    name="Sandshrew",
    base_stats=BaseStats(300, 50, 75, 85, 20, 30, 40),
    types=["Ground", ""],
    base_exp=60,
    growth_rate="Medium Fast",
    tmhm_learnset=ml.SANDSHREW_LEARNSET
)
SANDSLASH_DEX_ENTRY = FullPokeEntry(
    name="Sandslash",
    base_stats=BaseStats(450, 75, 100, 110, 45, 55, 65),
    types=["Ground", ""],
    base_exp=158,
    growth_rate="Medium Fast",
    tmhm_learnset=ml.SANDSLASH_LEARNSET
)
NIDORAN_F_DEX_ENTRY = FullPokeEntry(
    name="Nidoran♀",
    base_stats=BaseStats(275, 55, 47, 52, 40, 40, 41),
    types=["Poison", ""],
    base_exp=55,
    growth_rate="Medium Slow",
    tmhm_learnset=ml.NIDORAN_F_LEARNSET
)
NIDORINA_DEX_ENTRY = FullPokeEntry(
    name="Nidorina",
    base_stats=BaseStats(365, 70, 62, 67, 55, 55, 56),
    types=["Poison", ""],
    base_exp=128,
    growth_rate="Medium Slow",
    tmhm_learnset=ml.NIDORINA_LEARNSET
)
NIDOQUEEN_DEX_ENTRY = FullPokeEntry(
    name="Nidoqueen",
    base_stats=BaseStats(505, 90, 92, 87, 75, 85, 76),
    types=["Poison", "Ground"],
    base_exp=223,
    growth_rate="Medium Slow",
    tmhm_learnset=ml.NIDOQUEEN_LEARNSET
)
NIDORAN_M_DEX_ENTRY = FullPokeEntry(
    name="Nidoran♂",
    base_stats=BaseStats(273, 46, 57, 40, 40, 40, 50),
    types=["Poison", ""],
    base_exp=55,
    growth_rate="Medium Slow",
    tmhm_learnset=ml.NIDORAN_M_LEARNSET
)
NIDORINO_DEX_ENTRY = FullPokeEntry(
    name="Nidorino",
    base_stats=BaseStats(365, 61, 72, 57, 55, 55, 65),
    types=["Poison", ""],
    base_exp=128,
    growth_rate="Medium Slow",
    tmhm_learnset=ml.NIDORINO_LEARNSET
)
NIDOKING_DEX_ENTRY = FullPokeEntry(
    name="Nidoking",
    base_stats=BaseStats(505, 81, 102, 77, 85, 75, 85),
    types=["Poison", "Ground"],
    base_exp=223,
    growth_rate="Medium Slow",
    tmhm_learnset=ml.NIDOKING_LEARNSET
)
CLEFAIRY_DEX_ENTRY = FullPokeEntry(
    name="Clefairy",
    base_stats=BaseStats(323, 70, 45, 48, 60, 65, 35),
    types=["Normal", ""],
    base_exp=113,
    growth_rate="Fast",
    tmhm_learnset=ml.CLEFAIRY_LEARNSET
)
CLEFABLE_DEX_ENTRY = FullPokeEntry(
    name="Clefable",
    base_stats=BaseStats(483, 95, 70, 73, 95, 90, 60),
    types=["Normal", ""],
    base_exp=213,
    growth_rate="Fast",
    tmhm_learnset=ml.CLEFABLE_LEARNSET
)
VULPIX_DEX_ENTRY = FullPokeEntry(
    name="Vulpix",
    base_stats=BaseStats(299, 38, 41, 40, 50, 65, 65),
    types=["Fire", ""],
    base_exp=60,
    growth_rate="Medium Fast",
    tmhm_learnset=ml.VULPIX_LEARNSET
)
NINETALES_DEX_ENTRY = FullPokeEntry(
    name="Ninetales",
    base_stats=BaseStats(505, 73, 76, 75, 81, 100, 100),
    types=["Fire", ""],
    base_exp=177,
    growth_rate="Medium Fast",
    tmhm_learnset=ml.NINETALES_LEARNSET
)
JIGGLYPUFF_DEX_ENTRY = FullPokeEntry(
    name="Jigglypuff",
    base_stats=BaseStats(270, 115, 45, 20, 45, 25, 20),
    types=["Normal", ""],
    base_exp=76,
    growth_rate="Fast",
    tmhm_learnset=ml.JIGGLYPUFF_LEARNSET
)
WIGGLYTUFF_DEX_ENTRY = FullPokeEntry(
    name="Wigglytuff",
    base_stats=BaseStats(435, 140, 70, 45, 85, 50, 45),
    types=["Normal", ""],
    base_exp=109,
    growth_rate="Fast",
    tmhm_learnset=ml.WIGGLYTUFF_LEARNSET
)
ZUBAT_DEX_ENTRY = FullPokeEntry(
    name="Zubat",
    base_stats=BaseStats(245, 40, 45, 35, 30, 40, 55),
    types=["Poison", "Flying"],
    base_exp=49,
    growth_rate="Medium Fast",
    tmhm_learnset=ml.ZUBAT_LEARNSET
)
GOLBAT_DEX_ENTRY = FullPokeEntry(
    name="Golbat",
    base_stats=BaseStats(385, 75, 80, 70, 65, 75, 90),
    types=["Poison", "Flying"],
    base_exp=159,
    growth_rate="Medium Fast",
    tmhm_learnset=ml.GOLBAT_LEARNSET
)
ODDISH_DEX_ENTRY = FullPokeEntry(
    name="Oddish",
    base_stats=BaseStats(320, 45, 50, 55, 75, 65, 30),
    types=["Grass", "Poison"],
    base_exp=64,
    growth_rate="Medium Slow",
    tmhm_learnset=ml.ODDISH_LEARNSET
)
GLOOM_DEX_ENTRY = FullPokeEntry(
    name="Gloom",
    base_stats=BaseStats(395, 60, 65, 70, 85, 75, 40),
    types=["Grass", "Poison"],
    base_exp=138,
    growth_rate="Medium Slow",
    tmhm_learnset=ml.GLOOM_LEARNSET
)
VILEPLUME_DEX_ENTRY = FullPokeEntry(
    name="Vileplume",
    base_stats=BaseStats(490, 75, 80, 85, 110, 90, 50),
    types=["Grass", "Poison"],
    base_exp=216,
    growth_rate="Medium Slow",
    tmhm_learnset=ml.VILEPLUME_LEARNSET
)
PARAS_DEX_ENTRY = FullPokeEntry(
    name="Paras",
    base_stats=BaseStats(285, 35, 70, 55, 45, 55, 25),
    types=["Bug", "Grass"],
    base_exp=57,
    growth_rate="Medium Fast",
    tmhm_learnset=ml.PARAS_LEARNSET
)
PARASECT_DEX_ENTRY = FullPokeEntry(
    name="Parasect",
    base_stats=BaseStats(405, 60, 95, 80, 60, 80, 30),
    types=["Bug", "Grass"],
    base_exp=142,
    growth_rate="Medium Fast",
    tmhm_learnset=ml.PARASECT_LEARNSET
)
VENONAT_DEX_ENTRY = FullPokeEntry(
    name="Venonat",
    base_stats=BaseStats(305, 60, 55, 50, 40, 55, 45),
    types=["Bug", "Poison"],
    base_exp=61,
    growth_rate="Medium Fast",
    tmhm_learnset=ml.VENONAT_LEARNSET
)
VENOMOTH_DEX_ENTRY = FullPokeEntry(
    name="Venomoth",
    base_stats=BaseStats(450, 70, 65, 60, 90, 75, 90),
    types=["Bug", "Poison"],
    base_exp=158,
    growth_rate="Medium Fast",
    tmhm_learnset=ml.VENOMOTH_LEARNSET
)
DIGLETT_DEX_ENTRY = FullPokeEntry(
    name="Diglett",
    base_stats=BaseStats(265, 10, 55, 25, 35, 45, 95),
    types=["Ground", ""],
    base_exp=53,
    growth_rate="Medium Fast",
    tmhm_learnset=ml.DIGLETT_LEARNSET
)
DUGTRIO_DEX_ENTRY = FullPokeEntry(
    name="Dugtrio",
    base_stats=BaseStats(405, 35, 80, 50, 50, 70, 120),
    types=["Ground", ""],
    base_exp=149,
    growth_rate="Medium Fast",
    tmhm_learnset=ml.DUGTRIO_LEARNSET
)
MEOWTH_DEX_ENTRY = FullPokeEntry(
    name="Meowth",
    base_stats=BaseStats(290, 40, 45, 35, 40, 40, 90),
    types=["Normal", ""],
    base_exp=58,
    growth_rate="Medium Fast",
    tmhm_learnset=ml.MEOWTH_LEARNSET
)
PERSIAN_DEX_ENTRY = FullPokeEntry(
    name="Persian",
    base_stats=BaseStats(440, 65, 70, 60, 65, 65, 115),
    types=["Normal", ""],
    base_exp=154,
    growth_rate="Medium Fast",
    tmhm_learnset=ml.PERSIAN_LEARNSET
)
PSYDUCK_DEX_ENTRY = FullPokeEntry(
    name="Psyduck",
    base_stats=BaseStats(320, 50, 52, 48, 65, 50, 55),
    types=["Water", ""],
    base_exp=64,
    growth_rate="Medium Fast",
    tmhm_learnset=ml.PSYDUCK_LEARNSET
)
GOLDUCK_DEX_ENTRY = FullPokeEntry(
    name="Golduck",
    base_stats=BaseStats(500, 80, 82, 78, 95, 80, 85),
    types=["Water", ""],
    base_exp=175,
    growth_rate="Medium Fast",
    tmhm_learnset=ml.GOLDUCK_LEARNSET
)
MANKEY_DEX_ENTRY = FullPokeEntry(
    name="Mankey",
    base_stats=BaseStats(305, 40, 80, 35, 35, 45, 70),
    types=["Fighting", ""],
    base_exp=61,
    growth_rate="Medium Fast",
    tmhm_learnset=ml.MANKEY_LEARNSET
)
PRIMEAPE_DEX_ENTRY = FullPokeEntry(
    name="Primeape",
    base_stats=BaseStats(455, 65, 105, 60, 60, 70, 95),
    types=["Fighting", ""],
    base_exp=159,
    growth_rate="Medium Fast",
    tmhm_learnset=ml.PRIMEAPE_LEARNSET
)
GROWLITHE_DEX_ENTRY = FullPokeEntry(
    name="Growlithe",
    base_stats=BaseStats(350, 55, 70, 45, 70, 50, 60),
    types=["Fire", ""],
    base_exp=70,
    growth_rate="Slow",
    tmhm_learnset=ml.GROWLITHE_LEARNSET
)
ARCANINE_DEX_ENTRY = FullPokeEntry(
    name="Arcanine",
    base_stats=BaseStats(555, 90, 110, 80, 100, 80, 95),
    types=["Fire", ""],
    base_exp=194,
    growth_rate="Slow",
    tmhm_learnset=ml.ARCANINE_LEARNSET
)
POLIWAG_DEX_ENTRY = FullPokeEntry(
    name="Poliwag",
    base_stats=BaseStats(300, 40, 50, 40, 40, 40, 90),
    types=["Water", ""],
    base_exp=60,
    growth_rate="Medium Slow",
    tmhm_learnset=ml.POLIWAG_LEARNSET
)
POLIWHIRL_DEX_ENTRY = FullPokeEntry(
    name="Poliwhirl",
    base_stats=BaseStats(385, 65, 65, 65, 50, 50, 90),
    types=["Water", ""],
    base_exp=135,
    growth_rate="Medium Slow",
    tmhm_learnset=ml.POLIWHIRL_LEARNSET
)
POLIWRATH_DEX_ENTRY = FullPokeEntry(
    name="Poliwrath",
    base_stats=BaseStats(510, 90, 95, 95, 70, 90, 70),
    types=["Water", "Fighting"],
    base_exp=185,
    growth_rate="Medium Slow",
    tmhm_learnset=ml.POLIWRATH_LEARNSET
)
ABRA_DEX_ENTRY = FullPokeEntry(
    name="Abra",
    base_stats=BaseStats(310, 25, 20, 15, 105, 55, 90),
    types=["Psychic", ""],
    base_exp=62,
    growth_rate="Medium Slow",
    tmhm_learnset=ml.ABRA_LEARNSET
)
KADABRA_DEX_ENTRY = FullPokeEntry(
    name="Kadabra",
    base_stats=BaseStats(400, 40, 35, 30, 120, 70, 105),
    types=["Psychic", ""],
    base_exp=140,
    growth_rate="Medium Slow",
    tmhm_learnset=ml.KADABRA_LEARNSET
)
ALAKAZAM_DEX_ENTRY = FullPokeEntry(
    name="Alakazam",
    base_stats=BaseStats(500, 55, 50, 45, 135, 85, 120),
    types=["Psychic", ""],
    base_exp=221,
    growth_rate="Medium Slow",
    tmhm_learnset=ml.ALAKAZAM_LEARNSET
)
MACHOP_DEX_ENTRY = FullPokeEntry(
    name="Machop",
    base_stats=BaseStats(305, 70, 80, 50, 35, 35, 35),
    types=["Fighting", ""],
    base_exp=61,
    growth_rate="Medium Slow",
    tmhm_learnset=ml.MACHOP_LEARNSET
)
MACHOKE_DEX_ENTRY = FullPokeEntry( name="Machoke",
    base_stats=BaseStats(405, 80, 100, 70, 50, 60, 45),
    types=["Fighting", ""],
    base_exp=142,
    growth_rate="Medium Slow",
    tmhm_learnset= ml.MACHOKE_LEARNSET
)
MACHAMP_DEX_ENTRY = FullPokeEntry(
    name="Machamp",
    base_stats=BaseStats(505, 90, 130, 80, 65, 85, 55),
    types=["Fighting", ""],
    base_exp=227,
    growth_rate="Medium Slow",
    tmhm_learnset= ml.MACHAMP_LEARNSET
)
BELLSPROUT_DEX_ENTRY = FullPokeEntry(
    name="Bellsprout",
    base_stats=BaseStats(300, 50, 75, 35, 70, 30, 40),
    types=["Grass", "Poison"],
    base_exp=60,
    growth_rate="Medium Slow",
    tmhm_learnset= ml.BELLSPROUT_LEARNSET
)
WEEPINBELL_DEX_ENTRY = FullPokeEntry(
    name="Weepinbell",
    base_stats=BaseStats(390, 65, 90, 50, 85, 45, 55),
    types=["Grass", "Poison"],
    base_exp=137,
    growth_rate="Medium Slow",
    tmhm_learnset= ml.WEEPINBELL_LEARNSET
)
VICTREEBEL_DEX_ENTRY = FullPokeEntry(
    name="Victreebel",
    base_stats=BaseStats(490, 80, 105, 65, 100, 70, 70),
    types=["Grass", "Poison"],
    base_exp=216,
    growth_rate="Medium Slow",
    tmhm_learnset= ml.VICTREEBEL_LEARNSET
)
TENTACOOL_DEX_ENTRY = FullPokeEntry(
    name="Tentacool",
    base_stats=BaseStats(335, 40, 40, 35, 50, 100, 70),
    types=["Water", "Poison"],
    base_exp=67,
    growth_rate="Slow",
    tmhm_learnset= ml.TENTACOOL_LEARNSET
)
TENTACRUEL_DEX_ENTRY = FullPokeEntry(
    name="Tentacruel",
    base_stats=BaseStats(515, 80, 70, 65, 80, 120, 100),
    types=["Water", "Poison"],
    base_exp=180,
    growth_rate="Slow",
    tmhm_learnset= ml.TENTACRUEL_LEARNSET
)
GEODUDE_DEX_ENTRY = FullPokeEntry(
    name="Geodude",
    base_stats=BaseStats(300, 40, 80, 100, 30, 30, 20),
    types=["Rock", "Ground"],
    base_exp=60,
    growth_rate="Medium Slow",
    tmhm_learnset= ml.GEODUDE_LEARNSET
)
GRAVELER_DEX_ENTRY = FullPokeEntry(
    name="Graveler",
    base_stats=BaseStats(390, 55, 95, 115, 45, 45, 35),
    types=["Rock", "Ground"],
    base_exp=137,
    growth_rate="Medium Slow",
    tmhm_learnset= ml.GRAVELER_LEARNSET
)
GOLEM_DEX_ENTRY = FullPokeEntry(
    name="Golem",
    base_stats=BaseStats(495, 80, 120, 130, 55, 65, 45),
    types=["Rock", "Ground"],
    base_exp=218,
    growth_rate="Medium Slow",
    tmhm_learnset= ml.GOLEM_LEARNSET
)
PONYTA_DEX_ENTRY = FullPokeEntry(
    name="Ponyta",
    base_stats=BaseStats(410, 50, 85, 55, 65, 65, 90),
    types=["Fire", ""],
    base_exp=82,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.PONYTA_LEARNSET
)
RAPIDASH_DEX_ENTRY = FullPokeEntry(
    name="Rapidash",
    base_stats=BaseStats(500, 65, 100, 70, 80, 80, 105),
    types=["Fire", ""],
    base_exp=175,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.RAPIDASH_LEARNSET
)
SLOWPOKE_DEX_ENTRY = FullPokeEntry(
    name="Slowpoke",
    base_stats=BaseStats(315, 90, 65, 65, 40, 40, 15),
    types=["Water", "Psychic"],
    base_exp=63,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.SLOWPOKE_LEARNSET
)
SLOWBRO_DEX_ENTRY = FullPokeEntry(
    name="Slowbro",
    base_stats=BaseStats(490, 95, 75, 110, 100, 80, 30),
    types=["Water", "Psychic"],
    base_exp=172,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.SLOWBRO_LEARNSET
)
MAGNEMITE_DEX_ENTRY = FullPokeEntry(
    name="Magnemite",
    base_stats=BaseStats(325, 25, 35, 70, 95, 55, 45),
    types=["Electric", ""],
    base_exp=65,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.MAGNEMITE_LEARNSET
)
MAGNETON_DEX_ENTRY = FullPokeEntry(
    name="Magneton",
    base_stats=BaseStats(465, 50, 60, 95, 120, 70, 70),
    types=["Electric", ""],
    base_exp=163,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.MAGNETON_LEARNSET
)
FARFETCHD_DEX_ENTRY = FullPokeEntry(
    name="Farfetch'd",
    base_stats=BaseStats(352, 52, 65, 55, 58, 62, 60),
    types=["Normal", "Flying"],
    base_exp=94,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.FARFETCHD_LEARNSET
)
DODUO_DEX_ENTRY = FullPokeEntry(
    name="Doduo",
    base_stats=BaseStats(310, 35, 85, 45, 35, 35, 75),
    types=["Normal", "Flying"],
    base_exp=62,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.DODUO_LEARNSET
)
DODRIO_DEX_ENTRY = FullPokeEntry(
    name="Dodrio",
    base_stats=BaseStats(460, 60, 110, 70, 60, 60, 100),
    types=["Normal", "Flying"],
    base_exp=161,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.DODRIO_LEARNSET
)
SEEL_DEX_ENTRY = FullPokeEntry(
    name="Seel",
    base_stats=BaseStats(325, 65, 45, 55, 45, 70, 45),
    types=["Water", ""],
    base_exp=65,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.SEEL_LEARNSET
)
DEWGONG_DEX_ENTRY = FullPokeEntry(
    name="Dewgong",
    base_stats=BaseStats(475, 90, 70, 80, 70, 95, 70),
    types=["Water", "Ice"],
    base_exp=166,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.DEWGONG_LEARNSET
)
GRIMER_DEX_ENTRY = FullPokeEntry(
    name="Grimer",
    base_stats=BaseStats(325, 80, 80, 50, 40, 50, 25),
    types=["Poison", ""],
    base_exp=65,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.GRIMER_LEARNSET
)
MUK_DEX_ENTRY = FullPokeEntry(
    name="Muk",
    base_stats=BaseStats(500, 105, 105, 75, 65, 100, 50),
    types=["Poison", ""],
    base_exp=175,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.MUK_LEARNSET
)
SHELLDER_DEX_ENTRY = FullPokeEntry(
    name="Shellder",
    base_stats=BaseStats(305, 30, 65, 100, 45, 25, 40),
    types=["Water", ""],
    base_exp=61,
    growth_rate="Slow",
    tmhm_learnset= ml.SHELLDER_LEARNSET
)
CLOYSTER_DEX_ENTRY = FullPokeEntry(
    name="Cloyster",
    base_stats=BaseStats(525, 50, 95, 180, 85, 45, 70),
    types=["Water", "Ice"],
    base_exp=184,
    growth_rate="Slow",
    tmhm_learnset= ml.CLOYSTER_LEARNSET
)
GASTLY_DEX_ENTRY = FullPokeEntry(
    name="Gastly",
    base_stats=BaseStats(310, 30, 35, 30, 100, 35, 80),
    types=["Ghost", "Poison"],
    base_exp=62,
    growth_rate="Medium Slow",
    tmhm_learnset= ml.GASTLY_LEARNSET
)
HAUNTER_DEX_ENTRY = FullPokeEntry(
    name="Haunter",
    base_stats=BaseStats(405, 45, 50, 45, 115, 55, 95),
    types=["Ghost", "Poison"],
    base_exp=142,
    growth_rate="Medium Slow",
    tmhm_learnset= ml.HAUNTER_LEARNSET
)
GENGAR_DEX_ENTRY = FullPokeEntry(
    name="Gengar",
    base_stats=BaseStats(500, 60, 65, 60, 130, 75, 110),
    types=["Ghost", "Poison"],
    base_exp=225,
    growth_rate="Medium Slow",
    tmhm_learnset= ml.GENGAR_LEARNSET
)
ONIX_DEX_ENTRY = FullPokeEntry(
    name="Onix",
    base_stats=BaseStats(385, 35, 45, 160, 30, 45, 70),
    types=["Rock", "Ground"],
    base_exp=77,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.ONIX_LEARNSET
)
DROWZEE_DEX_ENTRY = FullPokeEntry(
    name="Drowzee",
    base_stats=BaseStats(328, 60, 48, 45, 43, 90, 42),
    types=["Psychic", ""],
    base_exp=66,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.DROWZEE_LEARNSET
)
HYPNO_DEX_ENTRY = FullPokeEntry(
    name="Hypno",
    base_stats=BaseStats(483, 85, 73, 70, 73, 115, 67),
    types=["Psychic", ""],
    base_exp=169,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.HYPNO_LEARNSET
)
KRABBY_DEX_ENTRY = FullPokeEntry(
    name="Krabby",
    base_stats=BaseStats(325, 30, 105, 90, 25, 25, 50),
    types=["Water", ""],
    base_exp=65,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.KRABBY_LEARNSET
)
KINGLER_DEX_ENTRY = FullPokeEntry(
    name="Kingler",
    base_stats=BaseStats(475, 55, 130, 115, 50, 50, 75),
    types=["Water", ""],
    base_exp=166,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.KINGLER_LEARNSET
)
VOLTORB_DEX_ENTRY = FullPokeEntry(
    name="Voltorb",
    base_stats=BaseStats(330, 40, 30, 50, 55, 55, 100),
    types=["Electric", ""],
    base_exp=66,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.VOLTORB_LEARNSET
)
ELECTRODE_DEX_ENTRY = FullPokeEntry(
    name="Electrode",
    base_stats=BaseStats(480, 60, 50, 70, 80, 80, 140),
    types=["Electric", ""],
    base_exp=172,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.ELECTRODE_LEARNSET
)
EXEGGCUTE_DEX_ENTRY = FullPokeEntry(
    name="Exeggcute",
    base_stats=BaseStats(325, 60, 40, 80, 60, 45, 40),
    types=["Grass", "Psychic"],
    base_exp=65,
    growth_rate="Slow",
    tmhm_learnset= ml.EXEGGCUTE_LEARNSET
)
EXEGGUTOR_DEX_ENTRY = FullPokeEntry(
    name="Exeggutor",
    base_stats=BaseStats(520, 95, 95, 85, 125, 65, 55),
    types=["Grass", "Psychic"],
    base_exp=186,
    growth_rate="Slow",
    tmhm_learnset= ml.EXEGGUTOR_LEARNSET
)
CUBONE_DEX_ENTRY = FullPokeEntry(
    name="Cubone",
    base_stats=BaseStats(320, 50, 50, 95, 40, 50, 35),
    types=["Ground", ""],
    base_exp=64,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.CUBONE_LEARNSET
)
MAROWAK_DEX_ENTRY = FullPokeEntry(
    name="Marowak",
    base_stats=BaseStats(425, 60, 80, 110, 50, 80, 45),
    types=["Ground", ""],
    base_exp=149,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.MAROWAK_LEARNSET
)
HITMONLEE_DEX_ENTRY = FullPokeEntry(
    name="Hitmonlee",
    base_stats=BaseStats(455, 50, 120, 53, 35, 110, 87),
    types=["Fighting", ""],
    base_exp=159,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.HITMONLEE_LEARNSET
)
HITMONCHAN_DEX_ENTRY = FullPokeEntry(
    name="Hitmonchan",
    base_stats=BaseStats(455, 50, 105, 79, 35, 110, 76),
    types=["Fighting", ""],
    base_exp=159,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.HITMONCHAN_LEARNSET
)
LICKITUNG_DEX_ENTRY = FullPokeEntry(
    name="Lickitung",
    base_stats=BaseStats(385, 90, 55, 75, 60, 75, 30),
    types=["Normal", ""],
    base_exp=77,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.LICKITUNG_LEARNSET
)
KOFFING_DEX_ENTRY = FullPokeEntry(
    name="Koffing",
    base_stats=BaseStats(340, 40, 65, 95, 60, 45, 35),
    types=["Poison", ""],
    base_exp=68,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.KOFFING_LEARNSET
)
WEEZING_DEX_ENTRY = FullPokeEntry(
    name="Weezing",
    base_stats=BaseStats(490, 65, 90, 120, 85, 70, 60),
    types=["Poison", ""],
    base_exp=172,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.WEEZING_LEARNSET
)
RHYHORN_DEX_ENTRY = FullPokeEntry(
    name="Rhyhorn",
    base_stats=BaseStats(345, 80, 85, 95, 30, 30, 25),
    types=["Ground", "Rock"],
    base_exp=69,
    growth_rate="Slow",
    tmhm_learnset= ml.RHYHORN_LEARNSET
)
RHYDON_DEX_ENTRY = FullPokeEntry(
    name="Rhydon",
    base_stats=BaseStats(485, 105, 130, 120, 45, 45, 40),
    types=["Ground", "Rock"],
    base_exp=170,
    growth_rate="Slow",
    tmhm_learnset= ml.RHYDON_LEARNSET
)
CHANSEY_DEX_ENTRY = FullPokeEntry(
    name="Chansey",
    base_stats=BaseStats(450, 250, 5, 5, 35, 105, 50),
    types=["Normal", ""],
    base_exp=395,
    growth_rate="Fast",
    tmhm_learnset= ml.CHANSEY_LEARNSET
)
TANGELA_DEX_ENTRY = FullPokeEntry(
    name="Tangela",
    base_stats=BaseStats(435, 65, 55, 115, 100, 40, 60),
    types=["Grass", ""],
    base_exp=166,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.TANGELA_LEARNSET
)
KANGASKHAN_DEX_ENTRY = FullPokeEntry(
    name="Kangaskhan",
    base_stats=BaseStats(490, 105, 95, 80, 40, 80, 90),
    types=["Normal", ""],
    base_exp=172,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.KANGASKHAN_LEARNSET
)
HORSEA_DEX_ENTRY = FullPokeEntry(
    name="Horsea",
    base_stats=BaseStats(295, 30, 40, 70, 70, 25, 60),
    types=["Water", ""],
    base_exp=59,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.HORSEA_LEARNSET
)
SEADRA_DEX_ENTRY = FullPokeEntry(
    name="Seadra",
    base_stats=BaseStats(440, 55, 65, 95, 95, 45, 85),
    types=["Water", ""],
    base_exp=154,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.SEADRA_LEARNSET
)
GOLDEEN_DEX_ENTRY = FullPokeEntry(
    name="Goldeen",
    base_stats=BaseStats(320, 45, 67, 60, 35, 50, 63),
    types=["Water", ""],
    base_exp=64,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.GOLDEEN_LEARNSET
)
SEAKING_DEX_ENTRY = FullPokeEntry(
    name="Seaking",
    base_stats=BaseStats(450, 80, 92, 65, 65, 80, 68),
    types=["Water", ""],
    base_exp=158,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.SEAKING_LEARNSET
)
STARYU_DEX_ENTRY = FullPokeEntry(
    name="Staryu",
    base_stats=BaseStats(340, 30, 45, 55, 70, 55, 85),
    types=["Water", ""],
    base_exp=68,
    growth_rate="Slow",
    tmhm_learnset= ml.STARYU_LEARNSET
)
STARMIE_DEX_ENTRY = FullPokeEntry(
    name="Starmie",
    base_stats=BaseStats(520, 60, 75, 85, 100, 85, 115),
    types=["Water", "Psychic"],
    base_exp=182,
    growth_rate="Slow",
    tmhm_learnset= ml.STARMIE_LEARNSET
)
MR_MIME_DEX_ENTRY = FullPokeEntry(
    name="Mr. Mime",
    base_stats=BaseStats(460, 40, 45, 65, 100, 120, 90),
    types=["Psychic", ""],
    base_exp=161,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.MR_MIME_LEARNSET
)
SCYTHER_DEX_ENTRY = FullPokeEntry(
    name="Scyther",
    base_stats=BaseStats(500, 70, 110, 80, 55, 80, 105),
    types=["Bug", "Flying"],
    base_exp=100,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.SCYTHER_LEARNSET
)
JYNX_DEX_ENTRY = FullPokeEntry(
    name="Jynx",
    base_stats=BaseStats(455, 65, 50, 35, 115, 95, 95),
    types=["Ice", "Psychic"],
    base_exp=159,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.JYNX_LEARNSET
)
ELECTABUZZ_DEX_ENTRY = FullPokeEntry(
    name="Electabuzz",
    base_stats=BaseStats(490, 65, 83, 57, 95, 85, 105),
    types=["Electric", ""],
    base_exp=172,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.ELECTABUZZ_LEARNSET
)
MAGMAR_DEX_ENTRY = FullPokeEntry(
    name="Magmar",
    base_stats=BaseStats(495, 65, 95, 57, 100, 85, 93),
    types=["Fire", ""],
    base_exp=173,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.MAGMAR_LEARNSET
)
PINSIR_DEX_ENTRY = FullPokeEntry(
    name="Pinsir",
    base_stats=BaseStats(500, 65, 125, 100, 55, 70, 85),
    types=["Bug", ""],
    base_exp=175,
    growth_rate="Slow",
    tmhm_learnset= ml.PINSIR_LEARNSET
)
TAUROS_DEX_ENTRY = FullPokeEntry(
    name="Tauros",
    base_stats=BaseStats(490, 75, 100, 95, 40, 70, 110),
    types=["Normal", ""],
    base_exp=172,
    growth_rate="Slow",
    tmhm_learnset= ml.TAUROS_LEARNSET
)
MAGIKARP_DEX_ENTRY = FullPokeEntry(
    name="Magikarp",
    base_stats=BaseStats(200, 20, 10, 55, 15, 20, 80),
    types=["Water", ""],
    base_exp=40,
    growth_rate="Slow",
    tmhm_learnset= ml.MAGIKARP_LEARNSET
)
GYARADOS_DEX_ENTRY = FullPokeEntry(
    name="Gyarados",
    base_stats=BaseStats(540, 95, 125, 79, 60, 100, 81),
    types=["Water", "Flying"],
    base_exp=189,
    growth_rate="Slow",
    tmhm_learnset= ml.GYARADOS_LEARNSET
)
LAPRAS_DEX_ENTRY = FullPokeEntry(
    name="Lapras",
    base_stats=BaseStats(535, 130, 85, 80, 85, 95, 60),
    types=["Water", "Ice"],
    base_exp=187,
    growth_rate="Slow",
    tmhm_learnset= ml.LAPRAS_LEARNSET
)
DITTO_DEX_ENTRY = FullPokeEntry(
    name="Ditto",
    base_stats=BaseStats(288, 48, 48, 48, 48, 48, 48),
    types=["Normal", ""],
    base_exp=61,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.DITTO_LEARNSET
)
EEVEE_DEX_ENTRY = FullPokeEntry(
    name="Eevee",
    base_stats=BaseStats(325, 55, 55, 50, 45, 65, 55),
    types=["Normal", ""],
    base_exp=65,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.EEVEE_LEARNSET
)
VAPOREON_DEX_ENTRY = FullPokeEntry(
    name="Vaporeon",
    base_stats=BaseStats(525, 130, 65, 60, 110, 95, 65),
    types=["Water", ""],
    base_exp=184,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.VAPOREON_LEARNSET
)
JOLTEON_DEX_ENTRY = FullPokeEntry(
    name="Jolteon",
    base_stats=BaseStats(525, 65, 65, 60, 110, 95, 130),
    types=["Electric", ""],
    base_exp=184,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.JOLTEON_LEARNSET
)
FLAREON_DEX_ENTRY = FullPokeEntry(
    name="Flareon",
    base_stats=BaseStats(525, 65, 130, 60, 95, 110, 65),
    types=["Fire", ""],
    base_exp=184,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.FLAREON_LEARNSET
)
PORYGON_DEX_ENTRY = FullPokeEntry(
    name="Porygon",
    base_stats=BaseStats(395, 65, 60, 70, 85, 75, 40),
    types=["Normal", ""],
    base_exp=79,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.PORYGON_LEARNSET
)
OMANYTE_DEX_ENTRY = FullPokeEntry(
    name="Omanyte",
    base_stats=BaseStats(355, 35, 40, 100, 90, 55, 35),
    types=["Rock", "Water"],
    base_exp=71,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.OMANYTE_LEARNSET
)
OMASTAR_DEX_ENTRY = FullPokeEntry(
    name="Omastar",
    base_stats=BaseStats(495, 70, 60, 125, 115, 70, 55),
    types=["Rock", "Water"],
    base_exp=173,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.OMASTAR_LEARNSET
)
KABUTO_DEX_ENTRY = FullPokeEntry(
    name="Kabuto",
    base_stats=BaseStats(355, 30, 80, 90, 55, 45, 55),
    types=["Rock", "Water"],
    base_exp=71,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.KABUTO_LEARNSET
)
KABUTOPS_DEX_ENTRY = FullPokeEntry(
    name="Kabutops",
    base_stats=BaseStats(495, 60, 115, 105, 65, 70, 80),
    types=["Rock", "Water"],
    base_exp=173,
    growth_rate="Medium Fast",
    tmhm_learnset= ml.KABUTOPS_LEARNSET
)
AERODACTYL_DEX_ENTRY = FullPokeEntry(
    name="Aerodactyl",
    base_stats=BaseStats(515, 80, 105, 65, 60, 75, 130),
    types=["Rock", "Flying"],
    base_exp=180,
    growth_rate="Slow",
    tmhm_learnset= ml.AERODACTYL_LEARNSET
)
SNORLAX_DEX_ENTRY = FullPokeEntry(
    name="Snorlax",
    base_stats=BaseStats(540, 160, 110, 65, 65, 110, 30),
    types=["Normal", ""],
    base_exp=189,
    growth_rate="Slow",
    tmhm_learnset= ml.SNORLAX_LEARNSET
)
ARTICUNO_DEX_ENTRY = FullPokeEntry(
    name="Articuno",
    base_stats=BaseStats(580, 90, 85, 100, 95, 125, 85),
    types=["Ice", "Flying"],
    base_exp=261,
    growth_rate="Slow",
    tmhm_learnset= ml.ARTICUNO_LEARNSET
)
ZAPDOS_DEX_ENTRY = FullPokeEntry(
    name="Zapdos",
    base_stats=BaseStats(580, 90, 90, 85, 125, 90, 100),
    types=["Electric", "Flying"],
    base_exp=261,
    growth_rate="Slow",
    tmhm_learnset= ml.ZAPDOS_LEARNSET
)
MOLTRES_DEX_ENTRY = FullPokeEntry(
    name="Moltres",
    base_stats=BaseStats(580, 90, 100, 90, 125, 85, 90),
    types=["Fire", "Flying"],
    base_exp=261,
    growth_rate="Slow",
    tmhm_learnset= ml.MOLTRES_LEARNSET
)
DRATINI_DEX_ENTRY = FullPokeEntry(
    name="Dratini",
    base_stats=BaseStats(300, 41, 64, 45, 50, 50, 50),
    types=["Dragon", ""],
    base_exp=60,
    growth_rate="Slow",
    tmhm_learnset= ml.DRATINI_LEARNSET
)
DRAGONAIR_DEX_ENTRY = FullPokeEntry(
    name="Dragonair",
    base_stats=BaseStats(420, 61, 84, 65, 70, 70, 70),
    types=["Dragon", ""],
    base_exp=147,
    growth_rate="Slow",
    tmhm_learnset= ml.DRAGONAIR_LEARNSET
)
DRAGONITE_DEX_ENTRY = FullPokeEntry(
    name="Dragonite",
    base_stats=BaseStats(600, 91, 134, 95, 100, 100, 80),
    types=["Dragon", "Flying"],
    base_exp=270,
    growth_rate="Slow",
    tmhm_learnset= ml.DRAGONITE_LEARNSET
)
MEWTWO_DEX_ENTRY = FullPokeEntry(
    name="Mewtwo",
    base_stats=BaseStats(680, 106, 110, 90, 154, 90, 130),
    types=["Psychic", ""],
    base_exp=306,
    growth_rate="Slow",
    tmhm_learnset= ml.MEWTWO_LEARNSET
)
MEW_DEX_ENTRY = FullPokeEntry(
    name="Mew",
    base_stats=BaseStats(600, 100, 100, 100, 100, 100, 100),
    types=["Psychic", ""],
    base_exp=270,
    growth_rate="Medium Slow",
    tmhm_learnset= ml.MEW_LEARNSET
)
