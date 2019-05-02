from src.models.pencil import Pencil


class TestPencil:

    def setup_method(self):
        self.pencil = Pencil(500, 20, 50)

    def test__should_create_new_instance_of_pencil_with_four_basic_properties(self):
        assert self.pencil.maximum_durability == 500
        assert self.pencil.remaining_durability == 500
        assert self.pencil.length == 20
        assert self.pencil.eraser == 50
