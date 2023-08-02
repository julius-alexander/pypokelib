from typing import NamedTuple

Color = NamedTuple('Color',
                   [
                       ('r', int),
                       ('g', int),
                       ('b', int)
                    ]
                )

color1 = Color(55, 155, 255)
color2 = Color(155, 55, 255)    
color3 = Color(55, 255, 155)
color4 = Color(155, 255, 55)

print(color1)
print(color2)
print(color3)
print(color4)

print(color1.r)
print(color1.g)
print(color1.b)

# * Example call for assignment:
# my_abra = Abra()
# defaults to level 1, no EVs, no IVs, no nature, no item, lvl. 1 moveset
#
# my_abra = Abra(level=5,
#               evs={'atk': 252, 'spe': 252, 'hp': 4},
#               ivs={'def': 30},
#               nature='adamant',
#               item='life orb',
#               moves=('psychic', 'fire punch', 'thunder punch', 'ice punch')
#           )
#
# This one assigns certain values to certain fields, and the rest are default
