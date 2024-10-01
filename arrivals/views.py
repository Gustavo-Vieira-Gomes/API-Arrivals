from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .models import Arrival
from .serializers import ArrivalSerializer


class ArrivalListView(ListAPIView):
    queryset = Arrival.objects.all()
    serializer_class = ArrivalSerializer


class ArrivalCreateView(CreateAPIView):
    queryset = Arrival.objects.all()
    serializer_class = ArrivalSerializer


class ArrivalUpdateView(UpdateAPIView):
    queryset = Arrival.objects.all()
    serializer_class = ArrivalSerializer


class ArrivalDestroyView(DestroyAPIView):
    queryset = Arrival.objects.all()
    serializer_class = ArrivalSerializer
