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



# def pridej_znamku(zak):
#     nahodne_cislo = random.randint(1, 5)
#     # print(f"Známka je: {nahodne_cislo}")
#     zaci[zak].append(nahodne_cislo)

def zak():
    with open('zaci.json', 'r') as file:
        zaci = json.load(file)
        print(zaci)

    pridej_znamku = random.randint(1, 5)

    kdo = input(f"Komu?: ")

    if kdo in zaci:
        znamka = input(f"Chceš přidat random známku?: ")
        if znamka == "ne":
            znamky = int(input(f"Jakou známku chceš přidat?: "))
            zaci[kdo].append(znamky)
            print(f"Známka pro {kdo} je: {znamky}")
        else:
            print(f"Známka pro {kdo} je: {pridej_znamku}")
            #  pridej_znamku(kdo)
            #  zaci[kdo].append(znamka)

        print(f"SHFHHF {zaci[kdo]}")
        prumer_znamek = sum(zaci[kdo]) / len(zaci[kdo])
        

        with open("zaci.json", "w", encoding="utf-8") as f:
            json.dump(zaci, f, ensure_ascii=False, indent=4)

        if prumer_znamek > 3:
            print(f"Průměr známky pro {kdo} je: {prumer_znamek:.2f}")
            print(f"RAHHHHHHHHHHH >:[")
        else:
            print(f"Průměr známky pro {kdo} je: {prumer_znamek:.2f}")
            print(f"NOMNOMNOM :D")
    else:
        print("Tento žák není v seznamu.")
        pridat = input("Přidat?: ")
        if pridat == "ano":
            zaci[kdo] = []
            with open("zaci.json", "w", encoding="utf-8") as f:
                json.dump(zaci, f, ensure_ascii=False, indent=4)
            print(f"Žák {kdo} byl přidán do seznamu.")
            with open('zaci.json', 'r') as file:
                zaci = json.load(file)
            znamka = input(f"Chceš přidat random známku?: ")
            if znamka == "ne":
                with open("zaci.json", "w", encoding="utf-8") as f:
                    json.dump(zaci, f, ensure_ascii=False, indent=4)
                znamky = int(input(f"Jakou známku chceš přidat?: "))
                zaci[kdo].append(znamky)
                print(f"Známka pro {kdo} je: {znamky}")
            else:
                # pridej_znamku(kdo)
                # zaci[kdo].append(znamka)
                print(f"Známka pro {kdo} je: {pridej_znamku}")
        elif pridat == "ne":
            print("Žák nebyl přidán.")
        with open("zaci.json", "w", encoding="utf-8") as f:
            json.dump(zaci, f, ensure_ascii=False, indent=4)
zak()

