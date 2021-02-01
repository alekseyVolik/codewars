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


if __name__ == '__main__':
    pass
