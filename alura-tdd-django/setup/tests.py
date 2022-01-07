from django.test import LiveServerTestCase
from selenium import webdriver


class AnimaisTestCase(LiveServerTestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome('C:\\Users\\Paulo César\\p\git-paulo\\alura-tdd-django\\chromedriver.exe')

    def tearDown(self):
        self.browser.quit()

    def test_verifica_se_a_janela_do_browser_e_aberta(self):
        self.browser.get(self.live_server_url)

    def test_deu_ruim(self):
        '''exemplo de teste qeu falha'''
        self.fail('Deu ruim! ou deu bom? ')
