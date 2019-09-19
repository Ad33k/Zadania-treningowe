age = int(input("Ile masz lat? \n"))
if age<18:
    print("Jesteś niepełnoletni!")
elif age>=18 and age<=100:
    print("Użytkownik pełnoletni")
elif age>100 and age<200:
    print("200 lat ♫")
else:
    print("To nie możliwe")