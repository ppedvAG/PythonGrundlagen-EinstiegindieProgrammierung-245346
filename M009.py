# In-/Output

# print()
x = 4
y = "Hallo"
z = [1, 2, 3]
print(x, y, z, sep=" - ")

# input()
# Verlangt vom Benutzer eine Eingabe
# Gibt dem User einen Prompt
eingabe = input("Gib eine Zahl ein: ")
print(f"Du hast {eingabe} eingegeben!")

# open()
# Öffnet eine Datei zum Lesen/Schreiben

# Datei schreiben
file = open("Test.txt", "w")
file.write("Hallo")  # Schreibt "Hallo" in den Buffer
file.write("Welt")  # Schreibt "Welt" in den Buffer
file.flush()  # Schreibt den gesamten Buffer in die Datei
file.close()  # Wichtig: Dateien immer schließen

# Datei lesen
file = open("Test.txt", "r")
lines = file.readlines()
print(lines)
file.close()

#######################################################

# with-Block
# Schließt den unterliegenden Stream am Ende des Blocks automatisch
# Syntax: with open(...) as <Name>:
# Das File ist nur innerhalb des Blocks angreifbar
with open("Test.txt", "r") as f:
	print(f.readlines())

#######################################################

# Escape-Sequenzen
# \n, \t, \\

# rstring
# raw string
# String, welcher keine Escape-Sequenzen interpretiert
pfad = r"C:\Users\lk3\Desktop"
p2 = "C:\\Users\\lk3\\Desktop"

#######################################################

# os.path
import os.path
os.path.exists("Test.txt")
print(os.path.sep)  # \

print(os.path.join("Users", "lk3", "Desktop"))