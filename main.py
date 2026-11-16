import random    # Gjør at vi kan bruke tilfeldige tall i spillet

class Character:    # Lager en hovedklasse for alle karakterer
    def __init__(self, name, hp):   # Konstruktør som kjøres når et objekt opprettes
        self._name = name   # Privat attributt som lagrer navnet
        self._hp = hp    # Privat attributt som lagrer karakterens liv
        self._max_hp = hp   # Lagrer maksimal HP



    def get_name(self): # Getter-metode som henter navnet
        return self._name   # Returnerer navnet

    def get_hp(self):  # Getter-metode som henter HP
        return self._hp # Returnerer HP

    def take_damage(self, damage):  # Metode som trekker fra liv
        self._hp = max(0, self._hp - damage)     # HP kan aldri bli mindre enn 0

    def is_alive(self):
        return self.__hp > 0 #returnerer True hvis hp er over 0


class Weapon
