x = round(float(input("Wprowadź pierwszą liczbę: ")), 2)
y = round(float(input("Wprowadź drugą liczbę: ")), 2)
z = round(float(input("Wprowadź trzecią liczbę: ")), 2)
tablica = [x,y,z]
print("Max = ", max(tablica))
print("Min = ", min(tablica))
print(sorted(tablica))
