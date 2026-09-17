# Gebruik een zelfgemaakte dictionary (of onderstaande).
fruitmand = { # Sleutel is fruit, element is aantal
    "appel": 5,
    "banaan": 3,
    "kers": 50
}
sleutel =input("geef een sleutel")
if sleutel not in fruitmand:
    print("niet bestaand")
else:
    print(f"Aantal{sleutel} in mand {fruitmand[sleutel]}")

