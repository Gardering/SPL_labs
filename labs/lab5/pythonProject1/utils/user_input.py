def get_shape_type():
    shape_type = input("Яку фігуру ви хочете побудувати? (cube/pyramid): ").strip().lower()
    while shape_type not in ["cube", "pyramid"]:
        print("Невірний вибір. Будь ласка, виберіть 'cube' або 'pyramid'.")
        shape_type = input("Яку фігуру ви хочете побудувати? (cube/pyramid): ").strip().lower()
    return shape_type

def get_scale_factor():
    while True:
        scale_factor = input("Введіть масштаб фігури (наприклад, 2 для збільшення, 0.5 для зменшення або '1' для стандартного розміру, 'exit' для виходу): ")
        if scale_factor.lower() == 'exit':
            return scale_factor
        try:
            scale_factor = float(scale_factor)
            if scale_factor <= 0:
                print("Будь ласка, введіть позитивне число для масштабу.")
                continue
            return scale_factor
        except ValueError:
            print("Будь ласка, введіть дійсне число.")

def get_rotation_direction():
    direction = input("Введіть напрямок обертання (top, bottom, left, right, none для пропуску): ").lower()
    return direction

def get_color_choice(colors):
    color_choice = input("Введіть колір фігури або 'none' для пропуску: ").lower()
    if color_choice in colors:
        return color_choice
    return None

def get_save_prompt():
    save_prompt = input("Бажаєте зберегти фігуру у файл? (y/n): ").lower()
    return save_prompt

def get_filename():
    filename = input("Введіть назву файлу (з розширенням .txt): ")
    return filename
