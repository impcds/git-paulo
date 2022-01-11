from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet
from animais.models import Animal


class IndexViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.animal = Animal.objects.create(
            nome_animal = "Canguru",
            predador = "Não",
            venenoso = "Não",
            domestico = "Não"
        )


    def test_index_view_retorna_caracteristias_do_animal(self):
        """teste que verifica se a index retorna as caracteristicas dos animais"""

        response = self.client.get('/',
                                   {'buscar': 'canguru'},)
        caracteristica_animal_pesquisado = response.context['caracteristicas']
        self.assertEqual(caracteristica_animal_pesquisado[0].nome_animal, 'Canguru')
        self.assertIs(type(response.context['caracteristicas']), QuerySet)
