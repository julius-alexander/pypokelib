import unittest
from pypokelib import PokemonGen2 as Pokemon

class Test_Pokemon(unittest.TestCase):
    def test_pokemon_get_dex_num_by_str(self):
        """Test the initialization of the Pokemon class:\n
        Return the Pokedex number of the Pokemon given its species name"""
        self.assertEqual(Pokemon("Chikorita").get_dex_num(), 152)
        self.assertEqual(Pokemon("Cyndaquil").get_dex_num(), 155)
        self.assertEqual(Pokemon("Totodile").get_dex_num(), 158)
        self.assertEqual(Pokemon("Pichu").get_dex_num(), 172)
        self.assertEqual(Pokemon("Espeon").get_dex_num(), 196)
        self.assertEqual(Pokemon("Celebi").get_dex_num(), 251)

    def test_pokemon_get_dex_num_by_int(self):
        """Test the initialization of the Pokemon class:\n
        Return the Pokedex number of the Pokemon given its Pokedex number"""
        self.assertEqual(Pokemon(152).get_dex_num(), 152)
        self.assertEqual(Pokemon(155).get_dex_num(), 155)
        self.assertEqual(Pokemon(158).get_dex_num(), 158)
        self.assertEqual(Pokemon(172).get_dex_num(), 172)
        self.assertEqual(Pokemon(196).get_dex_num(), 196)
        self.assertEqual(Pokemon(251).get_dex_num(), 251)