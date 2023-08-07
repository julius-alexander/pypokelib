"""Defines base stats for each move.\n
Example: Absorb, Grass, Special, 20, 100, 25, Absorbs 1/2 damage inflicted.\n"""
from typing import NamedTuple

# * In Generation 1, all attacks of a type are either physical or special.
# * e.g., ALL fire attacks are special, ALL fighting attacks are physical.
# * Thus, no need to specify category in the BaseMoves NamedTuple.
BaseMoves = NamedTuple(
    "BaseMoves",
    [
        ("name", str),
        ("type", str),
        ("power", int),
        ("accuracy", int),
        ("pp", int),
        ("effect", str),
    ],
)
NO_MOVE = BaseMoves(
    name="No Move",
    type="Normal",
    power=0,
    accuracy=0,
    pp=0,
    effect="No effect.",
)
ABSORB = BaseMoves(
    name="Absorb",
    type="Grass",
    power=20,
    accuracy=100,
    pp=25,
    effect="Absorbs 1/2 damage inflicted.",
)
ACID = BaseMoves(
    name="Acid",
    type="Poison",
    power=40,
    accuracy=100,
    pp=30,
    effect="May lower opponent's Special Defense by 1 stage.",
)
ACID_ARMOR = BaseMoves(
    name="Acid Armor",
    type="Poison",
    power=0,
    accuracy=0,
    pp=40,
    effect="Sharply raises user's Defense.",
)
AGILITY = BaseMoves(
    name="Agility",
    type="Psychic",
    power=0,
    accuracy=0,
    pp=30,
    effect="Sharply raises user's Speed.",
)
AMNESIA = BaseMoves(
    name="Amnesia",
    type="Psychic",
    power=0,
    accuracy=0,
    pp=20,
    effect="Sharply raises user's Special Defense.",
)
AURORA_BEAM = BaseMoves(
    name="Aurora Beam",
    type="Ice",
    power=65,
    accuracy=100,
    pp=20,
    effect="May lower opponent's Attack by 1 stage.",
)
BARRAGE = BaseMoves(
    name="Barrage",
    type="Normal",
    power=15,
    accuracy=85,
    pp=20,
    effect="Hits 2-5 times in one turn.",
)
BARRIER = BaseMoves(
    name="Barrier",
    type="Psychic",
    power=0,
    accuracy=0,
    pp=30,
    effect="Sharply raises user's Defense.",
)
BIDE = BaseMoves(
    name="Bide",
    type="Normal",
    power=0,
    accuracy=0,
    pp=10,
    effect="User takes damage for two turns then strikes back double.",
)
BIND = BaseMoves(
    name="Bind",
    type="Normal",
    power=15,
    accuracy=85,
    pp=20,
    effect="Traps opponent, damaging them for 4-5 turns.",
)
BITE = BaseMoves(
    name="Bite",
    type="Dark",
    power=60,
    accuracy=100,
    pp=25,
    effect="May cause flinching.",
)
BLIZZARD = BaseMoves(
    name="Blizzard",
    type="Ice",
    power=110,
    accuracy=70,
    pp=5,
    effect="May freeze opponent.",
)
BODY_SLAM = BaseMoves(
    name="Body Slam",
    type="Normal",
    power=85,
    accuracy=100,
    pp=15,
    effect="May paralyze opponent.",
)
BONE_CLUB = BaseMoves(
    name="Bone Club",
    type="Ground",
    power=65,
    accuracy=85,
    pp=20,
    effect="May cause flinching.",
)
BONEMERANG = BaseMoves(
    name="Bonemerang",
    type="Ground",
    power=50,
    accuracy=90,
    pp=10,
    effect="Hits twice in one turn.",
)
BUBBLE = BaseMoves(
    name="Bubble",
    type="Water",
    power=40,
    accuracy=100,
    pp=30,
    effect="May lower opponent's Speed by 1 stage.",
)
BUBBLE_BEAM = BaseMoves(
    name="Bubble Beam",
    type="Water",
    power=65,
    accuracy=100,
    pp=20,
    effect="May lower opponent's Speed by 1 stage.",
)
CLAMP = BaseMoves(
    name="Clamp",
    type="Water",
    power=35,
    accuracy=85,
    pp=10,
    effect="Traps opponent, damaging them for 4-5 turns.",
)
COMET_PUNCH = BaseMoves(
    name="Comet Punch",
    type="Normal",
    power=18,
    accuracy=85,
    pp=15,
    effect="Hits 2-5 times in one turn.",
)
CONFUSE_RAY = BaseMoves(
    name="Confuse Ray",
    type="Ghost",
    power=0,
    accuracy=100,
    pp=10,
    effect="Confuses opponent.",
)
CONFUSION = BaseMoves(
    name="Confusion",
    type="Psychic",
    power=50,
    accuracy=100,
    pp=25,
    effect="May confuse opponent.",
)
CONSTRICT = BaseMoves(
    name="Constrict",
    type="Normal",
    power=10,
    accuracy=100,
    pp=35,
    effect="May lower opponent's Speed by 1 stage.",
)
CONVERSION = BaseMoves(
    name="Conversion",
    type="Normal",
    power=0,
    accuracy=0,
    pp=30,
    effect="Changes user's type to opponent's.",
)
COUNTER = BaseMoves(
    name="Counter",
    type="Fighting",
    power=0,
    accuracy=100,
    pp=20,
    effect="When hit by a Physical Attack, user strikes back with 2x power.",
)
CRABHAMMER = BaseMoves(
    name="Crabhammer",
    type="Water",
    power=100,
    accuracy=90,
    pp=10,
    effect="High critical hit ratio.",
)
CUT = BaseMoves(
    name="Cut",
    type="Normal",
    power=50,
    accuracy=95,
    pp=30,
    effect="No added effect.",
)
DEFENSE_CURL = BaseMoves(
    name="Defense Curl",
    type="Normal",
    power=0,
    accuracy=0,
    pp=40,
    effect="Raises user's Defense.",
)
DIG = BaseMoves(
    name="Dig",
    type="Ground",
    power=80,
    accuracy=100,
    pp=10,
    effect="Digs underground on first turn, attacks on second. Can also escape from caves.",
)
DISABLE = BaseMoves(
    name="Disable",
    type="Normal",
    power=0,
    accuracy=100,
    pp=20,
    effect="Opponent can't use its last attack for a few turns.",
)
DIZZY_PUNCH = BaseMoves(
    name="Dizzy Punch",
    type="Normal",
    power=70,
    accuracy=100,
    pp=10,
    effect="May confuse opponent.",
)
DOUBLE_KICK = BaseMoves(
    name="Double Kick",
    type="Fighting",
    power=30,
    accuracy=100,
    pp=30,
    effect="Hits twice in one turn.",
)
DOUBLE_SLAP = BaseMoves(
    name="Double Slap",
    type="Normal",
    power=15,
    accuracy=85,
    pp=10,
    effect="Hits 2-5 times in one turn.",
)
DOUBLE_TEAM = BaseMoves(
    name="Double Team",
    type="Normal",
    power=0,
    accuracy=0,
    pp=15,
    effect="Raises user's evasiveness.",
)
DOUBLE_EDGE = BaseMoves(
    name="Double-Edge",
    type="Normal",
    power=120,
    accuracy=100,
    pp=15,
    effect="User receives recoil damage.",
)
DRAGON_RAGE = BaseMoves(
    name="Dragon Rage",
    type="Dragon",
    power=0,
    accuracy=100,
    pp=10,
    effect="Always inflicts 40 HP.",
)
DREAM_EATER = BaseMoves(
    name="Dream Eater",
    type="Psychic",
    power=100,
    accuracy=100,
    pp=15,
    effect="User recovers half the HP inflicted on opponent.",
)
DRILL_PECK = BaseMoves(
    name="Drill Peck",
    type="Flying",
    power=80,
    accuracy=100,
    pp=20,
    effect="No added effect.",
)
EARTHQUAKE = BaseMoves(
    name="Earthquake",
    type="Ground",
    power=100,
    accuracy=100,
    pp=10,
    effect="Power is doubled if opponent is underground from using Dig.",
)
EGG_BOMB = BaseMoves(
    name="Egg Bomb",
    type="Normal",
    power=100,
    accuracy=75,
    pp=10,
    effect="No added effect.",
)
EMBER = BaseMoves(
    name="Ember",
    type="Fire",
    power=40,
    accuracy=100,
    pp=25,
    effect="May burn opponent.",
)
EXPLOSION = BaseMoves(
    name="Explosion",
    type="Normal",
    power=250,
    accuracy=100,
    pp=5,
    effect="User faints.",
)
FIRE_BLAST = BaseMoves(
    name="Fire Blast",
    type="Fire",
    power=110,
    accuracy=85,
    pp=5,
    effect="May burn opponent.",
)
FIRE_PUNCH = BaseMoves(
    name="Fire Punch",
    type="Fire",
    power=75,
    accuracy=100,
    pp=15,
    effect="May burn opponent.",
)
FIRE_SPIN = BaseMoves(
    name="Fire Spin",
    type="Fire",
    power=35,
    accuracy=85,
    pp=15,
    effect="Traps opponent, damaging them for 4-5 turns.",
)
FISSURE = BaseMoves(
    name="Fissure",
    type="Ground",
    power=0,
    accuracy=0,
    pp=5,
    effect="One-Hit-KO, if it hits.",
)
FLAMETHROWER = BaseMoves(
    name="Flamethrower",
    type="Fire",
    power=90,
    accuracy=100,
    pp=15,
    effect="May burn opponent.",
)
FLASH = BaseMoves(
    name="Flash",
    type="Normal",
    power=0,
    accuracy=100,
    pp=20,
    effect="Lowers opponent's accuracy.",
)
FLY = BaseMoves(
    name="Fly",
    type="Flying",
    power=90,
    accuracy=95,
    pp=15,
    effect="Flies up on first turn, attacks on second turn.",
)
FOCUS_ENERGY = BaseMoves(
    name="Focus Energy",
    type="Normal",
    power=0,
    accuracy=0,
    pp=30,
    effect="Increases critical hit ratio.",
)
FURY_ATTACK = BaseMoves(
    name="Fury Attack",
    type="Normal",
    power=15,
    accuracy=85,
    pp=20,
    effect="Hits 2-5 times in one turn.",
)
FURY_SWIPES = BaseMoves(
    name="Fury Swipes",
    type="Normal",
    power=18,
    accuracy=80,
    pp=15,
    effect="Hits 2-5 times in one turn.",
)
GLARE = BaseMoves(
    name="Glare",
    type="Normal",
    power=0,
    accuracy=100,
    pp=30,
    effect="Paralyzes opponent.",
)
GROWL = BaseMoves(
    name="Growl",
    type="Normal",
    power=0,
    accuracy=100,
    pp=40,
    effect="Lowers opponent's Attack.",
)
GROWTH = BaseMoves(
    name="Growth",
    type="Normal",
    power=0,
    accuracy=0,
    pp=40,
    effect="Raises user's Attack and Special Attack.",
)
GUILLOTINE = BaseMoves(
    name="Guillotine",
    type="Normal",
    power=0,
    accuracy=0,
    pp=5,
    effect="One-Hit-KO, if it hits.",
)
GUST = BaseMoves(
    name="Gust",
    type="Flying",
    power=40,
    accuracy=100,
    pp=35,
    effect="No added effect.",
)
HARDEN = BaseMoves(
    name="Harden",
    type="Normal",
    power=0,
    accuracy=0,
    pp=30,
    effect="Raises user's Defense.",
)
HAZE = BaseMoves(
    name="Haze",
    type="Ice",
    power=0,
    accuracy=0,
    pp=30,
    effect="Resets all stat changes.",
)
HEADBUTT = BaseMoves(
    name="Headbutt",
    type="Normal",
    power=70,
    accuracy=100,
    pp=15,
    effect="May cause flinching.",
)
HIGH_JUMP_KICK = BaseMoves(
    name="High Jump Kick",
    type="Fighting",
    power=130,
    accuracy=90,
    pp=10,
    effect="If it misses, the user loses half their HP.",
)
HORN_ATTACK = BaseMoves(
    name="Horn Attack",
    type="Normal",
    power=65,
    accuracy=100,
    pp=25,
    effect="No added effect.",
)
HORN_DRILL = BaseMoves(
    name="Horn Drill",
    type="Normal",
    power=0,
    accuracy=0,
    pp=5,
    effect="One-Hit-KO, if it hits.",
)
HYDRO_PUMP = BaseMoves(
    name="Hydro Pump",
    type="Water",
    power=110,
    accuracy=80,
    pp=5,
    effect="No added effect.",
)
HYPER_BEAM = BaseMoves(
    name="Hyper Beam",
    type="Normal",
    power=150,
    accuracy=90,
    pp=5,
    effect="User must recharge next turn.",
)
HYPER_FANG = BaseMoves(
    name="Hyper Fang",
    type="Normal",
    power=80,
    accuracy=90,
    pp=15,
    effect="May cause flinching.",
)
HYPNOSIS = BaseMoves(
    name="Hypnosis",
    type="Psychic",
    power=0,
    accuracy=60,
    pp=20,
    effect="Puts opponent to sleep.",
)
ICE_BEAM = BaseMoves(
    name="Ice Beam",
    type="Ice",
    power=90,
    accuracy=100,
    pp=10,
    effect="May freeze opponent.",
)
ICE_PUNCH = BaseMoves(
    name="Ice Punch",
    type="Ice",
    power=75,
    accuracy=100,
    pp=15,
    effect="May freeze opponent.",
)
JUMP_KICK = BaseMoves(
    name="Jump Kick",
    type="Fighting",
    power=100,
    accuracy=95,
    pp=10,
    effect="If it misses, the user loses half their HP.",
)
KARATE_CHOP = BaseMoves(
    name="Karate Chop",
    type="Fighting",
    power=50,
    accuracy=100,
    pp=25,
    effect="High critical hit ratio.",
)
KINESIS = BaseMoves(
    name="Kinesis",
    type="Psychic",
    power=0,
    accuracy=80,
    pp=15,
    effect="Lowers opponent's accuracy.",
)
LEECH_LIFE = BaseMoves(
    name="Leech Life",
    type="Bug",
    power=80,
    accuracy=100,
    pp=10,
    effect="User recovers half the HP inflicted on opponent.",
)
LEECH_SEED = BaseMoves(
    name="Leech Seed",
    type="Grass",
    power=0,
    accuracy=90,
    pp=10,
    effect="User steals HP from opponent each turn.",
)
LEER = BaseMoves(
    name="Leer",
    type="Normal",
    power=0,
    accuracy=100,
    pp=30,
    effect="Lowers opponent's Defense.",
)
LICK = BaseMoves(
    name="Lick",
    type="Ghost",
    power=30,
    accuracy=100,
    pp=30,
    effect="May paralyze opponent.",
)
LIGHT_SCREEN = BaseMoves(
    name="Light Screen",
    type="Psychic",
    power=0,
    accuracy=0,
    pp=30,
    effect="Halves damage from Special attacks for 5 turns.",
)
LOVELY_KISS = BaseMoves(
    name="Lovely Kiss",
    type="Normal",
    power=0,
    accuracy=75,
    pp=10,
    effect="Puts opponent to sleep.",
)
LOW_KICK = BaseMoves(
    name="Low Kick",
    type="Fighting",
    power=0,
    accuracy=100,
    pp=20,
    effect="The heavier the opponent, the stronger the attack.",
)
MEDITATE = BaseMoves(
    name="Meditate",
    type="Psychic",
    power=0,
    accuracy=0,
    pp=40,
    effect="Raises user's Attack.",
)
MEGA_DRAIN = BaseMoves(
    name="Mega Drain",
    type="Grass",
    power=40,
    accuracy=100,
    pp=15,
    effect="User recovers half the HP inflicted on opponent.",
)
MEGA_KICK = BaseMoves(
    name="Mega Kick",
    type="Normal",
    power=120,
    accuracy=75,
    pp=5,
    effect="No added effect.",
)
MEGA_PUNCH = BaseMoves(
    name="Mega Punch",
    type="Normal",
    power=80,
    accuracy=85,
    pp=20,
    effect="No added effect.",
)
METRONOME = BaseMoves(
    name="Metronome",
    type="Normal",
    power=0,
    accuracy=0,
    pp=10,
    effect="User performs any move in the game at random.",
)
MIMIC = BaseMoves(
    name="Mimic",
    type="Normal",
    power=0,
    accuracy=0,
    pp=10,
    effect="Copies the opponent's last move.",
)
MINIMIZE = BaseMoves(
    name="Minimize",
    type="Normal",
    power=0,
    accuracy=0,
    pp=20,
    effect="Sharply raises user's evasiveness.",
)
MIRROR_MOVE = BaseMoves(
    name="Mirror Move",
    type="Flying",
    power=0,
    accuracy=0,
    pp=20,
    effect="User performs the opponent's last move.",
)
MIST = BaseMoves(
    name="Mist",
    type="Ice",
    power=0,
    accuracy=0,
    pp=30,
    effect="User's stats cannot be changed for a period of time.",
)
NIGHT_SHADE = BaseMoves(
    name="Night Shade",
    type="Ghost",
    power=0,
    accuracy=100,
    pp=15,
    effect="Inflicts damage equal to user's level.",
)
PAY_DAY = BaseMoves(
    name="Pay Day",
    type="Normal",
    power=40,
    accuracy=100,
    pp=20,
    effect="A small amount of money is gained after the battle resolves.",
)
PECK = BaseMoves(
    name="Peck",
    type="Flying",
    power=35,
    accuracy=100,
    pp=35,
    effect="No added effect.",
)
PETAL_DANCE = BaseMoves(
    name="Petal Dance",
    type="Grass",
    power=120,
    accuracy=100,
    pp=10,
    effect="User attacks for 2-3 turns but then becomes confused.",
)
PIN_MISSILE = BaseMoves(
    name="Pin Missile",
    type="Bug",
    power=25,
    accuracy=95,
    pp=20,
    effect="Hits 2-5 times in one turn.",
)
POISON_GAS = BaseMoves(
    name="Poison Gas",
    type="Poison",
    power=0,
    accuracy=90,
    pp=40,
    effect="Poisons opponent.",
)
POISON_POWDER = BaseMoves(
    name="Poison Powder",
    type="Poison",
    power=0,
    accuracy=75,
    pp=35,
    effect="Poisons opponent.",
)
POISON_STING = BaseMoves(
    name="Poison Sting",
    type="Poison",
    power=15,
    accuracy=100,
    pp=35,
    effect="May poison opponent.",
)
POUND = BaseMoves(
    name="Pound",
    type="Normal",
    power=40,
    accuracy=100,
    pp=35,
    effect="No added effect.",
)
PSYBEAM = BaseMoves(
    name="Psybeam",
    type="Psychic",
    power=65,
    accuracy=100,
    pp=20,
    effect="May confuse opponent.",
)
PSYCHIC = BaseMoves(
    name="Psychic",
    type="Psychic",
    power=90,
    accuracy=100,
    pp=10,
    effect="May lower opponent's Special Defense.",
)
PSYWAVE = BaseMoves(
    name="Psywave",
    type="Psychic",
    power=0,
    accuracy=80,
    pp=15,
    effect="Inflicts damage 50-150% of user's level.",
)
QUICK_ATTACK = BaseMoves(
    name="Quick Attack",
    type="Normal",
    power=40,
    accuracy=100,
    pp=30,
    effect="User attacks first.",
)
RAGE = BaseMoves(
    name="Rage",
    type="Normal",
    power=20,
    accuracy=100,
    pp=20,
    effect="Raises user's Attack when hit.",
)
RAZOR_LEAF = BaseMoves(
    name="Razor Leaf",
    type="Grass",
    power=55,
    accuracy=95,
    pp=25,
    effect="High critical hit ratio.",
)
RAZOR_WIND = BaseMoves(
    name="Razor Wind",
    type="Normal",
    power=80,
    accuracy=100,
    pp=10,
    effect="Charges on first turn, attacks on second. High critical hit ratio.",
)
RECOVER = BaseMoves(
    name="Recover",
    type="Normal",
    power=0,
    accuracy=0,
    pp=10,
    effect="User recovers half its max HP.",
)
REFLECT = BaseMoves(
    name="Reflect",
    type="Psychic",
    power=0,
    accuracy=0,
    pp=20,
    effect="Halves damage from Physical attacks for 5 turns.",
)
REST = BaseMoves(
    name="Rest",
    type="Psychic",
    power=0,
    accuracy=0,
    pp=10,
    effect="User sleeps for 2 turns, but user is fully healed.",
)
ROAR = BaseMoves(
    name="Roar",
    type="Normal",
    power=0,
    accuracy=0,
    pp=20,
    effect="In battles, the opponent switches. In the wild, the Pokémon runs.",
)
ROCK_SLIDE = BaseMoves(
    name="Rock Slide",
    type="Rock",
    power=75,
    accuracy=90,
    pp=10,
    effect="May cause flinching.",
)
ROCK_THROW = BaseMoves(
    name="Rock Throw",
    type="Rock",
    power=50,
    accuracy=90,
    pp=15,
    effect="No added effect.",
)
ROLLING_KICK = BaseMoves(
    name="Rolling Kick",
    type="Fighting",
    power=60,
    accuracy=85,
    pp=15,
    effect="May cause flinching.",
)
SAND_ATTACK = BaseMoves(
    name="Sand Attack",
    type="Ground",
    power=0,
    accuracy=100,
    pp=15,
    effect="Lowers opponent's accuracy.",
)
SCRATCH = BaseMoves(
    name="Scratch",
    type="Normal",
    power=40,
    accuracy=100,
    pp=35,
    effect="No added effect.",
)
SCREECH = BaseMoves(
    name="Screech",
    type="Normal",
    power=0,
    accuracy=85,
    pp=40,
    effect="Sharply lowers opponent's Defense.",
)
SEISMIC_TOSS = BaseMoves(
    name="Seismic Toss",
    type="Fighting",
    power=0,
    accuracy=100,
    pp=20,
    effect="Inflicts damage equal to user's level.",
)
SELF_DESTRUCT = BaseMoves(
    name="Self-Destruct",
    type="Normal",
    power=200,
    accuracy=100,
    pp=5,
    effect="User faints.",
)
SHARPEN = BaseMoves(
    name="Sharpen",
    type="Normal",
    power=0,
    accuracy=0,
    pp=30,
    effect="Raises user's Attack.",
)
SING = BaseMoves(
    name="Sing",
    type="Normal",
    power=0,
    accuracy=55,
    pp=15,
    effect="Puts opponent to sleep.",
)
SKULL_BASH = BaseMoves(
    name="Skull Bash",
    type="Normal",
    power=130,
    accuracy=100,
    pp=10,
    effect="Raises Defense on first turn, attacks on second.",
)
SKY_ATTACK = BaseMoves(
    name="Sky Attack",
    type="Flying",
    power=140,
    accuracy=90,
    pp=5,
    effect="Charges on first turn, attacks on second. May cause flinching.",
)
SLAM = BaseMoves(
    name="Slam",
    type="Normal",
    power=80,
    accuracy=75,
    pp=20,
    effect="No added effect.",
)
SLASH = BaseMoves(
    name="Slash",
    type="Normal",
    power=70,
    accuracy=100,
    pp=20,
    effect="High critical hit ratio.",
)
SLEEP_POWDER = BaseMoves(
    name="Sleep Powder",
    type="Grass",
    power=0,
    accuracy=75,
    pp=15,
    effect="Puts opponent to sleep.",
)
SLUDGE = BaseMoves(
    name="Sludge",
    type="Poison",
    power=65,
    accuracy=100,
    pp=20,
    effect="May poison opponent.",
)
SMOG = BaseMoves(
    name="Smog",
    type="Poison",
    power=30,
    accuracy=70,
    pp=20,
    effect="May poison opponent.",
)
SMOKESCREEN = BaseMoves(
    name="Smokescreen",
    type="Normal",
    power=0,
    accuracy=100,
    pp=20,
    effect="Lowers opponent's accuracy.",
)
SOFT_BOILED = BaseMoves(
    name="Soft-Boiled",
    type="Normal",
    power=0,
    accuracy=0,
    pp=10,
    effect="User recovers half its max HP.",
)
SOLAR_BEAM = BaseMoves(
    name="Solar Beam",
    type="Grass",
    power=120,
    accuracy=100,
    pp=10,
    effect="Charges on first turn, attacks on second.",
)
SONIC_BOOM = BaseMoves(
    name="Sonic Boom",
    type="Normal",
    power=0,
    accuracy=90,
    pp=20,
    effect="Always inflicts 20 HP.",
)
SPIKE_CANNON = BaseMoves(
    name="Spike Cannon",
    type="Normal",
    power=20,
    accuracy=100,
    pp=15,
    effect="Hits 2-5 times in one turn.",
)
SPLASH = BaseMoves(
    name="Splash",
    type="Normal",
    power=0,
    accuracy=0,
    pp=40,
    effect="Does nothing.",
)
SPORE = BaseMoves(
    name="Spore",
    type="Grass",
    power=0,
    accuracy=100,
    pp=15,
    effect="Puts opponent to sleep.",
)
STOMP = BaseMoves(
    name="Stomp",
    type="Normal",
    power=65,
    accuracy=100,
    pp=20,
    effect="May cause flinching.",
)
STRENGTH = BaseMoves(
    name="Strength",
    type="Normal",
    power=80,
    accuracy=100,
    pp=15,
    effect="No added effect.",
)
STRING_SHOT = BaseMoves(
    name="String Shot",
    type="Bug",
    power=0,
    accuracy=95,
    pp=40,
    effect="Sharply lowers opponent's Speed.",
)
STRUGGLE = BaseMoves(
    name="Struggle",
    type="Normal",
    power=50,
    accuracy=0,
    pp=1,
    effect="User loses 1/4 its max HP.",
)
STUN_SPORE = BaseMoves(
    name="Stun Spore",
    type="Grass",
    power=0,
    accuracy=75,
    pp=30,
    effect="Paralyzes opponent.",
)
SUBMISSION = BaseMoves(
    name="Submission",
    type="Fighting",
    power=80,
    accuracy=80,
    pp=25,
    effect="User receives recoil damage.",
)
SUBSTITUTE = BaseMoves(
    name="Substitute",
    type="Normal",
    power=0,
    accuracy=0,
    pp=10,
    effect="Uses 1/4 of the user's max HP to create a substitute that takes the opponent's attacks until the substitute breaks.",
)
SUPER_FANG = BaseMoves(
    name="Super Fang",
    type="Normal",
    power=0,
    accuracy=90,
    pp=10,
    effect="Always takes off half of the opponent's HP.",
)
SUPERSONIC = BaseMoves(
    name="Supersonic",
    type="Normal",
    power=0,
    accuracy=55,
    pp=20,
    effect="Confuses opponent.",
)
SURF = BaseMoves(
    name="Surf",
    type="Water",
    power=90,
    accuracy=100,
    pp=15,
    effect="Hits all adjacent Pokémon.",
)
SWIFT = BaseMoves(
    name="Swift",
    type="Normal",
    power=60,
    accuracy=0,
    pp=20,
    effect="Ignores Accuracy and Evasiveness.",
)
SWORDS_DANCE = BaseMoves(
    name="Swords Dance",
    type="Normal",
    power=0,
    accuracy=0,
    pp=20,
    effect="Raises user's Attack.",
)
TACKLE = BaseMoves(
    name="Tackle",
    type="Normal",
    power=50,
    accuracy=100,
    pp=35,
    effect="No added effect.",
)
TAIL_WHIP = BaseMoves(
    name="Tail Whip",
    type="Normal",
    power=0,
    accuracy=100,
    pp=30,
    effect="Lowers opponent's Defense.",
)
TAKE_DOWN = BaseMoves(
    name="Take Down",
    type="Normal",
    power=90,
    accuracy=85,
    pp=20,
    effect="User receives recoil damage.",
)
TELEPORT = BaseMoves(
    name="Teleport",
    type="Psychic",
    power=0,
    accuracy=0,
    pp=20,
    effect="Allows user to flee wild battles; also warps player to last PokéCenter.",
)
THRASH = BaseMoves(
    name="Thrash",
    type="Normal",
    power=120,
    accuracy=100,
    pp=10,
    effect="User attacks for 2-3 turns but then becomes confused.",
)
THUNDER = BaseMoves(
    name="Thunder",
    type="Electric",
    power=110,
    accuracy=70,
    pp=10,
    effect="May paralyze opponent.",
)
THUNDER_PUNCH = BaseMoves(
    name="ThunderPunch",
    type="Electric",
    power=75,
    accuracy=100,
    pp=15,
    effect="May paralyze opponent.",
)
THUNDER_SHOCK = BaseMoves(
    name="ThunderShock",
    type="Electric",
    power=40,
    accuracy=100,
    pp=30,
    effect="May paralyze opponent.",
)
THUNDER_WAVE = BaseMoves(
    name="Thunder Wave",
    type="Electric",
    power=0,
    accuracy=100,
    pp=20,
    effect="Paralyzes opponent.",
)
THUNDERBOLT = BaseMoves(
    name="Thunderbolt",
    type="Electric",
    power=90,
    accuracy=100,
    pp=15,
    effect="May paralyze opponent.",
)
TOXIC = BaseMoves(
    name="Toxic",
    type="Poison",
    power=0,
    accuracy=90,
    pp=10,
    effect="Badly poisons opponent.",
)
TRANSFORM = BaseMoves(
    name="Transform",
    type="Normal",
    power=0,
    accuracy=0,
    pp=10,
    effect="User takes on the form and attacks of the opponent.",
)
TRI_ATTACK = BaseMoves(
    name="Tri Attack",
    type="Normal",
    power=80,
    accuracy=100,
    pp=10,
    effect="May paralyze, burn or freeze opponent.",
)
TWINEEDLE = BaseMoves(
    name="Twineedle",
    type="Bug",
    power=25,
    accuracy=100,
    pp=20,
    effect="Hits twice in one turn. May poison opponent.",
)
VINE_WHIP = BaseMoves(
    name="Vine Whip",
    type="Grass",
    power=45,
    accuracy=100,
    pp=25,
    effect="No added effect.",
)
VICEGRIP = BaseMoves(
    name="ViceGrip",
    type="Normal",
    power=55,
    accuracy=100,
    pp=30,
    effect="No added effect.",
)
WATER_GUN = BaseMoves(
    name="Water Gun",
    type="Water",
    power=40,
    accuracy=100,
    pp=25,
    effect="No added effect.",
)
WATERFALL = BaseMoves(
    name="Waterfall",
    type="Water",
    power=80,
    accuracy=100,
    pp=15,
    effect="May cause flinching.",
)
WHIRLWIND = BaseMoves(
    name="Whirlwind",
    type="Normal",
    power=0,
    accuracy=0,
    pp=20,
    effect="In battles, the opponent switches. In the wild, the Pokémon runs.",
)
WING_ATTACK = BaseMoves(
    name="Wing Attack",
    type="Flying",
    power=60,
    accuracy=100,
    pp=35,
    effect="No added effect.",
)
WITHDRAW = BaseMoves(
    name="Withdraw",
    type="Water",
    power=0,
    accuracy=0,
    pp=40,
    effect="Raises user's Defense.",
)
WRAP = BaseMoves(
    name="Wrap",
    type="Normal",
    power=15,
    accuracy=90,
    pp=20,
    effect="Traps opponent, damaging them for 4-5 turns.",
)
