from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Arrival
from .serializers import ArrivalSerializer, AthleteSerializer, CategorySerializer
from entries.models import Entry
from .signals import build_competitor_name, calculate_competing_time


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


class GetPodiumView(APIView):

    def get(self, request, *args, **kwargs):
        arrivals = Arrival.objects.all()
        result = {}
        
        for arrival in arrivals:

            category_data = Entry.objects.get(vest_number=arrival.vest_number)
            athlete_name = build_competitor_name(category_data)
            boat_category = category_data.boat_class
            sex_category = category_data.sex_category
            age_category = category_data.age_category
            category_name = f'{boat_category.capitalize()} {sex_category.capitalize()} {age_category.title()}'
            start_category = 'OC6' if boat_category == 'OC6' or boat_category == 'V6' else 'JUNIORES' if sex_category == 'JUNIORES' else 'GERAL'

            athlete_time = calculate_competing_time(arrival.arrival_time, boat_category)

            if category_name not in result.keys():
                result[category_name] = []
                position = '1º'
            
            position = f'{len(result[category_name]) + 1}º'

            athlete_data = {
                'position': position,
                'name': athlete_name,
                'time': athlete_time
            }

            result[category_name].append(athlete_data)

            serialized_data = [
                {'category': category,
                 'athletes': AthleteSerializer(athletes, many=True).data
                }
                for category, athletes in result.items()
            ]
        serializer = CategorySerializer(serialized_data, many=True)
        return Response(serializer.data)
