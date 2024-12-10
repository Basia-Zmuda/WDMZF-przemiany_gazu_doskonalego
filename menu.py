from wykresy import show_info

#Funckja do wyświetlania menu
def show_menu():
    print("Wybierz rodzaj przemiany termodynamicznej:")
    print("1. Izotermiczna")
    print("2. Izobaryczna")
    print("3. Izochoryczna")

    pytaj_o_liczbe = True
    while(pytaj_o_liczbe):
        # Pobranie wyboru użytkownika
        choice = input("Podaj numer przemiany (1/2/3): ")
        if choice == '1' or choice == '2' or choice == '3':
            pytaj_o_liczbe = False


    if choice == "1":
        title = "Przemiana Izotermiczna"
        content = ("- Temperatura jest stała (T = const).\n"
                   "- Zmiana ciśnienia i objętości jest opisana równaniem:\n"
                   "  P * V = const\n"
                   "- Praca: W = nRT * ln(V2/V1)\n"
                   "- Ciepło dostarczone: Q = W")
    elif choice == "2":
        title = "Przemiana Izobaryczna"
        content = ("- Ciśnienie jest stałe (P = const).\n"
                   "- Zmiana objętości i temperatury jest opisana równaniem:\n"
                   "  V / T = const\n"
                   "- Praca: W = P * ΔV\n"
                   "- Ciepło dostarczone: Q = n * Cp * ΔT")
    elif choice == "3":
        title = "Przemiana Izochoryczna"
        content = ("- Objętość jest stała (V = const).\n"
                   "- Zmiana ciśnienia i temperatury jest opisana równaniem:\n"
                   "  P / T = const\n"
                   "- Praca: W = 0 (brak zmiany objętości)\n"
                   "- Ciepło dostarczone: Q = n * Cv * ΔT")
    else:
        print("Nieprawidłowy wybór!")
        return

    # Wyświetlenie informacji w okienku
    show_info(title, content)
