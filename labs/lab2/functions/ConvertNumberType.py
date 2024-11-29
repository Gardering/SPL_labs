def ConvertNumberType(nums):
    nums = nums.replace(',', '.')
    try:
        number = float(nums)
        if number.is_integer():
            return int(number)
        return number
    except ValueError:
        raise ValueError(f"Невірне число: '{nums}'")

def ConvertNumberType(nums):
    nums = nums.replace(',', '.')
    try:
        number = float(nums)
        if number.is_integer():
            return int(number)
        return number
    except ValueError:
        raise ValueError(f"Недійсне число: '{nums}'. Будь ласка, введіть дійсне число.")
