"""Tests Generation 1 Functionality"""
import unittest
from pypokelib import PokemonGen1 as Pokemon

class Test_Pokemon(unittest.TestCase):
    def test_pokemon_get_dex_num_by_str(self):
        """Test the initialization of the Pokemon class:\n
        Return the Pokedex number of the Pokemon given its species name"""
        self.assertEqual(Pokemon("Bulbasaur").get_dex_num(), 1)
        self.assertEqual(Pokemon("Charmander").get_dex_num(), 4)
        self.assertEqual(Pokemon("Squirtle").get_dex_num(), 7)
        self.assertEqual(Pokemon("Pikachu").get_dex_num(), 25)
        self.assertEqual(Pokemon("Eevee").get_dex_num(), 133)
        self.assertEqual(Pokemon("Mew").get_dex_num(), 151)

    def test_pokemon_get_dex_num_by_int(self):
        """Test the initialization of the Pokemon class:\n
        Return the Pokedex number of the Pokemon given its Pokedex number"""
        self.assertEqual(Pokemon(1).get_dex_num(), 1)
        self.assertEqual(Pokemon(4).get_dex_num(), 4)
        self.assertEqual(Pokemon(7).get_dex_num(), 7)
        self.assertEqual(Pokemon(25).get_dex_num(), 25)
        self.assertEqual(Pokemon(133).get_dex_num(), 133)
        self.assertEqual(Pokemon(151).get_dex_num(), 151)

    def test_pokemon_get_name(self):
        """Test the initialization of the Pokemon class:\n
        Return the species name of the Pokemon"""
        self.assertEqual(Pokemon("Bulbasaur").get_name(), "Bulbasaur")
        self.assertEqual(Pokemon("Charmander").get_name(), "Charmander")
        self.assertEqual(Pokemon("Squirtle").get_name(), "Squirtle")
        self.assertEqual(Pokemon("Pikachu").get_name(), "Pikachu")
        self.assertEqual(Pokemon("Eevee").get_name(), "Eevee")
        self.assertEqual(Pokemon("Mew").get_name(), "Mew")

    def test_pokemon_get_base_stats(self):
        """Test the initialization of the Pokemon class:\n
        Return the base stats of the Pokemon"""
        self.assertEqual(Pokemon("Bulbasaur").get_base_stats(), (318, 45, 49, 49, 65, 65, 45))
        self.assertEqual(Pokemon("Charmander").get_base_stats(), (309, 39, 52, 43, 60, 50, 65))
        self.assertEqual(Pokemon("Squirtle").get_base_stats(), (314, 44, 48, 65, 50, 64, 43))
        self.assertEqual(Pokemon("Pikachu").get_base_stats(), (320, 35, 55, 40, 50, 50, 90))
        self.assertEqual(Pokemon("Eevee").get_base_stats(), (325, 55, 55, 50, 45, 65, 55))
        self.assertEqual(Pokemon("Mew").get_base_stats(), (600, 100, 100, 100, 100, 100, 100))

    def test_pokemon_get_type(self):
        """Test the initialization of the Pokemon class:\n
        Return the type(s) of the Pokemon"""
        self.assertEqual(Pokemon("Bulbasaur").get_types(), ["Grass", "Poison"])
        self.assertEqual(Pokemon("Charmander").get_types(), ["Fire", ""])
        self.assertEqual(Pokemon("Squirtle").get_types(), ["Water", ""])
        self.assertEqual(Pokemon("Pikachu").get_types(), ["Electric", ""])
        self.assertEqual(Pokemon("Eevee").get_types(), ["Normal", ""])
        self.assertEqual(Pokemon("Mew").get_types(), ["Psychic", ""])

    def test_pokemon_reset_stats(self):
        """Test the initialization of the Pokemon class:\n
        Reset the current stats of the Pokemon to the base stats"""
        p = Pokemon("Bulbasaur")
        p.current_stats = (1, 2, 3, 4, 5, 6, 7)
        p.reset_stats()
        self.assertEqual(p.current_stats, (318, 45, 49, 49, 65, 65, 45))

    def test_pokemon_get_growth_rate(self):
        """Test the initialization of the Pokemon class:\n
        Return the growth rate of the Pokemon for leveling purposes"""
        self.assertEqual(Pokemon("Bulbasaur").get_growth_rate(), "Medium Slow")
        self.assertEqual(Pokemon("Charmander").get_growth_rate(), "Medium Slow")
        self.assertEqual(Pokemon("Squirtle").get_growth_rate(), "Medium Slow")
        self.assertEqual(Pokemon("Pikachu").get_growth_rate(), "Medium Fast")
        self.assertEqual(Pokemon("Eevee").get_growth_rate(), "Medium Fast")
        self.assertEqual(Pokemon("Mew").get_growth_rate(), "Medium Slow")




if __name__ == '__main__':
    unittest.main()
