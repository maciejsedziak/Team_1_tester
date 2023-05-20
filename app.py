wiek = input("Podaj wiek:")
if wiek.isdigit() == False:
	exit("Wiek musi być liczba calkowita")
wiek=int(wiek)
if wiek>=18:
	print("mozesz kupic aperol w Europie")
else:
	exit("nie mozesz kupic alkoholu w Europie")