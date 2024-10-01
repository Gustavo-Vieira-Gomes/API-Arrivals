from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .models import Entry
from .serializers import EntrySerializer


class EntryListView(ListAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class EntryCreateView(CreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class EntryUpdateView(UpdateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

class EntryDestroyView(DestroyAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
