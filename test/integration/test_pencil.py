from src.models.paper import Paper
from src.models.pencil import Pencil


class TestIntegration:

    def setup_method(self):
        self.pencil = Pencil(500, 20, 50)
        self.paper = Paper()

    def test_edit_on_paper__should_replace_word_rain_with_four_at_symbols_instead_of_word_snow(self):
        starting_index = 4
        string_to_write = 'snow'
        self.paper.text = 'The rain in Spain falls mainly on the plain.'

        self.pencil.edit_on_paper(self.paper, string_to_write, starting_index)

        assert self.pencil.remaining_durability == 496
        assert self.paper.text == 'The @@@@ in Spain falls mainly on the plain.'

    def test_edit_on_paper__should_replace_four_blank_spaces_where_word_rain_had_been_erased_with_word_snow(self):
        starting_index = 4
        string_to_write = 'snow'
        self.paper.text = 'The      in Spain falls mainly on the plain.'

        self.pencil.edit_on_paper(self.paper, string_to_write, starting_index)

        assert self.pencil.remaining_durability == 496
        assert self.paper.text == 'The snow in Spain falls mainly on the plain.'

    def test_edit_on_paper__should_write_five_letters_and_two_at_symbols_starting_where_word_rain_had_been_erased(self):
        starting_index = 4
        string_to_write = 'snowing'
        self.paper.text = 'The      in Spain falls mainly on the plain.'

        self.pencil.edit_on_paper(self.paper, string_to_write, starting_index)

        assert self.pencil.remaining_durability == 493
        assert self.paper.text == 'The snowi@@ Spain falls mainly on the plain.'

    def test_edit_on_paper__should_overwrite_word_rain_and_subsequent_characters_with_word_precipitation(self):
        starting_index = 4
        string_to_write = 'precipitation'
        self.paper.text = 'The rain in Spain falls mainly on the plain.'

        self.pencil.edit_on_paper(self.paper, string_to_write, starting_index)

        assert self.pencil.remaining_durability == 487
        assert self.paper.text == 'The @@@@i@@t@@@@@ falls mainly on the plain.'

    def test_edit_on_paper__should_write_word_fog_to_blank_spaces_left_by_erased_word_rain(self):
        starting_index = 4
        string_to_write = 'fog'
        self.paper.text = 'The      in Spain falls mainly on the plain.'

        self.pencil.edit_on_paper(self.paper, string_to_write, starting_index)

        assert self.pencil.remaining_durability == 497
        assert self.paper.text == 'The fog  in Spain falls mainly on the plain.'

    def test_edit_on_paper__should_write_word_grassland_over_word_plain_and_extend_full_text(self):
        starting_index = 38
        string_to_write = 'grassland.'
        self.paper.text = 'The rain in Spain falls mainly on the plain.'

        self.pencil.edit_on_paper(self.paper, string_to_write, starting_index)

        assert self.pencil.remaining_durability == 490
        assert self.paper.text == 'The rain in Spain falls mainly on the @@@@@@and.'

    def test_edit_on_paper__should_write_partial_word_snow_on_spaces_left_by_word_rain(self):
        self.pencil.remaining_durability = 2
        starting_index = 4
        string_to_write = 'snow'
        self.paper.text = 'The      in Spain falls mainly on the plain.'

        self.pencil.edit_on_paper(self.paper, string_to_write, starting_index)

        assert self.pencil.remaining_durability == 0
        assert self.paper.text == 'The sn   in Spain falls mainly on the plain.'
