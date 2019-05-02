from src.models.pencil import Pencil


class TestPencil:

    def setup_method(self):
        self.pencil = Pencil(500, 20, 50)

    def test__should_create_new_instance_of_pencil_with_four_basic_properties(self):
        assert self.pencil.maximum_durability == 500
        assert self.pencil.remaining_durability == 500
        assert self.pencil.length == 20
        assert self.pencil.eraser == 50

    def test_sharpen__should_reset_remaining_durability_to_maximum_durability_and_reduce_length_by_one(self):
        self.pencil.remaining_durability = 5
        self.pencil.length = 1

        self.pencil.sharpen()

        assert self.pencil.maximum_durability == 500
        assert self.pencil.length == 0

    def test_sharpen__should_not_reset_remaining_durability_to_maximum_durability_due_to_length_of_zero(self):
        self.pencil.remaining_durability = 5
        self.pencil.length = 0

        self.pencil.sharpen()

        assert self.pencil.remaining_durability == 5
        assert self.pencil.length == 0
