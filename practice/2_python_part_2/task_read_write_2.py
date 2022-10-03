"""
Use function 'generate_words' to generate random words.
Write them to a new file encoded in UTF-8. Separator - '\n'.
Write second file encoded in CP1252, reverse words order. Separator - ','.

Example:
    Input: ['abc', 'def', 'xyz']

    Output:
        file1.txt (content: "abc\ndef\nxyz", encoding: UTF-8)
        file2.txt (content: "xyz,def,abc", encoding: CP1252)
"""


def generate_words(n=20):
    import string
    import random

    words = list()
    for _ in range(n):
        word = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
        words.append(word)

    return words


def read_write_2(file1_path, file2_path, n):
    generated_words = generate_words(n)

    with open(file1_path, 'w', encoding='UTF-8') as file1:
        file1.write('\n'.join(generated_words))

    with open(file2_path, 'w', encoding='CP1252') as file2:
        file2.write(','.join(reversed(generated_words)))


read_write_2('file1.txt', 'file2.txt', 3)
