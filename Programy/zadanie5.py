print("""Program ma za zadanie sprawdzić, czy z podanych przez Ciebie wartości da się utworzyć trójkąt pitagorejski
Upewnij się tylko, że podajesz liczby naturalne!""")
A = int(input("Podaj zatem pierwszą liczbę, śmiało! :"))
B = int(input("Świetnie, teraz podaj długość następnego boku: "))
C = int(input("No i jeszcze ostatnia liczba, dajesz!  "))
lista = [A, B, C]
dobra = sorted(lista)
print(dobra)
if A+B>C and A+C>B and B+C>A:
    print("Z podanych przez Ciebie wartości można utworzyć trójkąt!")
    if dobra[0]**2+dobra[1]**2==dobra[2]**2:
        print("W dodatku to trójkąt pitagorejski!")
        if dobra[0]*3==dobra[1]*4==dobra[2]*5:
            print("Jakby tego było mało, to ten trójkąt jest jeszcze egipski!")
        else:
            print("Trójkąt pitagorejski, ale zawsze mógł być to trójkąt egipski")
    else:
        print("Może to i trójkąt, ale nie pitagorejski!")
else:
    print("Niestety, z podanych przez Ciebie wartości nie można utworzyć trójkąta :(")