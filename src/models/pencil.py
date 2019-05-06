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

    def edit_on_paper(self, paper, string_to_write, starting_index):
        ending_index = self.__get_ending_index(paper, string_to_write, starting_index)
        new_text_as_list = self.__parse_characters(paper, string_to_write, starting_index, ending_index)
        paper.text = ''.join(new_text_as_list)

    def __parse_characters(self, paper, string_to_write, starting_index, ending_index):
        original_text_as_list = list(paper.text)
        new_text_as_list = []
        j = 0
        for i, char in enumerate(original_text_as_list):
            if i < starting_index or i > ending_index:
                new_text_as_list.append(char)
            else:
                if self.remaining_durability == 0:
                    new_text_as_list.append(' ')
                elif original_text_as_list[i] == ' ':
                    new_text_as_list.append(string_to_write[j])
                    self.remaining_durability -= 1
                    j += 1
                elif original_text_as_list[i] != ' ':
                    new_text_as_list.append('@')
                    self.remaining_durability -= 1
                    j += 1
        return new_text_as_list

    @staticmethod
    def __get_ending_index(paper, string_to_write, starting_index):
        if starting_index + len(string_to_write) <= len(paper.text):
            return (starting_index + len(string_to_write)) - 1
        else:
            difference = (starting_index + len(string_to_write)) - len(paper.text)
            paper.text += ' ' * difference
            return len(paper.text) - 1
