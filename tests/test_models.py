import unittest
from game.models import Character

class TestCharacter(unittest.TestCase):
    def test_attack_hits_or_misses(self):
        attacker = Character(name='Hero', hp=10, attack_bonus=20, damage_die=1)
        defender = Character(name='Goblin', hp=5, armor_class=5)
        result = attacker.attack(defender)
        self.assertIn('Hit', result)
        self.assertLess(defender.hp, 5)

if __name__ == '__main__':
    unittest.main()
