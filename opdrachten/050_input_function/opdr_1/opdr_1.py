# Opdracht 1 input function
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.


import math


zijde_1 = float(input("Geef de lengte van de eerste zijde: "))
zijde_2 = float(input("Geef de lengte van de tweede zijde: "))


schuine_zijde = math.sqrt(zijde_1**2 + zijde_2**2)


print("De lengte van de schuine zijde is:", schuine_zijde)