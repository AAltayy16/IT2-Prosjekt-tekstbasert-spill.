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
        return self._hp > 0 # Returnerer True hvis hp er over 0


class Weapon:  # Lager en klasse for våpen
    def __init__(self, weapon_type, damage):  # Tar imot våpentype og skade
        self.weapon_type = weapon_type  # Lagrer navnet på våpenet
        self.damage = damage  # Lagrer hvor mye skade våpenet gjør  


class Player(Character):  # Player arver fra Character

    def __init__(self, name, weapon):  # Konstruktør for spilleren
        super().__init__(name, 100)  # Bruker Character sin konstruktør og gir 100 HP
        self.weapon = weapon  # Spilleren får et våpenobjekt
        self.ability_bonus = 0  # Spilleren starter uten skadebonus

    def attack(self, enemy):  # Metode som lar spilleren angripe en fiende
        damage = random.randint(self.weapon.damage - 3, self.weapon.damage + 3)  # Tilfeldig skade
        damage += self.ability_bonus  # Legger til eventuell evnebonus
        enemy.take_damage(damage)  # Trekker skade fra fiendens HP

        print(f"\nDu angriper {enemy.get_name()}!")  # Skriver ut hvem du angriper
        print(f"Du gjør {damage} skade.")  # Viser hvor mye skade du gjør

    def get_weapon(self):  # Henter spillerens våpentype
        return self.weapon.weapon_type  # Returnerer våpentypen


class Enemy(Character):  # Enemy arver fra Character

    def __init__(self, name, hp, damage):  # Fienden får navn, HP og skade
        super().__init__(name, hp)  # Bruker konstruktøren fra Character
        self.damage = damage  # Lagrer fiendens skadeverdi

    def attack(self, player, action):  # Metode som lar fienden angripe spilleren
        damage = random.randint(self.damage - 3, self.damage + 3)  # Tilfeldig skade

        if action == "block":  # Sjekker om spilleren blokkerer
            damage = damage // 2  # Halverer skaden
            print("Du blokkerer angrepet!")  # Gir beskjed om blokkering

        elif action == "parry":  # Sjekker om spilleren prøver å parere
            if random.random() < 0.4:  # 40 prosent sjanse for vellykket parering
                print("PERFECT PARRY!")  # Skriver ut at pareringen lyktes
                print("Du unngår all skade.")  # Viser at spilleren unngår skade
                return  # Avslutter metoden uten å gi skade
            else:  # Hvis pareringen mislykkes
                print("Pareringen mislyktes!")  # Gir beskjed om mislykket parering

        player.take_damage(damage)  # Trekker skade fra spilleren
        print(f"{self.get_name()} gjør {damage} skade!")  # Viser fiendens skade


Delt kode

