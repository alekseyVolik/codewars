def break_camel_casing(text):
    """
    Break up camel casing string with space between words

    link: https://www.codewars.com/kata/5208f99aee097e6552000148/train/python
    """
    return ''.join([' ' + letter if letter.isupper() else letter for letter in text])


def calc(string):
    """
    Transform string to number and calculate diff between number and number with replace 7 to 1

    link: https://www.codewars.com/kata/57f75cc397d62fc93d000059/train/python
    """
    return sum([int(num) - 1 for num in ''.join([str(ord(letter)) for letter in string]) if num == '7'])


if __name__ == '__main__':
    pass
