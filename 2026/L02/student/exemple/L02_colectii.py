sarcini = [
    {"id": 1, "titlu": "Alegerea temei", "gata": False},
    {"id": 2, "titlu": "Citirea cerințelor", "gata": True},
]
for sarcina in sarcini:
    if not sarcina["gata"]:
        print(sarcina["id"], sarcina["titlu"])
