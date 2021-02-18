def hit_the_target(matrix):
    """
    Return True if arrow hit the target else False

    Link: https://www.codewars.com/kata/5ffc226ce1666a002bf023d2/train/python
    """
    return any([('>' in row) and ('x' in row) and (row.index('>') < row.index('x')) for row in matrix])


def alphabet_war(fight):
    """
    Return winner side of fight

    Link: https://www.codewars.com/kata/59377c53e66267c8f6000027/train/python
    """
    ls = ['s', 'b', 'p', 'w']
    rs = ['z', 'd', 'q', 'm']
    lp = sum([pos * fight.count(letter) for (pos, letter) in enumerate(ls, 1)])
    rp = sum([pos * fight.count(letter) for (pos, letter) in enumerate(rs, 1)])
    return "Right side wins!" if rp > lp else ("Left side wins!" if rp < lp else "Let's fight again!")


def calc(string):
    """
    Transform string to number and calculate diff between number and number with replace 7 to 1

    link: https://www.codewars.com/kata/57f75cc397d62fc93d000059/train/python
    """
    return sum([int(num) - 1 for num in ''.join([str(ord(letter)) for letter in string]) if num == '7'])


def move_ten(st):
    """
    Shift each letter to ten position to right

    link: https://www.codewars.com/kata/57cf50a7eca2603de0000090/train/python
    """
    return ''.join([chr(97 + (ord(letter) - 97 + 10) % 26) for letter in st])


def max_re_digit(num):
    """
    Rearrange input digit to get maximum number

    link: https://www.codewars.com/kata/563700da1ac8be8f1e0000dc/train/python
    """
    return int(''.join(sorted(str(num), reverse=True))) if (99 < num < 1000) else None


def flatten_me(lst):
    """
    Takes a single list as an argument and returns a flattened list

    link: https://www.codewars.com/kata/55a5bef147d6be698b0000cd/train/python
    """
    smooth_list = []
    [smooth_list.extend(item) if isinstance(item, list) else smooth_list.append(item) for item in lst]
    return smooth_list


def switcheroo(string):
    """
    Switch a to b and b to a in input string

    link: https://www.codewars.com/kata/57f759bb664021a30300007d/train/python
    """
    return ''.join(['b' if ch == 'a' else ('a' if ch == 'b' else ch) for ch in string])


if __name__ == '__main__':
    pass
