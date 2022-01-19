from rest_framework import serializers
from clientes.models import Cliente
from clientes.validator import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):

        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({"cpf": "CPF inválido."})

        if nome_valido(data['nome']):
            raise serializers.ValidationError({"nome": "Não insira números aqui."})

        if not rg_valido(data['rg']):
            raise serializers.ValidationError({"rg": "O rg é formado por 9 dígitos."})

        if not celular_valido(data['celular']):
            raise serializers.ValidationError({"celular": "Número inválido. Siga o padrão (xx xxxxx-xxxx)"})

        return data
