from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .models import Car
from .serializers import CarIdentificationSerializer


class CarIdentificationAPIListView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarIdentificationSerializer


class CarIdentificationRetriveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarIdentificationSerializer
