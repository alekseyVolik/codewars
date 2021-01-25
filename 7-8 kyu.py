def sum_square_even_root_odd(nums):
    # Sum - Square Even, Root Odd
    # https://www.codewars.com/kata/5a4b16435f08299c7000274f/train/python
    return round(sum(num ** (2 if num % 2 == 0 else 0.5) for num in nums), 2)


def hydrate(drink_string):
    # Responsible Drinking
    # https://www.codewars.com/kata/5aee86c5783bb432cd000018/train/python
    total_glass = sum(int(l) for l in drink_string.split() if l.isdigit())
    return f'{total_glass} glass{"es" if total_glass > 1 else ""} of water'


def sum_even_numbers(seq):
    # Sum even numbers
    # https://www.codewars.com/kata/586beb5ba44cfc44ed0006c3/train/python
    return sum(num for num in seq if num % 2 == 0)
