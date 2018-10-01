class Gameplay:
    def __init__(self):
        self.difficulty = "normal"
        self.mode = "scarce"
        self.lp_replenish = 20
        self.multiplier = 1.3
        self.enemy_multiplier = 1
        self.level = 0
        self.tutorial = False

    def set_level(self, num):
        self.level = num

    @property
    def set_difficulty(self):
        return self.difficulty, self.multiplier, self.enemy_multiplier

    @property
    def set_mode(self):
        return self.mode

    @property
    def show_tutorials(self):
        self.tutorial = True
        return self.tutorial

    @property
    def level_up(self):
        self.level += 1
        return self.level

    @property
    def call_enemies(self):
        enemy_count = {
            "1": 5,
            "2": 8,
            "3": 7,
            "4": 10,
            "5": 9,
            "6": 14,
            "7": 16,
            "8": 15,
            "9": 18,
            "10": 20
        }

        return enemy_count[str(self.level)]

    @set_difficulty.setter
    def set_difficulty(self, value):
        valid_diffs = {
            "easy": ("easy", 1.1, 0.7),
            "normal": ("normal", 1.3, 1),
            "hard": ("hard", 1.8, 1.5)
        }
        if value.lower() in valid_diffs:
            self.difficulty, self.multiplier, self.enemy_multiplier = valid_diffs[value.lower()]
        else:
            raise ValueError("pick either easy, normal, or hard")

    @set_mode.setter
    def set_mode(self, value):
        valid_modes = {
            "generous": 100,
            "scarce": 20,
            "survival": 0
        }
        if value.lower() in valid_modes:
            self.mode = value.lower()
            self.lp_replenish = valid_modes[value.lower()]
        else:
            raise ValueError("pick either generous, scarce, or survival")
