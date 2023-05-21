# Obsluga regionu EUR/USA

while True:
    region = input("Wybierz swoj region: EUR/USA")
    if region == "EUR":
        print("W Europie picie alkoholu dozwolone jest od 18 r.z.")
        wiek = input("Podaj wiek użytkownika jako liczbe calkowitą:")
        if wiek.isdigit() == False:
          exit("Wiek musi być liczbą albo podana liczba nie jest calkowita")
          wiek = int(wiek)
        elif wiek>=18 and wiek<40:
	          print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
        elif wiek>=40 and wiek<=119:
	          print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
	          print("Uważaj w Twoim wieku nie przasadzaj ze spożyciem")
        elif wiek>=120:
            exit("Wpisano zbyt wysoki wiek. Zamykam aplikacje")  
     else:
        exit("Jesteś za młoda/y na alkohol. Zapraszamy na disney.com")      
    elif region == "USA":
        print("W USA picie alkoholu dozwolone jest od 21 r.z.")
        wiek = input("Podaj wiek użytkownika jako liczbe calkowitą:")
        if wiek.isdigit() == False:
          exit("Wiek musi być liczbą albo podana liczba nie jest calkowita")
          wiek = int(wiek)
        elif wiek>=21 and wiek<40:
	          print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
        elif wiek>=40 and wiek<=119:
	          print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
	          print("Uważaj w Twoim wieku nie przasadzaj ze spożyciem")
        elif wiek>=120:
            exit("Wpisano zbyt wysoki wiek. Zamykam aplikacje")  
        else:
            exit("Jesteś za młoda/y na alkohol. Zapraszamy na disney.com")
    else:
        print("Wybrales nieprawidlowy region. Sprobuj jeszcze raz.")

