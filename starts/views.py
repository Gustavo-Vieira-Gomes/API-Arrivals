from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .models import Start
from .serializers import StartSerializer


class StartListView(ListAPIView):
    queryset = Start.objects.all()
    serializer_class = StartSerializer


class StartCreateView(CreateAPIView):
    queryset = Start.objects.all()
    serializer_class = StartSerializer


class StartUpdateView(UpdateAPIView):
    queryset = Start.objects.all()
    serializer_class = StartSerializer

class StartDestroyView(DestroyAPIView):
    queryset = Start.objects.all()
    serializer_class = StartSerializer
