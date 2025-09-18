k = float(input())
res = (
    "Logn" if k <= 0.2 else
    "Andvari" if k <= 1.5 else
    "Kul" if k <= 3.3 else
    "Gola" if k <= 5.4 else
    "Stinningsgola" if k <= 7.9 else
    "Kaldi" if k <= 10.7 else
    "Stinningskaldi" if k <= 13.8 else
    "Allhvass vindur" if k <= 17.1 else
    "Hvassvidri" if k <= 20.7 else
    "Stormur" if k <= 24.4 else
    "Rok" if k <= 28.4 else
    "Ofsavedur" if k <= 32.6 else
    "Farvidri"
)
print(res)
