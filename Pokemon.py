class Pokemon:
    def __init__(self, nume, tip, viata, putere_atac):
        if tip not in ['Foc', 'Apa', 'Pamant']:
            raise ValueError("Tipul trebuie să fie unul dintre: 'Foc', 'Apa', 'Pamant'")
        self.nume = nume
        self.tip = tip
        self.viata = viata
        self.putere_atac = putere_atac

    def ataca(self, alt_pokemon):
        alt_pokemon.viata -= self.putere_atac

    def este_viu(self):
        return self.viata > 0

    def __str__(self):
        return f"{self.nume} (Tip: {self.tip}, Viata: {self.viata}, Putere atac: {self.putere_atac})"