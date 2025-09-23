# Opdracht 3 tekstfuncties
# Naam student:
# Groep:

# Hier komt je code...

# instellingen
max_breedte = 9   
aantal_bomen = 5  

# boom genereren
boom = []
for stars in range(1, max_breedte + 1, 2):
    line = ("*" * stars).center(max_breedte)
    boom.append(line)

stam = ("***".center(max_breedte))
boom.extend([stam, stam, stam])

for line in boom:   
    print("  ".join([line] * aantal_bomen))