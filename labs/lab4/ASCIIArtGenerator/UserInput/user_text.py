def get_user_text():
    while True:
        text = input("Введіть текст для створення ASCIIArtGenerator-арту: ").strip()
        if text:
            return text
        else:
            print("Текст не може бути порожнім. Будь ласка, введіть текст.")

def get_alignment_choice():
    while True:
        choice = input("Оберіть вирівнювання для арту (left/center/right): ").strip().lower()
        if choice in ["left", "center", "right"]:
            return choice
        else:
            print("Неправильний вибір. Будь ласка, введіть 'left', 'center' або 'right'.")
