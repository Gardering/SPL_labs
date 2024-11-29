from labs.lab3.UserInput.user_input import get_non_empty_input

def choose_color():
    colors = ['red', 'green', 'yellow', 'blue']
    print("Доступні кольори:")
    for i, color in enumerate(colors, 1):
        print(f"{i}. {color}")
    choice = int(get_non_empty_input(f"Оберіть колір (1-{len(colors)}): ")) - 1
    return colors[choice]
