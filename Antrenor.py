class Antrenor:
    def __init__(self, nume):
        self.nume = nume
        self.pokemoni = []

    def adauga_pokemon(self, pokemon):
        self.pokemoni.append(pokemon)

    def alege_pokemon(self):
        for pokemon in self.pokemoni:
            if pokemon.este_viu():
                return pokemon
        return None

    def are_pokemoni_vii(self):
        return any(pokemon.este_viu() for pokemon in self.pokemoni)

    def __str__(self):
        return f"{self.nume} cu Pokemonii: {[str(pokemon) for pokemon in self.pokemoni]}"