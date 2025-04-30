# Fehlerbehandlung

# Vermeidung des Absturzes bei unerwarteten Fehlern
# Beispiel: Alles mit externen Resourcen; Unerreichbarkeit

# eingabe = input("Gib eine Zahl ein: ")
# z = int(eingabe)  # Unerwarteter Fehler: User gibt Buchstaben ein

# try-except
# Zwei Blöcke: try-Block, except-Block
# try-Block enthält den Code, welcher ausgeführt werden soll (und potenziell Fehler wirft)
# except-Block enthält den Code, welcher die Fehlerbehandlung durchführt, und das Skript nicht zum Absturz bringt

try:
	eingabe = input("Gib eine Zahl ein: ")
	z = int(eingabe)  # Unerwarteter Fehler: User gibt Buchstaben ein
except ValueError as VE:  # Except-Block mit einem einzelnen Fehler
	print("Keine Zahl eingegeben")
	print(VE)  # Dem Error einen Namen zuweisen mittels as <Name>
except:  # Except-Block ohne Fehler behandelt alle anderen Fehler
	print("Anderer Fehler")
else:  # Else-Block: Wird ausgeführt, wenn der try-Block ohne Fehler ausgeführt wurde
	print("Ohne Fehler durchgelaufen")
finally:  # Finally-Block: Wird immer ausgeführt
	print("Fertig")


# Eigenen Fehler werfen (Programm abstürzen lassen)
raise NotImplementedError("Hier ist die Baustelle zu Ende")
print("Skript Ende")

# Warum raise?
# Wenn wir eine Fehlermeldung in die Konsole schreiben, wird diese möglicherweise von einem User übersehen
# z.B.: Webseite, Desktopanwendung, Mobilapp, ...
# Wenn das Programm per raise abstürzt, kann der Programmierer, welcher den Absturz mitbekommt, ein try-except einbauen
# und dadurch den Fehler beliebig behandeln
# z.B.: Auf eine Webseite schreiben, in eine DB schreiben, eine Handybenachrichtigung senden