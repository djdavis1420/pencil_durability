from src.models.paper import Paper


class TestPaper:

    def setup_method(self):
        self.paper = Paper()

    def test__should_create_new_instance_of_paper_with_text_property(self):
        assert self.paper.text == ''

    def test_write__should_write_capital_a_to_unpopulated_text_property(self):
        character = 'A'

        self.paper.write(character)

        assert self.paper.text == 'A'

    def test_write__should_write_blank_space_to_populated_text_property(self):
        self.paper.text = 'A'
        character = ' '

        self.paper.write(character)

        assert self.paper.text == 'A '

    def test_write__should_write_capital_z_to_populated_text_property(self):
        self.paper.text = 'A '
        character = 'Z'

        self.paper.write(character)

        assert self.paper.text == 'A Z'

    def test_locate_substring__should_return_dictionary_with_substring_information_for_last_occurrence_in_populated_text_property(self):
        self.paper.text = 'The rain in Spain falls mainly on the plain'
        string_to_erase = 'ain'

        actual = self.paper.locate_substring(string_to_erase)

        assert actual == {'substring_length': 3, 'starting_index': 40, 'ending_index': 42}
