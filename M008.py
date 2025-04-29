# Module
# Verbinden von mehreren Python Skripten
# Jedes Modul ist ein eigenes Python Skript

# Module einbinden:
# - import <Name>
# - from <Name> import <Member>
# Jeder Import kann auch noch einen Alias erhalten (as <Alias>)

# import
# Wenn ein Skript importiert wird, wird es immer vollständig ausgeführt
# Wenn ein import durchgeführt wird, wird jeder Member (Variable, Funktion oder Klasse) aus dem Skript importiert
# Nach dem import kann alles was in dem Skript definiert wurde hier verwendet werden
import M007
M007.summe(1, 2, 3, 4, 5)

import M001 as Eins
Eins.list2("Max", "Tim", "Udo")

# from import
# Importiert nur angegebene Member aus dem gegebenen Skript
from M007 import addiere, addiere2, addiere3, addiere4
print(addiere(4, 5))  # Bei Verwendung muss der Name des Skripts hier nicht angegeben werden

# from <Name> import *
from M007 import *
print(addiere4(3, 4))

####################################################

# Modul Suchpfade
# Im sys Paket gibt es eine Variable namens path
# Diese enthält alle Pfade, an denen Module gesucht werden
import sys
for p in sys.path:
	print(p)

# Reihenfolge:
# - Im selben Ordner/Unterordner vom Skript
# - Standardbibliothek
# - In der venv (externe Pakete)
# - Eigene Pfade
# Wenn das Modul nicht gefunden wird -> ModuleNotFoundError

sys.path.append(r"C:\Users\lk3\Desktop")  # Eigenen Pfad hinzufügen

####################################################

# Externe Pakete installieren

# Zwei Optionen:

# Python Packages
# - Name eingeben
# - Install drücken

# pip
# - pip install <Name>
# - pip uninstall <Name>

# Externe Pakete werden in .venv/Lib/site-packages installiert

####################################################

# Die Main Methode
# Startpunkt des Skriptes
# Generell sollte ein Skript selbst keinen Code ausführen
# - Code sollte nur Funktionen und Klassen anlegen
# - Diese Definition sollten dann vom importierenden Skript verwendet werden

# Wenn Code bei Skriptausführung passieren soll, gibt es dafür die Main-Methode
if __name__ == "__main__":  # Wird nur ausgeführt, wenn das Skript direkt ausgeführt wird (nicht bei import)
	print("...")

# __name__
# __main__, wenn das Skript direkt ausgeführt wird
# Der Name des Skripts selbst, bei import

print(__name__)  # __main__

####################################################

# Packages
# Ordner, um im Projekt Ordnung zu schaffen
from M008_Test import Test

# __init__.py
# Wird ausgeführt, wenn der Ordner angegriffen (ein oder mehrere Skript(e) importiert werden)