import random
import json

# print("llll")
# print("glock")



zaci = {
    "Adam": [],
    "Klara": [],
    "Martin": [],
    "Eva": [],
    "Lukas": [],
    "Petra": [],
    "Jakub": [],
    "Hana": [],
    "Michal": [],
    "Veronika": []
}


# nahodny_zak = random.choice(list(zaci))
def pridej_znamku(zak):
    nahodne_cislo = random.randint(1, 5)
    print(f"Známka je: {nahodne_cislo}")
    zaci[zak].append(nahodne_cislo)

def zak():
    kdo = input(f"Komu?: ")
    if kdo in zaci:
        pridej_znamku(kdo)
        with open("zaci.json", "w", encoding="utf-8") as f:
            json.dump(zaci, f, ensure_ascii=False, indent=4)
        print(f"Známka pro {kdo} je: {zaci[kdo]}")
    else:
        print("Tento žák není v seznamu.")
        pridat = input("Přidat?: ")
        if pridat == "ano":
            zaci[kdo] = 0
            with open("zaci.json", "w", encoding="utf-8") as f:
                json.dump(zaci, f, ensure_ascii=False, indent=4)
            print(f"Žák {kdo} byl přidán do seznamu.")
            print(f"Známka pro {kdo} je: {zaci[kdo]}")
        elif pridat == "ne":
            print("Žák nebyl přidán.")
zak()

