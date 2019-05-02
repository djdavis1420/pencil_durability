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
