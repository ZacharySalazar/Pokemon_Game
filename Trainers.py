
class Trainer():


    def __init__(self, name):
        self.name = name
        self.pokemon_list = []
        self.current_pokemon = None

    def add_pokemon(self, pokemon):
        self.pokemon_list.append(pokemon)
        self.current_pokemon = pokemon


