def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnożenie(a, b):
    return a * b

def dzielenie(a, b):
        if b!= 0:
            return a / b
        else:
            return("Nie można dzielić przez 0")

print("wybierz tryb:")
print("1. dodawanie")
print("2. odejmowanie")
print("3. mnożenie")
print("4. dzielenie")

wybierz = input("Wybierz tryb (1,2,3,4):")

if wybierz in ("1","2","3","4"):
    Liczba1 = int(input("Wpisz pierwszą liczbę: "))
    Liczba2 = int(input("Wpisz drugą liczbę:"))

    if wybierz == '1':
        print(Liczba1, "+", Liczba2, "=", dodawanie(Liczba1, Liczba2))

    if wybierz == '2':
        print(Liczba1, "-", Liczba2, "=", odejmowanie(Liczba1, Liczba2))

    if wybierz == '3':
        print(Liczba1, "*", Liczba2, "=", mnożenie(Liczba1, Liczba2))

    if wybierz == '4':
        print(Liczba1, "/", Liczba2, "=", dzielenie(Liczba1, Liczba2))


