from django.test import LiveServerTestCase
from selenium import webdriver


class AnimaisTestCase(LiveServerTestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome('C:\\Users\\Paulo César\\p\git-paulo\\alura-tdd-django\\chromedriver.exe')

    def tearDown(self):
        self.browser.quit()

    def test_buscando_um_novo_animal(self):
        """teste se um usuário encontra um animal pesquisando"""

        home_page = self.browser.get(self.live_server_url + '/')

        brand_element = self.browser.find_element_by_css_selector('.navbar')
        self.assertEqual('Busca Animal', brand_element.text)

