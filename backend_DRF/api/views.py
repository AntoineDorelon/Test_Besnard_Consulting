from rest_framework import viewsets, status, mixins
from .models import AgileValues, AgilePrinciples
from .serializers import ValuesSerializer, PrinciplesSerializer
from rest_framework.response import Response


class ValuesViewset(viewsets.ModelViewSet):
    queryset = AgileValues.objects.all()
    serializer_class = ValuesSerializer

    def create(self, request, *args, **kwargs):
        number_of_values = AgileValues.objects.all().count()
        if number_of_values < 4:
            return super().create(request, *args, **kwargs)
        else:
            response = {'message': 'You cant create more than 4 values'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class PrinciplesViewset(viewsets.ModelViewSet):
    queryset = AgilePrinciples.objects.all()
    serializer_class = PrinciplesSerializer

    def create(self, request, *args, **kwargs):
        numbers_of_principles = AgilePrinciples.objects.all().count()
        if numbers_of_principles < 12:
            return super().create(request, *args, **kwargs)
        else:
            response = {'message': 'You cant create more than 12 principles'}
            return Response(response, status.HTTP_400_BAD_REQUEST)



