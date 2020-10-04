import re
from itertools import product as pr


def most_common(line):
    words = line.split(' ')
    reg = re.compile('[^a-zA-Zа-яА-Я]')
    words_filtered = []
    for word in words:
        word_new = re.sub(reg, '', word)
        if word_new != '':
            words_filtered.append(word_new)

    word_index = {}
    let_index = {}

    for word in words_filtered:
        if word in word_index:
            word_index[word] += 1
        else:
            word_index[word] = 1
        for letter in word:
            if letter in let_index:
                let_index[letter] += 1
            else:
                let_index[letter] = 1

    max_word = max(word_index.values())
    print("Most common word(s):", [i for i, j in word_index.items() if j == max_word], "with", max_word, "occurences")
    max_let = max(let_index.values())
    print("Most common letter(s):", [i for i, j in let_index.items() if j == max_let], "with", max_let, "occurences")


def palindromes(workspace, len):
    result = []
    for i in range(len+1):
        for product in pr(alphabet, repeat=((i + 1) // 2)):
            if i % 2:
                result.append(''.join(product) + ''.join(product[-2::-1]))
            else:
                pass
                result.append(''.join(product) + ''.join(product[::-1]))
    return result


# if __name__ == "main":
line = 'Стандартная библиотека: 1. Написать код, который помогает выяснить на каких размерах словарь перевыделяет память 2. Написать функцию, которая для полученного текста возвращает самое популярное слово, самую популярную букву и среднее количество вхождений буквы в слово. 3. Написать функцию, которая принимает на вход алфавит и выдаёт все палиндром этого алфавита не больше указанной длины'
most_common(line)

alphabet = 'abcdefgh|'
print(palindromes(alphabet, 4))
