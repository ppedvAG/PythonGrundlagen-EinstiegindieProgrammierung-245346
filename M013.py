# Decorator
# Wrapper für Funktionen, welcher Code vor/nach einer Funktion ausführt

def testDecorator(func):  # func: Funktion, welche dekoriert werden soll
	def wrapper():
		print("Vorher")
		func()
		print("Nachher")
	return wrapper


@testDecorator
def halloWelt():
	print("Hello World")


# Decorator davor
halloWelt()
# Decorator danach

###########################################

def testDecoratorParameter(func):
	def wrapper(*args, **kwargs):  # Dieser Decorator kann dank *args und **kwargs alle Funktionen in Python dekorieren
		print("Vorher")
		func(*args, **kwargs)
		print("Nachher")
	return wrapper


@testDecoratorParameter
def hallo(name: str):
	print(f"Hallo {name}")


hallo("Max")

###########################################

# Praktisches Beispiel: Zeitmesser

def measureTime(func):
	import time
	def wrapper(*args, **kwargs):
		start = time.time()
		func(*args, **kwargs)
		end = time.time()
		print(end - start)
	return wrapper


@measureTime
def generateNumbers():
	list(range(100_000_000))


generateNumbers()