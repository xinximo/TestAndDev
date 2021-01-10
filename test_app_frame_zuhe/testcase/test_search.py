from test_app_frame_zuhe.base_page import BasePage
from test_app_frame_zuhe.page.main import Main


class TestSearch:
    def setup(self):
        basepage = BasePage()
        self.app = Main(basepage)

    def test_search(self):
        self.app.goto_market().goto_search().search()
