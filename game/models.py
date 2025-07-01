import random
from dataclasses import dataclass, field

@dataclass
class Character:
    name: str
    hp: int
    attack_bonus: int = 0
    armor_class: int = 10
    damage_die: int = 6
    is_monster: bool = False
    writer: object | None = field(default=None, repr=False, compare=False)
    
    def is_alive(self) -> bool:
        return self.hp > 0

    def attack(self, other: 'Character') -> str:
        roll = random.randint(1, 20)
        total = roll + self.attack_bonus
        result = f"{self.name} rolls {roll} + {self.attack_bonus} = {total}. "
        if total >= other.armor_class:
            damage = random.randint(1, self.damage_die)
            other.hp -= damage
            result += f"Hit for {damage}! {other.name} has {other.hp} HP left."
        else:
            result += "Misses!"
        return result
