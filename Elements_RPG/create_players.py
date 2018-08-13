class Player:
    def __init__(self, name="John Doe", element_type="", life_points=0, has_weapon=False, weapon_attack="", **kwargs):
        self.name = name
        if not element_type:
            raise ValueError("{} needs an element type".format(self.name))
        self.element_type = element_type
        self.life_points = life_points
        self.has_weapon = has_weapon
        self.weapon_attack = weapon_attack

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return self.name

    def attack(self):
        pass
        # come back to this one lol

class Hero(Player):
    def __init__(self, name, element_type, life_points, has_weapon, weapon_attack, basic_attack, magic_points=50, temp_stone=False, elemental_stone="", **kwargs):
        super().__init__(name, element_type, life_points, has_weapon, weapon_attack, **kwargs)
        self.life_points = 100
        self.magic_points = magic_points
        self.basic_attack = basic_attack
        self.temp_stone = temp_stone
        self.elemental_stone = elemental_stone


# enemy class inherits from player class, but we will call directly with specific enemies using MRO
class Enemy(Player):
    def __init__(self, name, element_type, life_points, has_weapon, weapon_attack, low_attack, high_attack, **kwargs):
        super().__init__(name, element_type, life_points, has_weapon, weapon_attack, **kwargs)
        self.low_attack = low_attack
        self.high_attack = high_attack
