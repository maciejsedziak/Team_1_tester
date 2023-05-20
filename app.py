  # Obsluga regionu EUR/USA

while True:
    region = input("Wybierz swoj region: EUR/USA lub wyjdz: Q   ")
    if region == "EUR":
        print("W Europie picie alkoholu dozwolone jest od 18 r.z.")
        wiek = input("Podaj wiek użytkownika jako liczbe calkowitą:")
        if wiek.isdigit() == False:
            exit("Wiek musi być liczbą albo podana liczba nie jest calkowita")
        wiek = int(wiek)
        if wiek >= 18 and wiek <= 40:
            print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
        elif wiek > 40:
            print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
            print("Uważaj w Twoim wieku nie przasadzaj ze spożyciem")
        else:
            exit("Jesteś za młoda/y na alkohol. Zapraszamy na disney.com")
        break
    elif region == "USA":
        print("W USA picie alkoholu dozwolone jest od 21 r.z.")
        wiek = input("Podaj wiek użytkownika jako liczbe calkowitą:")
        if wiek.isdigit() == False:
            exit("Wiek musi być liczbą albo podana liczba nie jest calkowita")
        wiek = int(wiek)
        if wiek >= 21 and wiek <= 40:
            print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
        elif wiek > 40:
            print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
            print("Uważaj w Twoim wieku nie przasadzaj ze spożyciem")
        else:
            exit("Jesteś za młoda/y na alkohol. Zapraszamy na disney.com")
        break
    elif region == "Q":
        break
    else:
        print("Wybrales nieprawidlowy region. Sprobuj jeszcze raz.")
