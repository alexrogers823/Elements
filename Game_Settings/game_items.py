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

    def storyline(self, hero, level, mid=""):
        story = {
            "1": [], # Move the 'long ago...' part here
            "2": [],
            "3": ['''"This seems odd", {} said. The approaching area felt so familiar...''',
                '''The symbols on the walls were identical to their own''',
                '''Suddenly {} realized. "Oh no!" the warrior said. "My own people have been corrupted!"'''],
            "4": ['''{}'s heart became filled with sadness after fighting their own people''',
                '''"I will end this evil presence!" the hero declared. "Then all will return to normal"''',
                '''But as {} was pondering, a shadow appeared...''',
                '''A force that had the exact opposite sign.''',
                '''{} now knew that he would be going up against his weakness. And it wouldn't be easy...'''],
            "5": ['''Now {} realized that they were getting closer to the great force that corrupted the world.''',
                '''Having defeated each of the elements, their confidence seemed to get higher.''',
                '''As {} kept walking, they noticed symbols that they had already came across.''',
                '''"Is this a place I already visited?", they wondered. "Or...a stronger tribe of an element before?"''',
                '''Ready for anything, {} carried on...'''],
            "6": [],
            "7": [],
            "8": ['''"Man, this feels weird" {} stated. They were getting closer to a force they had never encounted.''',
                '''It was clear that they were getting closer to the source of it all.''',
                '''As the horizon became more clear, {} saw a large tower. It looked as if sparks randomly surrounded it.''',
                '''"I don't know what element habits this place" the warrior said, "but it can't be good..."'''],
            "9": ['''A voice called out to {}...''',
                '''"MERE MORTAL" it said, "YOU WILL SUBMIT TO THE ULTIMATE POWER!"''',
                '''{} was ready to fight back. "Who are you?" they replied. "And why are you here?"'''
                '''"I AM ELEMATRIX" shouted the voice, "AND YOU WILL LEARN TO OBEY ME!"''',
                '''"I will never let you rule!" {} shouted. "I will save my friends and restore humanity!"''',
                '''"IF YOU WILL NOT COME WILLINGLY..."''',
                '''"THEN I SHALL SEND AN ARMY OF YOUR WEAKNESS AT YOU. HAHAHA..."'''],
            "10": [],
        }

        key = str(level) if mid == "" else str(level)+mid

        return story[key]




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
