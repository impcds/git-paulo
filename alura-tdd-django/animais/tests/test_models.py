from django.test import TestCase
from animais.models import Animal


class AnimalModelsTestCase(TestCase):

    def setUp(self):
        self.animal = Animal.objects.create(
            nome_animal = 'Leão',
            predador = 'Sim',
            venenoso = 'Não',
            domestico = 'Não'
        )


    def test_animal_cadastrado_com_caracteristicas(self):
        self.assertEqual(self.animal.nome_animal, 'Leão')
