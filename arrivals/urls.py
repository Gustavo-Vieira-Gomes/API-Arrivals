from django.urls import path
from .views import ArrivalListView, ArrivalCreateView, ArrivalDestroyView, ArrivalUpdateView


urlpatterns = [
    path('arrivals/list/', ArrivalListView.as_view(), name='arrivals_list'),
    path('arrivals/create/', ArrivalCreateView.as_view(), name='arrivals_create'),
    path('arrivals/update/<int:pk>/', ArrivalUpdateView.as_view(), name='arrivals_update'),
    path('arrivals/destroy/<int:pk>/', ArrivalDestroyView.as_view(), name='arrivals_destroy'),
]