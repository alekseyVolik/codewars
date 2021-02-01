def hit_the_target(matrix):
    """
    Return True if arrow hit the target else False

    Link: https://www.codewars.com/kata/5ffc226ce1666a002bf023d2/train/python
    """
    return any([('>' in row) and ('x' in row) and (row.index('>') < row.index('x')) for row in matrix])


if __name__ == '__main__':
    pass
