# Task: https://www.codewars.com/kata/5a4e3782880385ba68000018/train/python
def balanced_num(number):
    number = list(map(int, str(number)))
    middle = (len(number)-1)
    if middle > 1:
        return "Balanced" if (sum(number[:middle//2]) == sum(number[round(middle/2) + 1:])) else "Not Balanced"
    return "Balanced"
