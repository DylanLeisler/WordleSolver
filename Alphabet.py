class Alphabet:
    LIST_OF_CAPITAL_LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    glob_abc = []

    must_have = []

    def __init__(self):
        self.local_abc = self.LIST_OF_CAPITAL_LETTERS.copy()

    def remove_letter(self, c):
        self.local_abc.remove(c.upper())
        self.must_have.append(c.upper())  # the word must include yellow letters

    def correct_letter(self, c):
        self.local_abc = c.upper()
        self.must_have.append(c.upper())

    def add_glob_ban_letter(self, c):
        self.glob_abc.append(c.upper())  # any letter in this list is banned
        self.glob_abc.sort()
