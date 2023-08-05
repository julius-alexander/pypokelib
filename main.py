from pypokelib import PokemonGen1

my_party = []

p1 = PokemonGen1("Bulbasaur")
p01 = PokemonGen1(1)
p2 = PokemonGen1("Charmander")
p3 = PokemonGen1("Squirtle")
p4 = PokemonGen1("Pikachu")
p5 = PokemonGen1("Eevee")
p6 = PokemonGen1("Mew")

my_party.append(p1)
my_party.append(p2)
my_party.append(p3)
my_party.append(p4)
my_party.append(p5)
my_party.append(p6)

for pokemon in my_party:
    print(f"{pokemon}")
