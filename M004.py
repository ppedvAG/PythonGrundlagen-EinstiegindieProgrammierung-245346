# If-Anweisungen

z1 = 8
z2 = 5
if z1 > z2:
	print(z1)  # WICHTIG: Einrückungen beachten
	print(z2)

if z1 > z2:
	print(z1)
elif z1 < z2:  # elif: Else-If in einem Keyword
	print(z2)
else:
	print(z1 + z2)

#######################################

# Logische Operatoren
# and, or, not
# &, |, ~

if z1 > z2 and z1 > 5:
	print("...")

if z1 > 5 or z2 > 5:
	print("...")

# in
# Prüft ob ein Wert in einer Liste enthalten ist
if z1 in range(10):  # ist z1 in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]?
	print("z1 ist zw. 0 und 9")

if z1 in (1, 2, 3):
	print("...")

l = [1, 2, 3]
if z1 in l:
	print("...")

#######################################

# Ternary Operator
# If-Elif-Else Bäume einzeilig machen

if z1 > z2:
	print(z1)
elif z1 < z2:
	print(z2)
else:
	print(z1 + z2)

print(z1) if z1 > z2 else print(z2) if z1 < z2 else print(z1 + z2)  # Jedes else trennt die Bedingungen voneinander

print(z1 if z1 > z2 else z2 if z1 < z2 else z1 + z2)