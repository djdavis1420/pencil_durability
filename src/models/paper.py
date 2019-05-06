class Paper:
    def __init__(self):
        self.text = ''

    def write(self, character):
        self.text += character

    def locate_substring(self, string_to_erase):
        substring_information = {}
        substring_information['substring_length'] = len(string_to_erase)
        substring_information['starting_index'] = self.text.rindex(string_to_erase)
        substring_information['ending_index'] = (substring_information['starting_index'] + substring_information['substring_length']) - 1
        return substring_information

    def edit(self, pencil, string_to_write, starting_index, ending_index):
        original_text_as_list = list(self.text)
        new_text_as_list = []
        j = 0
        for i, char in enumerate(original_text_as_list):
            if i < starting_index or i > ending_index:
                new_text_as_list.append(char)
            else:
                if pencil.remaining_durability == 0:
                    new_text_as_list.append(' ')
                elif original_text_as_list[i] == ' ':
                    new_text_as_list.append(string_to_write[j])
                    pencil.remaining_durability -= 1
                    j += 1
                elif original_text_as_list[i] != ' ':
                    new_text_as_list.append('@')
                    pencil.remaining_durability -= 1
                    j += 1
        return new_text_as_list
