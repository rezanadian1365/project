from enum import Enum


class Actions(Enum):
    pass


class Character:
    BUFF = 1
    NORMAL_ATTACK = 2
    SPECIAL_ATTACK = 3

    def __init__(self, hp, power):

        self.hp = hp
        self.power = power

    def recive_damage(self):
        pass


class Wariorr(Character):
    def iron_skin(self):
        pass

    def blade_storm(self):
        pass


class Mage(Character):
    def arcane_shield(self):
        pass

    def fireball(self):
        pass


class Assissin(Character):
    def assassin_instinct(self):
        pass

    def laserat(self):
        pass


class Battle:
    def __init__(self):
        pass

    def play_turn(self):
        pass
