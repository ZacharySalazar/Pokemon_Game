import random
class Abilities():

    def __init__(self, name, type, power):
        self.name = name
        self.type = type
        self.power = power


class DamageAbility(Abilities):
    def __init__(self, name, type, power):
        super().__init__(name, type, power)

    def use(self, target):
        target.health -= self.power


class HealAbility(Abilities):
    def __init__(self, name, type, power):
        super().__init__(name, type, power)

    def use(self, target):
        target.health += self.power


class Buff(Abilities):
    """Buffs increase stats of pokemon *DOES NOT HAVE SUPER EFFECT ALL TYPES ARE NORMAL!"""
    def __init__(self, name, type, power):
        super().__init__(name, type, power)

    def use(self, target, stat_type):
        if stat_type == "defence":
            target.defence += self.power
        elif stat_type == "attack":
            target.attack += self.power


class Debuff(Abilities):
    """Debffus decrease stats of pokemon *CAN HAVE SUPER EFFECT AND INCLUDES VARIANT TYPES!"""
    def __init__(self, name, type, power, condition=None):
        super().__init__(name, type, power)
        self.condition = condition

    def use(self, target, stat):
        target.stat -= self.power


#ABILITIES AND TYPES
#Normal
Tackle = DamageAbility("Tackle", "normal", 5)
Headbutt = DamageAbility("Headbutt", "normal", 10)  #30% chance to flinch
Slash = DamageAbility("Slash", "normal", 10) #Always crits
Quick_Attack = DamageAbility("Quick Attack", "normal", 10)  #attacks first
Gust = DamageAbility("Gust", "flying", 15)
Fury_Attack = DamageAbility("Fury_Attack", "normal", 2)
Recover = HealAbility("Recover", "normal", 10)

#Leaf
Vine_Whip = DamageAbility("Vine Whip", "leaf", 15)
Razor_Leaf = DamageAbility("Vine Whip", "leaf", 15) #Greater chance to crit
Absorb = DamageAbility("Absorb", "leaf", 10)
SolarBeam = DamageAbility("SolarBeam", "leaf", 30)#Takes 2 turns to cast
Pinneedle = DamageAbility("Pinneedle", "leaf", 30)#Strikes twice

#Fire
Ember = DamageAbility("Ember", "fire", 15)
Flamethrower = DamageAbility("Flamethrower", "leaf", 25)
Fire_Punch = DamageAbility("Flamethrower", "leaf", 10) #Always burns target
Blaze = Buff("Blaze", "fire", 10)  # increases damage when below half health
Flash_Fire = DamageAbility("Flamethrower", "leaf", 10) #Chance to Burn AND Stun

#Water
Crab_Hammer = DamageAbility("Crab Hammer", "water", 15) #High Crit Chance
Bubble = DamageAbility("Bubble", "water", 15) #Lowers target accuracy
Bubble_Beam = DamageAbility("BubbleBeam", "water", 25) #Lowers target accuracy
Hydropump = DamageAbility("Hydropump", "water", 50) #(Only cast once, but does large damage)
Withdraw = Buff("Withdraw", "water", 5)  # increases defence

#Electric
Thundershock = DamageAbility("Thundershock", "water", 10) #lowest damage good accuracy
Thunderwave = DamageAbility("Thunderwave", "water", 0) #Stuns target 100%
Thunderbolt = DamageAbility("Thunderbolt", "water", 20) #medium damage medium accuracy
Thunder = DamageAbility("Thunder", "water", 30) #High Damage / Low Accuracy
Electric_Surge = Buff("Electric Surge", "electric", 30) #Chance to double damge or half it

#Flying
Peck = DamageAbility("Peck", "flying", 15)
Drill_Peck = DamageAbility("Drill Peck", "water", 15) #Random amount of multiple strikes
Mirror_Move = DamageAbility("Mirror Move", "water", 15) #Copies opponents attack back at them
Wing_Attack = DamageAbility("Wing_Attack", "water", 20)
Fly = DamageAbility("Fly", "water", 40) #Takes 2 turns


#Buff
Harden = Buff("Harden", "normal", 5) #decreases damage taken
Growth = Buff("Growth", "normal", 5) #increases extra damage done


#Debuffs
Leech_Seed = Debuff("Leech Seed", "leaf", 10, "drain") #siphons health to user
Sleep_Powder = Debuff("Sleep Powder", "normal", 0, "sleep") #puts to sleep
Poison_Powder = Debuff("Poison Powder", "normal", 0, "poisoned") #poisons target
Stun_Spore = Debuff("Poison Powder", "normal", 0, "paralyze") #paralyzes target

