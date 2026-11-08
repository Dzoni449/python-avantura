sobe = {
    "hodnik": {
        "ime": "Hodnik",
        "opis": "Dugačak, mračan hodnik. Sa zidova te gledaju stare slike.",
        "izlazi": {"sever": "kuhinja", "istok": "biblioteka"},
        "predmeti": [],
    },
    "kuhinja": {
        "ime": "Kuhinja",
        "opis": "Hladna kuhinja. Miriše na zagoreli hleb.",
        "izlazi": {"jug": "hodnik", "dole": "podrum"},
        "predmeti": ["lampa"],
    },
    "biblioteka": {
        "ime": "Biblioteka",
        "opis": "Police do plafona, pune prašnjavih knjiga.",
        "izlazi": {"zapad": "hodnik"},
        "predmeti": ["ključ", "knjiga"],
    },
    "podrum": {
        "ime": "Podrum",
        "opis": "Vlažno i tiho. U uglu svetluca stari kovčeg.",
        "izlazi": {"gore": "kuhinja"},
        "predmeti": ["blago"],
        "treba": "ključ",
    },
}

inventar = set()

trenutna = "hodnik"
soba = sobe[trenutna]
broj_poteza = 1

def prikazi_sobu(soba):
    print(f"== {soba['ime']} ==")
    print(soba["opis"])
    print(f"Izlazi: {(', '.join(sorted(soba['izlazi'])))}")

    if soba["predmeti"]:
        print(f"Ovde vidiš: {', '.join(soba['predmeti'])}") 


prikazi_sobu(soba)

komanda = input("> ").strip().lower()

while komanda != "kraj":
    reci = komanda.split()

    if komanda in soba["izlazi"]:
        cilj = soba["izlazi"][komanda]
        potreban = sobe[cilj].get("treba")

        if potreban and potreban not in inventar:
            print(f"Vrata su zaključana. Treba ti: {potreban}.")
        else:
            trenutna = cilj
            soba = sobe[trenutna]

            prikazi_sobu(soba)

    elif not reci:
        print("Ne možeš tamo.")

    elif reci[0] == "uzmi":
        if len(reci) > 1 and reci[1] in soba["predmeti"]:
            print(f"Uzeo si: {reci[1]}")
            soba["predmeti"].remove(reci[1])
            inventar.add(reci[1])
        else:
            print("Ovde nema toga.")

    elif komanda == "inventar":
        if inventar:
            print(f"Nosiš: {', '.join(sorted(inventar))}")
        else:
            print("Ruke su ti prazne.")

    else:
        print("Ne možeš tamo.")

    if "blago" in inventar:
        print(f"🏆 Pronašao si blago! Pobeda u {broj_poteza} poteza.")
        break

    broj_poteza += 1
    komanda = input("> ").strip().lower()

print("Doviđenja!")