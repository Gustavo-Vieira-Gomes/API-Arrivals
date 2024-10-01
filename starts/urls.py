from django.urls import path
from .views import StartListView, StartCreateView, StartUpdateView, StartDestroyView


urlpatterns = [
    path('starts/list/', StartListView.as_view(), name='starts_list'),
    path('starts/create/', StartCreateView.as_view(), name='starts_create'),
    path('starts/update/<int:pk>/', StartUpdateView.as_view(), name='starts_update'),
    path('starts/destroy/<int:pk>/', StartDestroyView.as_view(), name='starts_destroy'),
]
