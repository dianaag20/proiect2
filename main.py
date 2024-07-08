from Pokemon import Pokemon
from Antrenor import Antrenor
from Batalie import Batalie

from Pokemon import Pokemon
from Antrenor import Antrenor
from Batalie import Batalie

pokemoni_disponibili1 = [
    Pokemon("Ivysaur", "Pamant", 50, 10),
    Pokemon("Wartortle", "Apa", 60, 15),
    Pokemon("Charmander", "Foc", 55, 12)
]
pokemoni_disponibili2 = [
    Pokemon("Venusaur", "Pamant", 52, 9),
    Pokemon("Charizard", "Foc", 60, 11),
    Pokemon("Bulbasaur", "Apa", 50, 13)
]

def afiseaza_pokemoni_disponibili(pokemoni_disponibili, antrenor):
    print(f"Pokemoni disponibili pentru {antrenor.nume}:")
    for i, pokemon in enumerate(pokemoni_disponibili):
        print(f"{i + 1}. {pokemon}")

def alege_pokemoni_pentru_antrenor(antrenor, pokemoni_disponibili):
    afiseaza_pokemoni_disponibili(pokemoni_disponibili, antrenor)
    for i in range(3):
        numar = int(input(f"Alege numărul pentru Pokémon-ul {i + 1} al lui {antrenor.nume}: "))
        while numar < 1 or numar > len(pokemoni_disponibili):
            print("Număr invalid. Te rog să încerci din nou.")
            numar = int(input(f"Alege numărul pentru Pokémon-ul {i + 1} al lui {antrenor.nume}: "))
        antrenor.adauga_pokemon(pokemoni_disponibili[numar - 1])

antrenor1 = Antrenor("Antrenor1")
antrenor2 = Antrenor("Antrenor2")

# Alegerea Pokémonilor pentru fiecare antrenor
alege_pokemoni_pentru_antrenor(antrenor1, pokemoni_disponibili1)
alege_pokemoni_pentru_antrenor(antrenor2, pokemoni_disponibili2)

batalie = Batalie()
batalie.lupta(antrenor1, antrenor2)

print(f"Starea finală a lui {antrenor1.nume}: {antrenor1}")
print(f"Starea finală a lui {antrenor2.nume}: {antrenor2}")
