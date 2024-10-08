from django.urls import path
from .views import CarIdentificationAPIListView, CarIdentificationRetriveUpdateDestroyAPIView


urlpatterns = [
    path('cars/list/', CarIdentificationAPIListView.as_view(), name='cars_licence_plate'),
    path('cars/detail/<int:pk>/', CarIdentificationRetriveUpdateDestroyAPIView.as_view(), name='cars_update_destroy'),
]