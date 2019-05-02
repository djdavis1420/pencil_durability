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
