class Batalie:
    def lupta(self, antrenor1, antrenor2):
        print(f"Începe lupta între {antrenor1.nume} și {antrenor2.nume}!")
        while antrenor1.are_pokemoni_vii() and antrenor2.are_pokemoni_vii():
            pokemon1 = antrenor1.alege_pokemon()
            pokemon2 = antrenor2.alege_pokemon()
            print(f"{antrenor1.nume} a ales pe {pokemon1.nume} și {antrenor2.nume} a ales pe {pokemon2.nume}.")

            while pokemon1.este_viu() and pokemon2.este_viu():
                pokemon1.ataca(pokemon2)
                print(f"{pokemon1.nume} a atacat pe {pokemon2.nume}! {pokemon2.nume} mai are {pokemon2.viata} viata.")
                if not pokemon2.este_viu():
                    print(f"{pokemon2.nume} a fost învins!")
                    break

                pokemon2.ataca(pokemon1)
                print(f"{pokemon2.nume} a atacat pe {pokemon1.nume}! {pokemon1.nume} mai are {pokemon1.viata} viata.")
                if not pokemon1.este_viu():
                    print(f"{pokemon1.nume} a fost învins!")
                    break

        if antrenor1.are_pokemoni_vii():
            print(f"{antrenor1.nume} a câștigat lupta!")
        else:
            print(f"{antrenor2.nume} a câștigat lupta!")