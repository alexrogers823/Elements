class Inventory:
    def __init__(self):
        self.slots = []

    def add(self, *args):
        self.slots.extend(args)

    def exchange_stone(self, old_stone, new_stone):
        #find method to exchange old stone with new one
        pass

    def __str__(self):
        return str(self.slots)

    def __len__(self):
        return len(self.slots)

    def __contains__(self, item):
        return item in self.slots

    def __iter__(self):
        yield from self.slots

    def __getitem__(self, index):
        return self.slots[index]


class Item:
    def __init__(self, name, description=""):
        self.name = name
        self.description = description

    def __str__(self):
        return "{}: {}".format(self.name, self.description)


class Password:
    def __init__(self):
        pass

    def __str__(self):
        return str(self)

    def __len__(self):
        return len(self)

    def separate(self):
        element = {
            "AQ": "Water",
            "TE": "Earth",
            "PY": "Fire",
            "AE": "Air"
        }

        return

class Cutscenes:
    def __init__(self):
        pass

    def storyline(self, hero, level):
        pass




# Obsolete class. Will delete later
class Battle:
    def __init__(self, life_points, magic_points=0, fusion_turns=0):
        self.life_points = life_points
        self.magic_points = magic_points
        self.fusion_turns = fusion_turns

    # for hero: MP replenish per turn
    @property
    def mp_replenish(self):
        self.magic_points += 5

    @property
    def fusion(self):
        return self.fusion_turns

    @property
    def attacked(self):
        return self.life_points

    @attacked.setter
    def attacked(self, damage):
        self.life_points -= damage

    # if hero attacks with something that uses MP
    @mp_replenish.setter
    def mp_replenish(self, magic_used):
        self.magic_points -= magic_used

    # if hero has fusion and uses it, this will set how many turns it can use
    @fusion.setter
    def fusion(self, used):
        self.fusion_turns -= used
