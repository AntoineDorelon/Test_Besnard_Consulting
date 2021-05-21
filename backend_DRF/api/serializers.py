from .models import AgileValues, AgilePrinciples
from rest_framework import serializers


# need to put a maximum of 4 values
class ValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgileValues
        fields = ['id', 'title', ]


# need to put a maximum of 4 values
class PrinciplesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgilePrinciples
        fields = ['id', 'description', ]
