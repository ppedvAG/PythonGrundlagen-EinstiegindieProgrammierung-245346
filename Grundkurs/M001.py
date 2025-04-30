def list(*namen):
	if len(namen) == 0:
		print("Keine Teilnehmer")
	elif len(namen) == 1:
		print(namen[0])
	else:
		# gesamt = ""
		# for n in namen[:-1]:
		# 	gesamt += n + ", "
		# gesamt = gesamt.rstrip(", ") + " und " + namen[-1]
		# print(gesamt)

		print(", ".join(namen[:-1]) + " und " + namen[-1])


def list2(*namen):
	print("Keine Teilnehmer" if len(namen) == 0 else
		  namen[0] if len(namen) == 1 else
		  ", ".join(namen[:-1]) + " und " + namen[-1])

list2("Max", "Tim", "Udo", "Lea")
list2("Max")