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