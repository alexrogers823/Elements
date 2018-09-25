class Attacks:
    def __init__(self, morality, element_type, boss=False, *args, **kwargs):
        self.morality = morality
        self.element_type = element_type
        self.boss = boss

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return "Morality: {}, Type: {}".format(self.morality, self.element_type)

    # obsolete function
    def damage(self, value=0):
        # for hero: basic and mp basic (first); weapon and mp multiplier (second).
        # for enemy: low, high, weapon
        base_damage = {
            "hero": [(10, 15), (15, 2)],
            "enemy": [(10, 15, 13)]
        }

        return base_damage[self.morality][value]

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
                            ("Aquatic Outburst", "Tsunami", "Hydroplanar Eruption")
                        ],
                "Earth": [
                            ("Earthquake", "Meteor Shower", "Stonewall"),
                            ("Crying Terra", "Rock Shatter", "Geological Crush")
                        ],
                "Fire": [
                            ("Fireball Blast", "Inferno", "Stream of Flames"),
                            ("Scorched Wave", "Hell on Earth", "Third-Degree Incision")
                        ],
                "Air": [
                            ("Air Rush", "Tornado", "Wind Slash"),
                            ("Suffication", "Flight of Death", "Ozone Strike")
                        ],
                "Lightning": [
                            ("Static Shock", "Jolt of Electricity", "Bolt Strike"),
                            ("1000 Watts", "2000 Watts", "Surge Line")
                ]
            }

            if self.boss == True:
                return attacks[self.element_type][1]
            else:
                return attacks[self.element_type][0]
