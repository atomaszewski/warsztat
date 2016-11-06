print( """to jest prosta gra w zbijanie statku
twoje zadanie bedzie polegac na tym aby,
majac cztery strzaly (0-4)znalesc statek
             !!POWODZENIA!!"""
)

from random import randint # przywolanie modulu do generowania losowych liczb

plansza = []

for _ in range(5):     # funkcja ta tworzy nasza tablice gdzie z range(0 ,1, 2, 3, 4, )
    plansza.append(["0"]* 5) # birzzemy tylko pozycje 0 i zwiekszamy ja o 5 razy
                             # tworzy nam sie lista dluga a dokladnie 5X ['0', '0', '0', '0', '0']
# ta funkcja ponizej ma nam wyswietlin nasza wczesniej wyzej strorzona liste nie w jednym ciagu
def wydruk_planszy(plansza):   # tylko w kolejnych wierszach 
    for pola in plansza:
        print(pola)

#wydruk_planszy(plansza)

# wydruk tej samej planszy tylko ze usuwamy zbedne elementy
# aby nasza plansza ladniej wygladala usuwamy "" pozostawiajac tylko same O
def wydruk_planszy_czyszczenie(plansza):
    for linia in plansza:
        print(" ".join(linia)) 
wydruk_planszy_czyszczenie(plansza)

# kojene dwie funkcje to beda nasze zmienne pionowa i pozioma , (statek_linia_ponioma oraz statek_linia_pionowa)
# w nich umieszczimy nasz statwek losowo 
# uzyjemy tutaj moduli randint

def linia_pozioma(plansza):
    return randint(0, len(plansza) -1)
def linia_pionowa(plansza):
    return randint(0, len(plansza) - 1)

statek_pozycja_x = linia_pozioma(plansza) #( row)
statek_pozycja_y = linia_pionowa(plansza)  # (col)


# gdy juz ukryliśmy nasz statek pora aby zgadnac i dac mozliwosc podania dwoch liczb
# calosc umieszczamy w petli ktora konczy sie wraz z czterema probami
tura = 0
while tura < 4:
    pozycja_x = int()
    pozycja_y = int()
    while pozycja_x != -1:
        try:
            pozycja_x = int(input("podaj pozycje x :"))
        except(ValueError, NameError):
            print("Błąd, to nie jest liczba \n")
            continue
        try:
            pozycja_y = int(input("podaj pozycje y :"))
        except(ValueError, NameError):
            print("Błąd, to nie jest liczba \n")
            print("podaj jeszcze raz dwie liczby\n")
            continue
        if int(pozycja_x) and int(pozycja_y) >= 0 :
            break
    

    # sprawdzamy tutaj czy nasze namiary sa takie same jak losowe gdzie ukryty zostal statek
    
    if statek_pozycja_x == pozycja_x and statek_pozycja_y == pozycja_y:
        print("Gratulacje! zatopiles moj statek ")
        break
# tutaj sprawdzamy czy podane liczby mieszcza sie w zasiegu naszej mapy 
    elif pozycja_x not in range(5) or pozycja_y not in range(5):
        print("strzal po za zakres mapy, spruboj jeszcze raz!! ")
# tutaj sprawdzamy czy juz wczesniej nie strzelalismy w to miejsce        
    elif plansza[pozycja_x][pozycja_y] == "x":
        print("Juz tu strzelaleś, wybierz inne koordynaty !!")

    else: # po sprawdzeniu i przy braku trafienia wyswietla sie informacja 
    # tutaj odlicza sie nasza petla, oraz na mapie zaznacza sie miejsce gdzie celowalismy
        print("Pudlo, sprobuj jeszcze raz")
        plansza[pozycja_x][pozycja_y] = "x"
        print(wydruk_planszy_czyszczenie(plansza))
        tura = tura + 1
        print("to jest tura: ",tura)

        if tura == 4:
            print("koniec strzalów, Game Over")
            
input("\n\nAby zakonczyc program, nacisnij klawisz Enter.")
