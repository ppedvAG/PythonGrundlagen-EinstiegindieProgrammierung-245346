# List Comprehension
# Anhand einer kompakten Syntax eine Liste erzeugen

# Syntax: [<Laufvariable> <for-Schleife>]
print([i for i in range(10)])

# if-Anweisung in List Comprehension
# -> Es werden am Ende weniger Elemente in der fertigen Liste sein
print([i for i in range(10) if i % 2 == 0])

# Linke Seite verändern
# -> Die Elemente, die in die Liste kommen, sind nicht nur einfache Zahlen, sondern haben eine bestimmte Form
print([i ** i for i in range(10)])

print([f"Die Zahl ist: {i}" for i in range(10)])

print(["X" for i in range(10)])

print([bool(i % 2) for i in range(10)])

# Verschachtelte Schleifen
# Mehrere Schleifen in eine LC packen
print([f"{i}*{j}={i * j}" for i in range(1, 11) for j in range(1, 11)])

# Ternary Operator
# In die Linke Seite Bedingungen einbauen, um das Aussehen bedingt zu machen
print(["FizzBuzz" if i % 3 == 0 and i % 5 == 0 else
	   "Fizz" if i % 3 == 0 else
	   "Buzz" if i % 5 == 0 else
	   i for i in range(1, 101)])