class Pencil:
    def __init__(self, durability, length, eraser):
        self.maximum_durability = durability
        self.remaining_durability = durability
        self.length = length
        self.eraser = eraser

    def sharpen(self):
        if self.length > 0:
            self.remaining_durability = self.maximum_durability
            self.length -= 1

    def write_to_paper(self, paper, string_to_write):
        for char in string_to_write:
            if char == ' ' or char == '\n':
                paper.write(char)
            elif self.remaining_durability >= 2 and char.isupper():
                paper.write(char)
                self.remaining_durability -= 2
            elif self.remaining_durability >= 1 and char.islower():
                paper.write(char)
                self.remaining_durability -= 1
            else:
                paper.write(' ')

    def erase_from_paper(self, paper, string_to_erase):
        substring_information = paper.locate_substring(string_to_erase)
        text_before_string_to_erase = paper.text[:substring_information['starting_index']:]
        text_after_string_to_erase = paper.text[substring_information['ending_index'] + 1::]
        string_being_erased = ''

        for char in string_to_erase[::-1]:
            if self.eraser > 0 and char != ' ':
                string_being_erased = string_being_erased + ' '
                self.eraser -= 1
            elif self.eraser > 0 and char == ' ':
                string_being_erased = string_being_erased + ' '
            else:
                string_being_erased = char + string_being_erased

        new_text = text_before_string_to_erase + string_being_erased + text_after_string_to_erase
        paper.text = new_text
