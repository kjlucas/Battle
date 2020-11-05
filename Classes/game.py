import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, hp, mp, atk, df, mag):
        self.maxHP = hp
        self.hp = hp
        self.maxMP = mp
        self.mp = mp
        self.atkh = atk + 10
        self.arkl = atk - 10
        self.df = df
        self.mag = mag
        self.actions = ["Attack", "Magic"]

    def generate_dmg(self):
        return random.randrange(self.arkl, self.atkh)

    def heal(self, dmg):
        self.hp += dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_num_spells(self):
        i = 1
        for spell in self.mag:
            i += 1
        return i

    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0

        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxHP

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxMP

    def _reduce_mp(self, cost):
        self.maxMP -= cost

    def lowest_cost(self):
        i = float("inf")
        for spell in self.mag:
            if spell.cost < i:
                i = spell.cost
        return i

    def choose_action(self):
        i = 1
        print("Actions")
        for item in self.actions:
            print(str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("Magic")
        for spell in self.mag:
            print(str(i) + ":", spell["name"], "(" + str(spell["cost"]) + "mp)")
            i += 1


