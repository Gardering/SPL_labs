def get_symbol_set():
    while True:
        symbol = input("Введіть символ для створення арту (@, #, *, .): ").strip()
        if symbol:
            return symbol
        else:
            print("Введіть символ для створення арту.")
