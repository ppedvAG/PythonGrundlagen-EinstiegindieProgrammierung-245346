# Listentypen

# List
# Sammlung von beliebigen Elementen
# Wird mit [ ] Klammern definiert
l = [1, 2, 3, 4, 5, 6]  # Definition mit Startelementen

print(l)  # Für eine Ausgabe der Element wird keine Schleife benötigt

# Index
print(l[0])
print(l[-1])
print(l[1:4])

# Listenfunktionen

# append(Wert)
# Neuen Wert hinzufügen (am Ende)
l.append(10)
print(l)

# pop(Index), remove(Wert)
# pop: Entfernt das Element am gegebenen Index
# remove: Sucht das Element, und entfernt das erste Vorkommen
l.remove(3)
print(l)

l.pop(0)
l.pop(-1)  # Negative Zahlen auch hier möglich
print(l)

# sort()
# Sortiert die Liste
# WICHTIG: Die Elemente müssen alle den gleichen Typen haben
l.append(0)
l.sort()
print(l)

# Absteigend sortieren
l.sort(reverse=True)
print(l)

# Länge einer Liste
print(len(l))

# Arithmetik mit Listen
print([1, 2, 3] + [4, 5, 6])
l += [1, 2, 3, 4]
print(l)

print(l * 3)

###########################################

# Tuple
# Liste, die aber nicht verändert werden kann
# Wird mit ( ) definiert
t = (1, 2, 3)
print(t)

print(t + (4, 5, 6))
print(t * 3)

# Tupel über Umwege verändern
x = list(t)  # Zu einer List konvertieren
x.append(4)  # Neues Element hinzufügen
t = tuple(x)  # Zu einem Tuple konvertieren
print(t)

###########################################

# range
# Bereich von X bis Y
r = range(10)  # Zahlen von 0 bis 9
print(r)  # range(0, 10)

# Nur ein Generator
print(list(r))  # Generator ausführen mithilfe der list() Funktion

# Ober- und Untergrenze angeben
print(list(range(-10, 10)))

# + Schrittgröße
print(list(range(-100, 101, 5)))

###########################################

# set
# Funktioniert wie eine Liste, aber jedes Element muss eindeutig sein
# Wird mit { } definiert
s = {1, 2, 3, 4, 1, 1, 1, 4}
print(s)

s.add(5)
print(s)

###########################################

# dict
# Funktioniert wie ein Set, aber jeder Wert hat einen Namen (Schlüssel)
auto = {
	"Marke": "VW",
	"Baujahr": 2020,
	"AnzSitze": 5
}

print(auto)

# Index
print(auto["Marke"])  # Hier muss als Index ein String verwendet werden

# print(auto["KM"])  # Fehlermeldung (KM existiert nicht)
print(auto.get("KM"))  # Sicher, keine Fehlermeldung

# Neue Schlüssel hinzufügen
auto["KM"] = 5000
print(auto["KM"])

print(auto.keys())
print(auto.values())
print(auto.items())

###########################################

# Konvertierungen
# Werte in Variablen zu anderen Typen ändern
# Syntax: Zieltyp(Variable)

# String zu Zahl
a = "123"
a = int(a)  # Versucht den Inhalt von a zu einer Zahl umzuwandeln
print(a * 2)

b = "123.456"
b = float(b)
print(b * 2)

print(str(a) + str(b))

print(bool(a))  # Jeder Wert der nicht 0 ist, ist True
print(bool([]))  # Leere Liste -> bool: False