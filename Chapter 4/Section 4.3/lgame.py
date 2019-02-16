"""
ID: hsfncd31
LANG: PYTHON3
TASK: lgame
"""
import os
import typing
import string


def main():
    base_filename = 'test' if os.name == 'nt' else 'lgame'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        letter_values = [2, 5, 4, 4, 1, 6, 5, 5, 1, 7, 6, 3, 5, 2, 3, 5, 7, 2, 1, 2, 4, 6, 6, 7, 5, 7]

        def index_of(char: str) -> int:
            return ord(char) - ord('a')

        def value_of_char(char: str) -> int:
            return letter_values[index_of(char)]

        def value_of_word(word: str) -> int:
            return sum(value_of_char(char) for char in word)

        usable_letters = get_line()
        usable_letters_set = set(usable_letters)
        # map the usable letters to 0 ... n - 1, just use list for look up
        usable_letters_id = [None] * len(string.ascii_lowercase)  # type: typing.List[typing.Union[int, None]]
        for i, letter in enumerate(usable_letters_set):
            usable_letters_id[index_of(letter)] = i

        def encode(word: str) -> typing.Union[int, None]:
            """
            encodes a word with its number of letters,
            4 bits per letter(in case of overflow after adding)
            """
            result = 0
            for char in word:
                index = index_of(char)
                if not 0 <= index < len(string.ascii_lowercase):
                    return None
                letter_id = usable_letters_id[index]
                if letter_id is None:
                    return None
                result += 1 << (4 * letter_id)
            return result

        encoded_input = encode(usable_letters)
        # If (encoded_data + complement) & overflow_mask,
        # we can know that some characters appear too many times.
        complement = eval('0x0' + '7' * len(usable_letters_set)) - encoded_input
        overflow_mask = eval('0x0' + '8' * len(usable_letters_set))

        def legal(encoded_data: int) -> bool:
            return not bool((encoded_data + complement) & overflow_mask)

        # [(word, value, encoded_data)]
        viable_words = []
        max_value_so_far = 0
        # [(first_word, second_word_or_empty_string)]
        best_words_so_far = []
        with open('lgame.dict', 'r') as dictionary_file:
            for line in dictionary_file:
                word = line.rstrip('\n')
                encoded_data = encode(word)
                # filter out words that are definitely not possible
                if encoded_data is None or not legal(encoded_data):
                    continue
                value = value_of_word(word)
                if value >= max_value_so_far:
                    if value > max_value_so_far:
                        max_value_so_far = value
                        best_words_so_far.clear()
                    best_words_so_far.append((word, ''))
                viable_words.append((word, value, encoded_data))

        # Enumerate all word pairs, may cost a lot of time.
        for i in range(len(viable_words)):
            for j in range(i, len(viable_words)):
                if legal(viable_words[i][2] + viable_words[j][2]):
                    value = viable_words[i][1] + viable_words[j][1]
                    if value >= max_value_so_far:
                        if value > max_value_so_far:
                            max_value_so_far = value
                            best_words_so_far.clear()
                        best_words_so_far.append((viable_words[i][0], viable_words[j][0]))
        best_words_so_far.sort()

        out_print(max_value_so_far)
        for first_word, second_word in best_words_so_far:
            if second_word == '':
                out_print(first_word)
            else:
                out_print(first_word, second_word)


if __name__ == '__main__':
    main()
