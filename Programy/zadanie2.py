print("Witam w kalkulatorze BMI!")
waga = int(input("Podaj swoją wagę w 'kg': "))
wzrost = int(input("\nA teraz podaj swój wzrost w 'cm': "))
BMI = waga/((wzrost/100)**2)
print ("\n")
if BMI<18.5:
    print("Niedowaga")
elif 18.5<BMI<=24:
    print("Waga normalna")
elif 24<BMI<=26.5:
    print("Lekka nadwaga")
elif 26.5<BMI<=30:
    print("Nadwaga")
elif 30<BMI<=35:
    print("Otyłość I stopnia")
elif 35<BMI<=40:
    print("Otyłość II stopnia")
elif 40<BMI<=80:
    print("Otyłość III stopnia")
else:
    print("Ups! Coś poszło nie tak drogi użytkowniku!")