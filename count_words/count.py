import re


def count_words(input: str) -> dict:
    result = {}
    for word in input.split():
        test_word = re.sub(r'^[^a-zA-Z0-9]|[^a-zA-Z0-9]$', '', word.lower())
        if test_word in result:
            result[test_word] += 1
        else:
            result[test_word] = 1
    return result
