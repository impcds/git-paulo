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

        buscar_animal_input = self.browser.find_element_by_id('buscar-animal')
        self.assertEqual(buscar_animal_input.get_attribute('placeholder'), 'Exemplo: leão')

        buscar_animal_input.send_keys('leão')
        self.browser.find_element_by_css_selector('form button').click()

        caracteristicas = self.browser.find_elements_by_css_selector('.result-description')
        self.assertGreater(len(caracteristicas), 3)
