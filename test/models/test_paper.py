from src.models.paper import Paper


class TestPaper:

    def setup_method(self):
        self.paper = Paper()

    def test__should_create_new_instance_of_paper_with_text_property(self):
        assert self.paper.text == ''
