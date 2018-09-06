from game_items import Inventory
from game_items import Item
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

    @property
    def attacked(self):
        return self.life_points

    @attacked.setter
    def attacked(self, damage):
        self.life_points -= damage
        # return self.life_points


class Hero(Player):
    def __init__(self, name, element_type, basic_attack, inventory=Inventory, item_name=Item, attack_points=Attacks, magic_points=50, temp_stone=False, elemental_stone="", weapon_attack="", xp=0, *args, **kwargs):
        super().__init__(name=name, element_type=element_type, life_points=100, has_weapon=False, weapon_attack=weapon_attack, *args, **kwargs)
        # self.life_points = 100
        self.magic_points = magic_points
        self.basic_attack = basic_attack
        self.inventory = inventory
        self.item_name = item_name
        self.attack_points = attack_points
        self.temp_stone = temp_stone
        self.elemental_stone = elemental_stone
        self.xp = xp
        self.base_normal_damage = 10
        self.base_weapon_damage = 15
        self.base_weapon_mp = 15
        self.coins = 0

    @property
    def display_inventory(self):
        acquired_options = [self.temp_stone, self.elemental_stone]
        options = self.inventory()
        options.add(self.basic_attack)
        if self.has_weapon:
            options.add(self.weapon_attack)
        else:
            options.add("(Locked. Buy weapon first)")
        for item in acquired_options:
            if item:
                options.add(item)

        return options

    @property
    def show_attack_damage(self):
        damage = ((self.base_normal_damage, 0), (self.base_weapon_damage, self.base_weapon_mp))
        return damage

    @property
    def choose_attack_damage(self):
        return self.show_attack_damage

    @property
    def stats(self):
        # super().stats(self)
        return '{}: {} Type, {} LP, {} MP'.format(self.name, self.element_type.title(), self.life_points, self.magic_points)

    @property
    def shop_stats(self):
        return '{}: {} XP, {} Coins'.format(self.name, self.xp, self.coins)

    @property
    def display_shop_options(self):
        shop_list = self.inventory()
        stones = ['water', 'earth', 'fire', 'air']
        weapon = self.item_name('Weapon of Great {}'.format(self.element_type), 'Your weapon for greater attacks. Can upgrade')
        if self.has_weapon == False:
            shop_list.add([weapon.name.title(), 100, weapon.description])
        else:
            shop_list.add(['Lvl {} {}'.format(2, weapon.name.title()), 250, weapon.description])
        if self.temp_stone == False:
            shop_list.add(['Temperature Stone', 500, 'This stone lets you do temp-altered attacks for greater damage'])
        try:
            stones.pop(stones.index(self.elemental_stone))
        except ValueError:
            pass
        # if self.has_weapon:
        for element in stones:
            if self.element_type.lower() == element:
                message = 'Use the {0} stone to reduce damage of {0}-based attacks'.format(element)
            else:
                message = 'Use the {0} stone with {1} to do a fusion-based attack.\n\tAlso reduces damage of {0}-based attacks'.format(element, self.weapon_attack)
            shop_list.add(['{} Stone'.format(element.title()), 1000, message])

        return shop_list

    @property
    def mp_replenish(self):
        if self.magic_points >= 50:
            return self.magic_points
        else:
            self.magic_points += 5

    @property
    def gain_coins_and_xp(self):
        return self.coins, self.xp


    @property
    def acquire_items(self):
        self.has_weapon = has_weapon
        self.temp_stone = temp_stone
        self.elemental_stone = elemental_stone
        self.coins = coins

    # def attacked(self):
    #     self.attacked(enemy_damage)

    @mp_replenish.setter
    def mp_replenish(self, magic_used):
        self.magic_points -= magic_used

    @choose_attack_damage.setter
    def choose_attack_damage(self, attack):
        self.show_attack_damage = attack


    @gain_coins_and_xp.setter
    def gain_coins_and_xp(self, enemy):
        if enemy == 'minion':
            self.coins += 5
            self.xp += 5
        elif enemy == 'sub-boss':
            self.coins += 30
            self.xp += 10
        elif enemy == 'boss':
            self.coins += 75
            self.xp += 50
        elif enemy == 'flawless':
            self.xp += 100
        else:
            return self.coins, self.xp


    @acquire_items.setter
    def acquire_items(self, bought):
        if bought == "weapon":
            self.has_weapon = True
            self.coins -= 100
        if bought == "temp stone":
            self.temp_stone = True
        if bought.startswith("element"):
            self.elemental_stone = bought.split()[1]


# enemy class inherits from player class, but we will call directly with specific enemies using MRO
class Enemy(Player):
    def __init__(self, name, element_type, life_points, low_attack, high_attack, weapon_attack="", boss=False, sub_boss=False, *args, **kwargs):
        super().__init__(name, element_type=element_type, life_points=life_points, has_weapon=False, weapon_attack=weapon_attack, *args, **kwargs)
        self.low_attack = low_attack
        self.high_attack = high_attack
        self.base_low_damage = 10
        self.base_high_damage = 15
        self.base_weapon_damage = 13
        self.boss = boss
        self.sub_boss = sub_boss

    @property
    def stats(self):
        return '{}: {} Type, {} LP'.format(self.name, self.element_type.title(), self.life_points)

    @property
    def change_base_damage(self):
        damage = [(12, 18, 16), (15, 25, 20)]
        if self.sub_boss:
            self.base_low_damage, self.base_high_damage, self.base_weapon_damage = damage[0]
        elif self.boss:
            self.base_low_damage, self.base_high_damage, self.base_weapon_damage = damage[1]
        else:
            pass



    # def attacked(self, hero_damage):
    #     return self.attacked(hero_damage)