class Game:  # Hovedklassen som styrer hele spillet

    def __init__(self):  # Konstruktør for Game
        self.enemies = [  # Liste som inneholder alle fiendene
            Enemy("Bandit", 40, 10),  # Første fiende: 40 HP og 10 skade
            Enemy("Thug", 65, 15),  # Andre fiende: 65 HP og 15 skade
            Enemy("Sharko", 100, 20),  # Tredje fiende: 100 HP og 20 skade
            Enemy("Dread Serpent", 150, 25)  # Fjerde fiende: 150 HP og 25 skade
        ]

    def create_player(self):  # Metode som lager spilleren
        name = input("Skriv inn navnet ditt: ")  # Ber om spillernavn

        print("\nVelg våpen:")  # Viser våpenmenyen
        print("1. Light")  # Viser Light
        print("2. Medium")  # Viser Medium
        print("3. Heavy")  # Viser Heavy

        weapons = {  # Dictionary som kobler valg til våpenobjekter
            "1": Weapon("Light", 12),  # Light gjør 12 grunnskade
            "2": Weapon("Medium", 17),  # Medium gjør 17 grunnskade
            "3": Weapon("Heavy", 23)  # Heavy gjør 23 grunnskade
        }

        while True:  # Gjentar til spilleren velger et gyldig våpen
            choice = input("Velg 1, 2 eller 3: ")  # Leser spillerens valg

            if choice in weapons:  # Sjekker om valget finnes i dictionary
                break  # Avslutter løkken hvis valget er gyldig

            print("Ugyldig valg. Prøv igjen.")  # Vises ved feil valg

        return Player(name, weapons[choice])  # Oppretter og returnerer spillerobjektet


    def battle(self, player, enemy):  # Metode som starter en kamp

        print(f"\nEn {enemy.get_name()} dukker opp!")  # Viser hvilken fiende du møter
        print(f"Fiendens HP: {enemy.get_hp()}")  # Viser fiendens liv

        while player.is_alive() and enemy.is_alive():  # Kampen fortsetter så lenge begge lever

            print("\n----------------------")  # Lager en skillelinje
            print(f"{player.get_name()} HP: {player.get_hp()}")  # Viser spillerens HP
            print(f"{enemy.get_name()} HP: {enemy.get_hp()}")  # Viser fiendens HP
            print("----------------------")  # Lager en skillelinje

            print("1. Angrip")  # Alternativ for angrep
            print("2. Blokker")  # Alternativ for blokkering
            print("3. Parer")  # Alternativ for parering

            action = input("Velg handling: ")  # Leser spillerens valg

            if action not in ["1", "2", "3"]:  # Sjekker om valget er gyldig
                print("Ugyldig valg!")  # Gir beskjed om feil valg
                continue  # Starter neste runde uten angrep

            if action == "1":  # Hvis spilleren velger å angripe
                player.attack(enemy)  # Spilleren angriper fienden
                action = "attack"  # Registrerer handlingen

            elif action == "2":  # Hvis spilleren velger blokkering
                action = "block"  # Registrerer blokkering

            else:  # Hvis spilleren velger parering
                action = "parry"  # Registrerer parering

            if enemy.is_alive():  # Sjekker om fienden fortsatt lever
                enemy.attack(player, action)  # Fienden angriper spilleren

        if player.is_alive():  # Sjekker om spilleren vant
            print(f"\nDu beseiret {enemy.get_name()}!")  # Skriver ut seier
            return True  # Sender True tilbake til Game

        else:  # Hvis spilleren ikke lever
            print("\nDu ble beseiret!")  # Skriver ut tap
            return False  # Sender False tilbake til Game


    def start(self):  # Metode som starter hele spillet

        print("======================")  # Lager overskrift
        print("      DEEP FIGHT")  # Skriver spillets navn
        print("======================")  # Lager overskrift

        player = self.create_player()  # Oppretter spilleren

        print(f"\nVelkommen, {player.get_name()}!")  # Ønsker spilleren velkommen
        print(f"Våpen: {player.get_weapon()}")  # Viser valgt våpen

        for floor, enemy in enumerate(self.enemies, start=1):  # Går gjennom fiendene i rekkefølge
            print(f"\n========== FLOOR {floor} ==========")  # Viser hvilket floor spilleren er på

            won = self.battle(player, enemy)  # Starter kampen mot fienden

            if not won:  # Sjekker om spilleren tapte
                print("\nGAME OVER!")  # Skriver Game Over
                print("Du må starte en ny runde.")  # Gir beskjed om ny runde
                return  # Avslutter spillet

            if floor == 2:  # Sjekker om spilleren har fullført Floor 2
                print("\nDu har fått en ny evne!")  # Informerer om ny evne
                print("Damage øker med 5.")  # Viser evnebonus
                player.ability_bonus += 5  # Øker spillerens skadebonus

        print("\n======================")  # Lager avslutning
        print("DU HAR BESEIRET ALLE!")  # Skriver ut seier
        print("VICTORIOUS!")  # Viser at spillet er vunnet
        print("======================")  # Lager avslutning


game = Game()  # Lager et Game-objekt
game.start()  # Starter spillet
