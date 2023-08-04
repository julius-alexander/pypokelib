from pypokelib.generation1.data.pokemon.basestats.poke_base_class import Pokemon
import time

my_party = []

p1 = Pokemon("Bulbasaur")
p2 = Pokemon("Charmander")
p3 = Pokemon("Squirtle")
p4 = Pokemon("Pikachu")
p5 = Pokemon("Eevee")
p6 = Pokemon("Mew")

my_party.append(p1)
my_party.append(p2)
my_party.append(p3)
my_party.append(p4)
my_party.append(p5)
my_party.append(p6)

for pokemon in my_party:
    print(pokemon)
    