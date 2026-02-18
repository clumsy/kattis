ms = {
    "A#": "Bb",
    "Bb": "A#",
    "C#": "Db",
    "Db": "C#",
    "D#": "Eb",
    "Eb": "D#",
    "F#": "Gb",
    "Gb": "F#",
    "G#": "Ab",
    "Ab": "G#",
}
try:
    i = 0
    while True:
        i += 1
        t, m = input().split()
        t = "UNIQUE" if t not in ms else f"{ms[t]} {m}"
        res = f"Case {i}: {t}"
        print(res)
except:
    pass
