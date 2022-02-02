gracz1 = input("Podaj nazwe: ")
gracz2 = input("Podaj nazwe: ")

gracz1_wybor = input("%s, Co wybierasz? Kamień, Papier, Nożyczki?" % gracz1)
gracz2_wybor = input("%s, Co wybierasz? Kamień, Papier, Nożyczki?" % gracz2)


def ruchy(gracz1, gracz2):
    if gracz1 == gracz2:
        return ("Remis")
    elif gracz1 == 'Kamień':
        if gracz2 == 'Nożyczki':
            return ("Kamień wygrywa")
        else:
            return ("Papier wygrywa")
    elif gracz1 == 'Nożyczki':
        if gracz2 == 'Papier':
            return ("Nożyczki wygrały")
        else:
            return ("Kamień wygrywa")
    elif gracz1 == 'Papier':
        if gracz2 == 'Kamień':
            return ("Papier wygrywa")
        else:
            return ("Nożyczki wygrały")
    else:
        return ("Błąd, złe dane. Spróbuj ponownie.")

print(ruchy(gracz1_wybor, gracz2_wybor))