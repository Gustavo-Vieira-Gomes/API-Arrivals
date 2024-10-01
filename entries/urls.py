from django.urls import path
from .views import EntryListView, EntryCreateView, EntryUpdateView, EntryDestroyView


urlpatterns = [
    path('entries/list/', EntryListView.as_view(), name='entries_list'),
    path('entries/create/', EntryCreateView.as_view(), name='entries_create'),
    path('entries/update/<int:pk>/', EntryUpdateView.as_view(), name='entries_update'),
    path('entries/destroy/<int:pk>/', EntryDestroyView.as_view(), name='entries_destroy'),
]