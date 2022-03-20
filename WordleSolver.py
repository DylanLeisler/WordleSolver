from Alphabet import Alphabet as col
from tabulate import tabulate

# TODO refactor

TOTAL_GUESSES = 5

col1 = col()
col2 = col()
col3 = col()
col4 = col()
col5 = col()

col_list = [col1, col2, col3, col4, col5]


def update_column(column: col, inc: int):
    selection = input(
        "Update col{0}?\nENTER 1 TO BAN LETTER FROM COL\n"
        "ENTER 2 TO BAN LETTER FROM WORD\nENTER 3 TO ENTER COLUMNS CONFIRMED LETTER\n"
        "ENTER 0 TO PASS\nSELECTION: ".format(inc)
    )
    selection = int(selection)

    if not selection:
        pass
    elif selection == 1 or selection == 2:
        letter = input("Enter letter to ban: ")
        if selection == 1:
            column.remove_letter(letter)
        else:
            column.add_glob_ban_letter(letter)
    else:
        letter = input("Enter letter to lock in this col: ")
        column.correct_letter(letter)


def extract_words(fh: str) -> list:
    with open(fh, 'r') as wo:
        return [str(line).strip().upper() for line in wo.readlines()]


def filter_words(all_cols: [], word_list):
    for i, col in enumerate(all_cols, 0):
        word_list = [word for word in word_list if word[i] in col.local_abc]
    for letter in all_cols[0].glob_abc:
        word_list = [word for word in word_list if letter not in word]
    for letter in all_cols[0].must_have:
        word_list = [word for word in word_list if letter in word]
    return word_list


def render_options(words):
    print(tabulate(words))


word_list = extract_words('word_options.txt')
for interval in range(TOTAL_GUESSES):
    for i, col in enumerate(col_list, 1):
        update_column(col, i)
    render_options(
        filter_words(
            col_list, word_list
        )
    )



