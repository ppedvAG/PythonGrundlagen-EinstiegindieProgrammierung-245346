# Funktionen
# Code wiederverwenden
from argparse import ArgumentError


def halloWelt():
	print("Hallo Welt")

halloWelt()
halloWelt()
halloWelt()


# Funktion mit Parameter
# Über Parameter können einer Funktion Daten mitgegeben werden
def hallo(vorname):
	print(f"Hallo {vorname}")

hallo("Lukas")
hallo("Anita")


# Funktion mit Rückgabewert
# Diese Funktion gibt einen Wert zurück
# Dieser Wert kann dann in eine Variable geschrieben/bei einer anderen Funktion eingesetzt werden
def addiere(x, y):
	return x + y  # return beendet die Funktion

summe = addiere(4, 5)  # Über die Variable wird das Ergebnis gefangen
print(summe)

print(addiere(4, 5))

#########################################################

# Typempfehlungen
# Bei Parametern/Rückgabewerten ist nie ein Typ vorgegeben
# D.h. addiere könnte beliebige Werte empfangen
print(addiere(4, 5))
print(addiere(2.5, 8.3))
print(addiere("Hallo", "Welt"))  # Sollte nicht möglich sein
print(addiere([1, 2, 3], [4, 5, 6]))  # Sollte nicht möglich sein

# Mit Empfehlungen
def addiere2(x: int, y: int) -> int:
	return x + y

print(addiere2(8, 2))
print(addiere2(4.6, 2.3))  # Fehlerhafte Typen funktionieren trotzdem
print(addiere2("Hallo", "Welt"))
print(addiere2([1, 2, 3], [4, 5, 6]))

# Mit Typprüfungen
def addiere3(x: int, y: int):
	if type(x) == int and type(y) == int:
		return x + y
	else:
		raise ArgumentError(None, "X und Y müssen Integer sein")

print(addiere3(4, 5))
# print(addiere3(4.3, 5.5))

# Mehrere Typen empfehlen
def addiere4(x: int | float, y: int | float) -> float:
	return x + y

print(addiere4(4, 5))
print(addiere4(4.9, 5.1))

#########################################################

# Default Values
# Parameter können Standardwerte haben
# Können überschrieben werden bei Funktionsaufruf
def dividiere(x, y = 1):
	return x / y

dividiere(10)  # Ein Parameter (y = 1)
dividiere(10, 4)  # Zwei Parameter (y = 4)

# In der Praxis: Es gibt viele Funktionen mit 20+ Parametern
# Von diesen 20+ Parametern sind fast alle optional
# Beispiel: pandas.read_csv

# Optionale Parameter können auch direkt angesprochen und überschrieben werden
def printPerson(vorname: str = "", nachname: str = "", wohnort: str = "", alter: int = -1):
	print("...")

printPerson(wohnort="Zuhause", alter=30)
printPerson(vorname="Max")
printPerson(nachname="Mustermann", alter=50, vorname="Max")
printPerson("Max", "Mustermann", alter=44)

#########################################################

# Arbitrary Arguments
# Parameter, welcher beliebig viele Werte akzeptiert
def summe(*zahlen: int):
	ergebnis = 0
	for x in zahlen:
		ergebnis += x
	print(ergebnis)


# Beliebig viele Parameter möglich
summe(1, 2, 3)
summe(4, 9, 2, 1, 49, 28, 10, 38)
summe(1)
summe()


# Arbitrary Keyword Arguments
# Parameter, welcher beliebig viele BENANNTE Werte akzeptiert
def printTeilnehmer(**tn: str):
	for k, v in tn.items():
		print(f"{k}: {v}")

printTeilnehmer(Trainer="Lukas", T1="Anita")


# Unpacking
# Bestehende Liste/Tupel/Dict/str/... in Einzelteile zerlegen, damit diese in *args und **kwargs übergeben werden können
z = [1, 8, 3, 2, 9, 1]
summe(*z)  # * oder **: Unpacking Operator

namen = {
	"Trainer": "Lukas",
	"T1": "Anita"
}

printTeilnehmer(**namen)

a, b, c, d, e, f = z

j, *k, l = z
print(j)
print(k)
print(l)