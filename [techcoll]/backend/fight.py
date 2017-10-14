def hp_count(race_name):
    if race_name == 'human':
        return 200
    elif race_name == 'orc':
        return 400
    elif race_name == 'elf':
        return = 150
    elif race_name == 'undead':
        return = 175
    else:
        return = 200

def hit_power_count(class_name):
    if class_name == 'warrior:
        return 30
    elif class_name == 'mage':
        return 35
    elif class_name == 'rogue':
        return = 25
    else:
        return = 30

class Race():

    def __init__(self, race_name):
        self.race_name = race_name
        self.hp = hp_count(self.race_name)

class PlayerClass():

    def __init__(self, class_name):
        self.class_name = class_name
        self.hit_power = hit_power_count(self.class_name)

class Fighter():

    def __init__(self, race, fclass):
        self.race = Race(race)
        self.fclass = PlayerClass(fclass)
