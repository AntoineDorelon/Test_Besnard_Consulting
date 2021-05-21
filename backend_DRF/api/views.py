from rest_framework import viewsets
from .models import AgileValues, AgilePrinciples
from .serializers import ValuesSerializer, PrinciplesSerializer


class ValuesViewset(viewsets.ModelViewSet):
    queryset = AgileValues.objects.all()
    serializer_class = ValuesSerializer


class PrinciplesViewset(viewsets.ModelViewSet):
    queryset = AgilePrinciples.objects.all()
    serializer_class = PrinciplesSerializer

