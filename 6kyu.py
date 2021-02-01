def break_camel_casing(text):
    """
    Break up camel casing string with space between words

    link: https://www.codewars.com/kata/5208f99aee097e6552000148/train/python
    """
    return ''.join([' ' + letter if letter.isupper() else letter for letter in text])


if __name__ == '__main__':
    pass
