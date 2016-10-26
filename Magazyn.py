# program wyswietla stan magazynu wraz z cena, nastepnie wykonuje zamowienie online
# sprawdza czy produkt jest dostepny na magazynie i aktualizuje stan magazynu
# na koniec zwraca kwote jaka mamy zaplacic 


lista_zakupow = ["jablko", 'gruszka', 'cytryna', "banan", "banan", "arbuz" ]
asortyment_cena = {
"jablko": 2,
"gruszka": 5,
"banan": 3,
"cytryna": 11,
"arbuz": 1.5,
}

stan_magazyn = {
"jablko": 10,
"gruszka": 11,
"banan": 120,
"cytryna": 6,
"arbuz": 0, 
}
zapowiedz = "witaj ponizej jest lista produktow dostepnych w naszym magazynie wraz z cenami"
print(zapowiedz.upper())
for klucz in asortyment_cena: # petla wyswietlajaca stan magazynu
    print(klucz)
    print("cena: %s" % asortyment_cena[klucz])
    print("stan: %s" % stan_magazyn[klucz])
calosc = 0
for klucz in asortyment_cena: # petla wyswietlajaca ceny do produktow
    mix = asortyment_cena[klucz] * stan_magazyn[klucz]           
    calosc = calosc + mix
print("wartosc: ", calosc)
print('________________')
print("stan magazyny przed: ", stan_magazyn) 
print('________________')
print("zamowienie sklada sie z:", len(lista_zakupow), lista_zakupow)

def zamowienie(produkty): # funkcja wraz z petla sprawdzajaca stan magazynu i odejmujaca po 1 produkcie
    calosc_zamowienia = 0
    for produkt in produkty:
        if stan_magazyn[produkt] == 0:
            print([produkt], "BRAK")
        if stan_magazyn[produkt] > 0 :
            calosc_zamowienia = calosc_zamowienia + asortyment_cena[produkt]
            stan_magazyn[produkt] = stan_magazyn[produkt] - 1
    return calosc_zamowienia
print("kwota do zaplaty", zamowienie(lista_zakupow)) 
print('________________')
print("stan magazynu po: ", stan_magazyn)

