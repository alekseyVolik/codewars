# https://www.codewars.com/kata/526989a41034285187000de4/train/python
def ips_between(start, end):
    start, end, result = reversed(start.split(".")), reversed(end.split(".")), 0
    for position, pair in enumerate(zip(start, end)):
        result += (int(pair[1]) - int(pair[0])) * pow(256, position)
    return result


def generate_hashtag(s):
    hashtag = "#" + "".join(map(lambda x: x.capitalize(), s.split())) if s.split() else ''
    return hashtag if hashtag and len(hashtag) <= 140 else False