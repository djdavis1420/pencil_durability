from mock import Mock

from src.models.pencil import Pencil
from src.models.paper import Paper


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

    def test_erase_from_paper__should_reduce_eraser_durability_by_three_and_erase_first_occurrence_of_string_from_paper(self):
        mock_paper = Mock()
        string_to_erase = 'ain'
        mock_paper.text = 'The rain in Spain falls mainly on the plain.'
        mock_paper.locate_substring.return_value = {'substring_length': 3, 'starting_index': 40, 'ending_index': 42}

        self.pencil.erase_from_paper(mock_paper, string_to_erase)

        assert self.pencil.eraser == 47
        assert mock_paper.text == 'The rain in Spain falls mainly on the pl   .'

    def test_erase_from_paper__should_reduce_eraser_durability_by_three_and_erase_second_occurrence_of_string_from_paper(self):
        mock_paper = Mock()
        string_to_erase = 'ain'
        mock_paper.text = 'The rain in Spain falls mainly on the pl   .'
        mock_paper.locate_substring.return_value = {'substring_length': 3, 'starting_index': 25, 'ending_index': 27}

        self.pencil.erase_from_paper(mock_paper, string_to_erase)

        assert self.pencil.eraser == 47
        assert mock_paper.text == 'The rain in Spain falls m   ly on the pl   .'

    def test_erase_from_paper__should_reduce_eraser_durability_by_three_to_zero_and_partially_erase_string_from_paper_due_to_no_eraser(self):
        self.pencil.eraser = 3
        mock_paper = Mock()
        string_to_erase = 'Spain'
        mock_paper.text = 'The rain in Spain falls mainly on the plain.'
        mock_paper.locate_substring.return_value = {'substring_length': 5, 'starting_index': 12, 'ending_index': 16}

        self.pencil.erase_from_paper(mock_paper, string_to_erase)

        assert self.pencil.eraser == 0
        assert mock_paper.text == 'The rain in Sp    falls mainly on the plain.'

    def test_erase_from_paper__should_reduce_eraser_durability_by_four_and_erase_string_from_paper(self):
        mock_paper = Mock()
        string_to_erase = 'in in'
        mock_paper.text = 'The rain in Spain falls mainly on the plain.'
        mock_paper.locate_substring.return_value = {'substring_length': 5, 'starting_index': 6, 'ending_index': 10}

        self.pencil.erase_from_paper(mock_paper, string_to_erase)

        assert self.pencil.eraser == 46
        assert mock_paper.text == 'The ra      Spain falls mainly on the plain.'
