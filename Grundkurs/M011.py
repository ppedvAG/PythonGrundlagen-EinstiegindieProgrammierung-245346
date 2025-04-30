# Vererbung
# Basisklassen definieren, welche ihre Inhalte nach unten weitergeben
# Intern: Object; Oberklasse von allen Klassen

# Beispiel:
# - Lebewesen (Oberklasse)
# - Mensch (Unterklasse)
# - Hund (Unterklasse)

class Lebewesen:
	def __init__(self, alter: int):
		self.alter = alter

	def bewegen(self, distanz: int):
		print(f"{type(self).__name__} bewegt sich um {distanz}m.")


class Mensch(Lebewesen):  # Vererbung herstellen über Oberklasse in der Klammer
	def __init__(self, alter: int, name: str):
		super().__init__(alter)  # super(): Greife in die Oberklasse, und führe die __init__ Methode aus
		self.name = name

	def __eq__(self, other):
		return self.alter == other.alter and self.name == other.name


class Hund(Lebewesen):
	pass


m = Mensch(33, "Max")
m.bewegen(10)

m2 = Mensch(33, "Max")
print(m == m2)

h = Hund(10)
h.bewegen(50)

###################################################

# __str__
# Gibt eine Stringrepräsentation von dem Objekt zurück
# Kann in eigenen Klassen überschrieben werden

print(m.__str__())  # <__main__.Mensch object at 0x0000025F050B6030> (Standard)
x = 123
print(x.__str__())  # 123 (Standard geändert)
y = [1, 2, 3]
print(y.__str__())  # [1, 2, 3] (Standard geändert)

print(m)
print(x)
print(y)