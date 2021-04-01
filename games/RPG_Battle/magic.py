import random

class Spell:
    def __init__(self, name, cost, dmg, type):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = type

    def generate_damage(self):
        low = self.dmg - 15
        high = self.dmg + 15
        return random.randrange(low, high)

    #def get_spell_name(self, i):
    #    return self.magic[i]["name"]

    #def get_spell_mp_cost(self, i):
    #    return self.magic[i]["cost"]

#        magic_dmg = player.generate_spell_damage(magic_choice)
#        spell = player.get_spell_name(magic_choice)
#        cost = player.get_spell_mp_cost(magic_choice)

#magic = [{"name": "Fire", "cost": 10, "dmg": 100},
#         {"name": "Thunder", "cost": 12, "dmg": 124},
#         {"name": "Blizzard", "cost": 10, "dmg": 100}]

