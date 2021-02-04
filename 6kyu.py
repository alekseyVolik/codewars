def break_camel_casing(text):
    """
    Break up camel casing string with space between words

    link: https://www.codewars.com/kata/5208f99aee097e6552000148/train/python
    """
    return ''.join([' ' + letter if letter.isupper() else letter for letter in text])


def json_attr(filepath):
    """
    Set attribute from json to class

    link: https://www.codewars.com/kata/55b0fb65e1227b17d60000dc/train/python
    """
    import json
    json_file = open(filepath, 'r')
    json_dict = json.load(json_file)
    json_file.close()

    def set_attr(some_class):
        for attr, value in json_dict.items():
            setattr(some_class, attr, value)
        return some_class

    return set_attr


if __name__ == '__main__':
    pass
