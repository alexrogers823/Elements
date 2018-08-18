from game_items import Inventory
from attack_names import Attacks

class Player:
    def __init__(self, name="John Doe", element_type="", life_points=0, has_weapon=False, weapon_attack="", *args, **kwargs):
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

    def attacked(self, damage):
        self.life_points -= damage
        # return self.life_points


class Hero(Player):
    def __init__(self, name, element_type, basic_attack, inventory=Inventory, attack_points=Attacks, magic_points=50, temp_stone=False, elemental_stone="", weapon_attack="", *args, **kwargs):
        super().__init__(name=name, element_type=element_type, life_points=100, has_weapon=False, weapon_attack=weapon_attack, *args, **kwargs)
        # self.life_points = 100
        self.magic_points = magic_points
        self.basic_attack = basic_attack
        self.inventory = inventory
        self.attack_points = attack_points
        self.temp_stone = temp_stone
        self.elemental_stone = elemental_stone

    @property
    def display_inventory(self):
        acquired_options = [self.temp_stone, self.elemental_stone]
        options = self.inventory()
        options.add(self.basic_attack)
        if self.has_weapon:
            options.add(self.weapon_attack)
        for item in acquired_options:
            if item:
                options.add(item)

        return options

    @property
    def show_attack_damage(self):
        return self.attack_points("hero", self.element_type).damage

    @property
    def stats(self):
        # super().stats(self)
        return '{}: {} Type, {} LP, {} MP'.format(self.name, self.element_type.title(), self.life_points, self.magic_points)

    @property
    def mp_replenish(self):
        self.magic_points += 5

    def attacked(self, enemy_damage):
        return self.attacked(enemy_damage)

    @mp_replenish.setter
    def mp_replenish(self, magic_used):
        self.magic_points -= magic_used


# enemy class inherits from player class, but we will call directly with specific enemies using MRO
class Enemy(Player):
    def __init__(self, name, element_type, life_points, low_attack, high_attack, weapon_attack="", *args, **kwargs):
        super().__init__(name, element_type=element_type, life_points=life_points, has_weapon=False, weapon_attack=weapon_attack, *args, **kwargs)
        self.low_attack = low_attack
        self.high_attack = high_attack

    @property
    def stats(self):
        return '{}: {} Type, {} LP'.format(self.name, self.element_type.title(), self.life_points)

    def attacked(self, hero_damage):
        return self.attacked(hero_damage)
