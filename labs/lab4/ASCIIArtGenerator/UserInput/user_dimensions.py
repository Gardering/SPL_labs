def get_dimensions():
    while True:
        try:
            width = int(input("Введіть ширину арту (від 10 до 100): "))
            height = int(input("Введіть висоту арту (від 1 до 50): "))
            if 10 <= width <= 100 and 1 <= height <= 50:
                return width, height
            else:
                print("Ширина повинна бути від 10 до 100, а висота від 1 до 50.")
        except ValueError:
            print("Будь ласка, введіть ціле число для ширини і висоти.")
