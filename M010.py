# Klassen und Objekte

# Klassen stellen den Bauplan für Objekte dar
# Aus der Klasse können beliebig viele Objekte erstellt werden
# Jedes Objekt hat einen Typen; der Typ ist immer mit einer Klasse verbunden

# Jede Klasse enthält Funktionen
# Diese Funktionen werden an die Objekte weitergegeben
# Jedes Objekt kann dann über sich selbst die Funktionen ausführen
s = "Hallo"
s.lower()  # Die lower() Funktion kennt den string s; in der Funktion wird dieser als "self" bezeichnet

#################################################################

# Eigene Klasse

# Zwei Arten von Membern welche definiert werden
# - Felder (Daten halten; Eigenschaften)
# - Funktionen

# Person
# - Felder: Vorname, Nachname, Alter, Adresse
# - Funktionen: Sprechen, Bewegen
class Person:
	"""
	docstring

	Klassen/Funktion dokumentieren
	"""
	def __init__(self, vorname: str, nachname: str, alter: int, adresse: str):  # self: Das Objekt selbst
		"""
		__init__: Startfunktion des Objekts

		Wenn ein Objekt von der Klasse erzeugt wird, wird diese Funktion ausgeführt

		Hier werden die Felder definiert
		"""
		self.vorname = vorname  # Hier wird der Parameter an das Objekt angehängt
		self.nachname = nachname
		self.alter = alter
		self.adresse = adresse

	def bewegen(self, distanz: int):
		print(f"Die Person {self.vorname} {self.nachname} bewegt sich um {distanz}m.")

	def sprechen(self, text: str):
		print(f"{self.vorname} sagt: {text}")


p = Person("Max", "Mustermann", 33, "Wien")

print(f"Die Person {p.vorname} {p.nachname} ist {p.alter} Jahre alt, und wohnt in {p.adresse}")

# Funktionen in einer Klasse benötigen immer ein Objekt
p.sprechen("Hallo")
Person.sprechen(p, "Hallo")