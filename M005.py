# Schleifen
# Code mehrmals ausführen

a = 0
b = 10
while a < b:
	print(a)  # Einrückungen beachten!
	a += 1

# break und continue
# break: Beendet die Schleife
c = 0
while c < b:
	print(c)
	c += 1
	if c > 5:
		break
print("Nach der Schleife")

# continue: Springt an den Anfang der Schleife zurück; überspringt den gesamten Code nach dem continue Keyword
d = 0
while d < b:
	d += 1
	if d == 5:
		continue  # Überspringe bei d == 5 das print Statement
	print(d)

# Endlosschleife
e = 0
while True:  # while 1:
	e += 1
	if e > 500:
		break  # Endlosschleifen benötigen generell immer ein break

# else bei Schleife
# Wird nur ausgeführt, wenn die Schleife erfolgreich zu Ende läuft (ohne break)
f = 0
while f < 10:
	f += 1
	break
else:  # Mit break kein Output
	print("Schleife erfolgreich")

##################################################

# for-Schleife
# In anderen Sprachen als foreach-Schleife bekannt
# Benötigt immer eine Liste zum iterieren

l = [1, 2, 3, 4]
for zahl in l:
	print(zahl)

l2 = ["Hallo", "Welt", "!"]
for wort in l2:
	print(wort)

# Wird oft mit einer Range kombiniert
for x in range(10):
	print(x)

# for-Schleife mit mehreren Laufvariablen
# Bei Dictionary
auto = {
	"Marke": "VW",
	"Baujahr": 2020,
	"AnzSitze": 5
}

for k, v in auto.items():  # Die Inhalte von items() sind Tupel; diese werden hier zerlegt in zwei Teile (k und v)
	print(k + " von dem Auto ist: " + str(v))

# Unpacking
# Liste in einzelne Variablen zerlegen
u, i, o = [3, 5, 6]
print(u)
print(i)
print(o)

##################################################

# fstring
# Code in einen String einbetten
# string muss mit einem f beginnen
# Mit { } kann im Anschluss beliebiger Code in den String einbettet werden
# Konvertierung wird hier automatisch durchgeführt
for i in range(10):
	print("Die Zahl ist: " + str(i))
	print("Die Zahl^2 ist: " + str(i ** 2))
	print(str(i) + "^2=" + str(i ** 2))

	print(f"Die Zahl ist: {i}")
	print(f"Die Zahl^2 ist: {i ** 2}")
	print(f"{i}^2={i ** 2}")