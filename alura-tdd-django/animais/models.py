from django.db import models


class Animal(models.Model):
    nome_animal = models.CharField(max_length=100)
    predador = models.CharField(max_length=20)
    venenoso = models.CharField(max_length=20)
    domestico = models.CharField(max_length=20)


    def __str__(self):
        return self.nome_animal
