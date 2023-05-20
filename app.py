wiek = input("Podaj wiek użytkownika jako liczbe calkowitą:")
# Sprawdzamy czy podany wiek jest liczbą
if wiek.isdigit() == False:
	exit("Wiek musi być liczbą albo podana liczba nie jest calkowita")
wiek=int(wiek)
if wiek>=18 and wiek<40 and wiek<=119:
	print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
elif wiek>=40 and wiek<=119:
	print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
	print("Uważaj w Twoim wieku nie przasadzaj ze spożyciem")
elif wiek>=120:
	print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
	print("Gratulujemy pieknego wieku!")
else:
  exit("Jesteś za młoda/y na alkohol. Zapraszamy na disney.com")

