class Paper:
    def __init__(self):
        self.text = ''

    def write(self, character):
        self.text += character

    def locate_substring(self, string_to_erase):
        substring_information = {}
        substring_information['substring_length'] = len(string_to_erase)
        substring_information['starting_index'] = self.text.rindex(string_to_erase)
        return substring_information
