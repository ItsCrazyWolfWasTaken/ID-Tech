import random

class Character:
    def __init__(self, name, strength, health, defense):
        self.name = name
        self.strength = strength
        self.health = health
        self.defense = defense

    def take_damage(self, damage):
        damage_taken = damage - self.defense
        self.health -= damage_taken
        return damage_taken

    def attack(self, target):
        damage = self.strength * 2
        damage_dealt = target.take_damage(damage)
        return damage_dealt

    def is_alive(self):
        return self.health > 0

class Rogue(Character):
    def attack(self, target):
        dexterity = 20
        critical_hit = random.randint(0, 100) < dexterity
        damage = self.strength * 2
        if critical_hit:
            damage *= 2
            print("*** Critical Hit ***")
        damage_dealt = target.take_damage(damage)
        return damage_dealt

player1 = Character("Cheetah", 10, 100, 2)
print(player1.name)
print(player1.strength)
print(player1.health)
print(player1.defense)

player2 = Rogue("Latte", 8, 100, 4)
print(player2.name)
print(player2.strength)
print(player2.health)
print(player2.defense)

print(player1.name + " vs." + player2.name)
print(str(player1.health) + " vs. " + str(player2.health))

while player1.is_alive() and player2.is_alive():
    print(player1.name + ": " + str(player1.health))
    print(player2.name + ": " + str(player2.health))

    damage = player1.attack(player2)
    print(player1.name + " hits " + player2.name + " for " + str(damage))

    damage = player2.attack(player1)
    print(player2.name + " hits " + player1.name + " for " + str(damage))

if player1.is_alive():
    print(player1.name + " wins!")
elif player2.is_alive():
    print(player2.name + " wins!")
else:
    print("It's a draw!")
