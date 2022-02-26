print ("Witaj! To jest prosty kalkulator. Zostaniesz poproszony o wybór typu działania oraz podanie dwóch liczb")
print("Możesz wykonać cztery podstawowe działania:")
print("1 - Dodawanie")
print("2 - Odejmowanie")
print("3 - Dzielenie")
print("4 - Mnożenie")
calculation_choice = input("Podaj działanie które chcesz wykonać:")

num1 = float(input("Podaj pierwszą cyfrę: "))
num2 = float(input("Podaj drugą cyfrę: "))

def dodawanie(a,b):
    return a+b

def odejmowanie(a,b):
    return a - b

def dzielenie(a,b):
    return a/b

def mnozenie(a,b):
    return a*b

if calculation_choice =="1":
    print("Wynik Twojego dodawania: ", dodawanie(num1, num2))
elif calculation_choice == "2":
    print("Wynik Twojego odejmowania: ", odejmowanie(num1, num2))
elif calculation_choice == "3":
    print("Wynik Twojego dzielenia: ", dzielenie(num1, num2))
elif calculation_choice == "4":
    print("Wynik Twojego mnożenia: ", mnozenie(num1, num2))

