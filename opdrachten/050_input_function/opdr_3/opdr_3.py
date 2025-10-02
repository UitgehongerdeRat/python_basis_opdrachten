# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

input_str = input(['Sri Lanka', 'Rwanda', 'Oezbekistan', 'Finland', 'Chad'])


objecten = [item.strip() for item in input_str.split(",")]


objecten.sort(reverse=True)


print(objecten)