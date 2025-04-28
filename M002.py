# Kommentar
print("Hello World")  # Schreibt "Hello World" in die Konsole

# Variablen
# Feld, welches einen Wert halten kann
# WICHTIG: Eine Variable hat keinen Typen; der Typ der Variable wird über den Inhalt bestimmt
x = 5
print(type(x))  # <class 'int'>

x = "Hallo"
print(type(x))  # <class 'str'>

# Datentypen

# int: Ganze Zahlen (-∞, +∞)
i = 316487324612935236195237816416324578621358762391578263428379567812936547823

# float: Kommazahlen (-∞, +∞)
f = 31648732461293523619523781641632.4578621358762391578263428379567812936547823

# str: String; Text mit beliebiger Länge
s1 = "Hallo"  # Doppelte Hochkomma möglich
s2 = 'Hallo'  # Einzelne Hochkomma möglich (kein Unterschied)
print(s1)
print(s2)

# bool: Wahr-/Falschwert
t = True
b = False  # Großschreibung beachten

# complex: Komplexe Zahlen
c = 12 + 5j
print(type(c))  # <class 'complex'>

############################################################

# Index
# Bestimmte Stellen aus Listen entnehmen
# String ist auch eine Liste
s = "Hallo Welt"
print(s[0])  # H
print(s[1])  # a

# Index von der anderen Seite
print(s[-1])  # t
print(s[-2])  # l
print(s[-3])  # e
print(s[-4])  # W

# Bereichsindex
# Mit einem Doppelpunkt kann von X bis Y genommen werden
print(s[0:5])  # Hallo
print(s[6:10])  # Welt

# WICHTIG: Obergrenze wird nie genommen (exklusiv)
print(s[:5])  # Grenze kann weggelassen werden (vom Anfang bis 5)
print(s[6:])  # Von 6 bis zum Ende

############################################################

# Stringfunktionen

# islower(), isupper()
# Prüfen, ob der gesamte String lowercase oder UPPERCASE ist
print(s.islower())
print(s.isupper())

# WICHTIG: Einzelne Zeichen sind selbst auch Strings
s[0].islower()
print(s[0].isupper())  # Fängt der String mit einem Uppercase Zeichen an?

# title(), capitalize()
# Schreiben den String mit Anfangsbuchstaben Groß, rest klein
s.title()  # Alle Wörter Groß
s.capitalize()  # Nur der allererste Buchstabe Groß

# count()
# Zählt, wie oft ein gegebenes Zeichen in dem String enthalten ist
print(s.count("H"))

# WICHTIG: Case-Sensitive
n = "Max Mustermann"
print(n.count("M"))

# lower(), upper()
# Schreibt den gesamten String klein oder GROß
print(s.upper())
print(s.lower())

############################################################

# Arithmetische Operatoren
# Klassiker: +, -, *, /

z1 = 4
z2 = 7
z1 + z2  # WICHTIG: z1 und z2 bleiben unverändert

z1 += z2  # += verändert z1, + alleine verändert nichts
z1 = z1 + z2

print(z1 + z2)  # + alleine berechnet nur die Summe

# Modulo (%): Rest einer Division
# 12 / 5 = 2
#  2R. -> Ergebnis von Modulo

print(12 % 5)

# Potenzoperator
# X^Y
print(2 ** 3)  # 2^3=8

print(5 ** 5)  # 5^5=3125

p1 = 5
p2 = 5
p1 **= p2

# Ganzzahldivision
# In anderen Sprachen: Wenn zwei Integer dividiert werden, kommt ein Integer heraus
# 8 / 5 = 1
print(8 / 5)  # 1.6
print(8 // 5)  # 1, Kommastellen werden abgeschnitten

# Arithmetik mit Strings
t1 = "Hallo"
t2 = "Welt"
print(t1 + t2)

t1 += t2

# print("Hallo" + 5)  # str und int kann in Python nicht addiert werden
print("20" + "20")  # 2020 und nicht 40
print("20" * 20)  # Strings können multipliziert werden