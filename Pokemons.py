from Abilities import *
from Images import *
"""
Creates pokemon
"""
class Pokemon():
    condition = None

    def __init__(self, name, health, type, ab1, ab2, ab3, ab4, img=None):
        self.name = name
        self.max_health = health
        self.current_health = health
        self.type = type
        self.img = img

        self.ab1 = ab1
        self.ab2 = ab2
        self.ab3 = ab3
        self.ab4 = ab4
        self.ability_list = [ab1, ab2, ab3, ab4]
        self.lvl = 35


    def use_ability(self, ability_num_slot, target):
        def calculate_outcome(self):
            pass

        def show_pokemon_ability_used(self):
            print(self.name + " used " + ability.name + " on " + target.name)

        ability = self.ability_list[ability_num_slot - 1]
        ability.use(target)

        #Update console
        show_pokemon_ability_used(self)
        target.report_health()


    def show_abilities(self):
        print("{} {}".format(self.ab1.name, self.ab2.name))
        print("{} {}".format(self.ab3.name, self.ab4.name))

    def report_health(self):
        print("{} has {} Health remaining".format(self.name, self.health))


"""Pokemon List
normal (good against nothing, but vulnerable either)
leaf > water
water > fire and rock
fire > leaf
electric > water
rock > electric
flying > leaf

*Note Evolutions have more extra damage and Hp
normal: Rattatata, Raticate, SandShrew, SandSlash, Snorlax 
Leaf: Bulbasaur, "Oddish", "Vileplume", Exeggcute, Exeggutor	
Fire: "Charmander", "Growlithe, Arcanine, Ponita, Rapiddash"
Water: "Slowpoke, Slowbro, Shelder, Cloyster, Staryu, Starmite"
Electric: "Pikachu", "Raichu", "Voltorb", "Electrode", "Magmite", "Magneton"
Rock: "Geodude, Graveler, Onyx, Rhyhorn, Rhydon"
FLying: Pigey, Pigeotto, Zubat, Golbat, Spearow, Fearow
"""
#Pokemon
#Normal
Rattatata = Pokemon("Rattatata", 100, "normal", ab1=Tackle, ab2=Quick_Attack, ab3=Gust, ab4=Recover)
Raticate = Pokemon("Raticate", 100, "normal", ab1=Tackle, ab2=Quick_Attack, ab3=Gust, ab4=Recover)

#Rock
Geodude = Pokemon("Geodude", 100, "rock", ab1=Tackle, ab2=Quick_Attack, ab3=Gust, ab4=Recover, img=geodude_back)
Sandshrew = Pokemon("Sandshrew", 100, "rock", ab1=Tackle, ab2=Quick_Attack, ab3=Gust, ab4=Recover, img=sandshrew_facing)

#Flying
Pigey = Pokemon("Pigey", 100, "normal", ab1=Tackle, ab2=Quick_Attack, ab3=Gust, ab4=Recover)
Pigeotto = Pokemon("Pigeotto", 100, "normal", ab1=Tackle, ab2=Quick_Attack, ab3=Gust, ab4=Recover)

#print(Pigey.use_ability(1, Pigey2))