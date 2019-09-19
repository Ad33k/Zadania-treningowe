man = ["Andrzej", "Adrian", "Bartek", "Grzegorz", "Michał", "Tomasz", "Zenon"]
woman = ["Anita", "Cecylia", "Dominika", "Monika", "Magda", "Patrycja"]
imie = input("Podaj swoje imię: ")
if imie in man:
    print("Jesteś mężczyzną!")
elif imie in woman:
    print("Jesteś kobiętą!")
elif imie not in man or woman:
    print("Niestety, jeszcze nie znamy twoje imienia")
    plec = input("Jeśli jesteś mężczyzną, wpisz 'm', jeśli jednak jesteś kobietą, wpisz 'w' ")
    if plec == "m":
        man.append(imie)
        print("Dziękujemy! Zaktualizowana lista imion to: ")
        print(sorted(man))
    elif plec == "w":
        woman.append(imie)
        print("Dziękujemy! Zaktualizowana lista imion to: ")
        print(sorted(woman))
    else:
        "Ups! Coś poszło nie tak!"
else:
    print("Ohoho, coś się nie udało!")