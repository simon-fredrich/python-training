powers_of_two = []
for x in range(100):
    powers_of_two.append(2**x)

print(powers_of_two)
print(len(powers_of_two))
print(x) # will print 99 -> sideeffect

# another way without sideeffects
powers_of_two = list(map(lambda y: 2**y, range(100)))
print(powers_of_two)
print(len(powers_of_two))

try:
    print(y)
except NameError:
    print("y ist nicht definiert also hat der zweite Weg keine Auswirkungen auf den global scope.")

