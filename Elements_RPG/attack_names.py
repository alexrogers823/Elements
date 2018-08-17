class Attacks:
    def __init__(self, morality, element_type, boss=False, *args, **kwargs):
        self.morality = morality
        self.element_type = element_type
        self.boss = boss

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return "Morality: {}, Type: {}".format(self.morality, self.element_type)

    def names(self):
        if self.morality == "hero":
            # attacks go in this order: basic attack, weapon attack. later will add temp-based and fusion attacks
            attacks = {
                "Water": ("Rushing Waterfall", "Nautic Whiplash"), #frostbite for temp attack
                "Earth": ("Boulder Impact", "Ground Boomerang"),
                "Fire": ("Ring of Fire", "Flamethrower"),
                "Air": ("Wind Pressure", "Breathtaker")
            }
            return attacks[self.element_type]

        if self.morality == "enemy":
            # attacks in this order: low-level attack, high-level attack, weapon attack.
            # first tuple is normal. second tuple is boss (sub-bosses have same names as minions)
            attacks = {
                "Water": [
                            ("Aqua Attack", "Typhoon", "Strong Current"),
                            ("", "", "")
                        ],
                "Earth": [
                            ("Earthquake", "Meteor Shower", "Stonewall"),
                            ("", "", "")
                        ],
                "Fire": [
                            ("Fireball Blast", "Inferno", "Stream of Flames"),
                            ("Scorched Wave", "Hell on Earth", "Third-Degree Incision")
                        ],
                "Air": [
                            ("Air Rush", "Tornado", "Wind Slash"),
                            ("Suffication", "", "")
                        ]
            }

            if self.boss == True:
                return attacks[self.element_type][1]
            else:
                return attacks[self.element_type][0]
