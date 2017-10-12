class Fighter():

    def __init__(self, race, hp, hit_base):
        self.race = race
        self.hp = hp
        if self.race == "Orc":
            self.hit_base = hit_base * 3
        elif self.race == "Human":
            self.hit_base = hit_base * 1.5

    def smash(self):
        return self.hit_base

    def get_hit(self, hit):
        self.hit = hit
        if self.hp > 0:
            self.hp -= self.hit
            return self.hp
        else:
            print("{} is already DEAD! Stop beating corpse, maniac!".format(self.race))

orc = Fighter("Orc", 400, 20)
human = Fighter("Human", 250, 10)

print("BEHOLD! THE WAR IS NEAR!")
print("There are two fighters tries kill each other! LOOK!\n")
print("{} is attacking! Get ready!".format(orc.race))
print("{} get hit!".format(human.race))

print("\nDEBUG SEQUENCE BELOW:")
human.get_hit(orc.smash())
print(human.hp)
human.get_hit(orc.smash())
print(human.hp)
human.get_hit(orc.smash())
print(human.hp)
human.get_hit(orc.smash())
print(human.hp)
human.get_hit(orc.smash())
print(human.hp)
