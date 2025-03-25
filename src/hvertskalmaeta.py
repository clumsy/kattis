m = {
    "Reykjavik": {
        "Reykjavik": 0,
        "Kopavogur": 6,
        "Hafnarfjordur": 12,
        "Reykjanesbaer": 48,
        "Akureyri": 388,
        "Gardabaer": 9,
        "Mosfellsbaer": 16,
        "Arborg": 64,
        "Akranes": 49,
        "Fjardabyggd": 659,
        "Mulathing": 603,
        "Seltjarnarnes": 4,
    },
    "Akureyri": {
        "Akureyri": 0,
        "Reykjavik": 388,
        "Kopavogur": 387,
        "Hafnarfjordur": 391,
        "Reykjanesbaer": 427,
        "Gardabaer": 389,
        "Mosfellsbaer": 371,
        "Arborg": 428,
        "Akranes": 350,
        "Fjardabyggd": 290,
        "Mulathing": 216,
        "Seltjarnarnes": 390,
    }
}
s = input()
res = "Reykjavik" if m["Reykjavik"][s] <= m["Akureyri"][s] else "Akureyri"
print(res)
