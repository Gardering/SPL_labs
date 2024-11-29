class UserInput:
    @staticmethod
    def input_non_empty(prompt, valid_choices=None):
        while True:
            user_input = input(prompt).strip()
            if not user_input:
                print("Введення не може бути порожнім. Спробуйте ще раз.")
            elif valid_choices and user_input.lower() not in valid_choices:
                print(f"Невірний вибір! Виберіть один з доступних варіантів: {', '.join(valid_choices)}.")
            else:
                return user_input.lower()
