from rest_framework import serializers
from .models import Arrival
from entries.models import Entry


class ArrivalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Arrival
        fields = '__all__'

    def validate_vest_number(self, value):
        entries = Entry.objects.all()

        if entries.filter(vest_number=value):
            return value
        else:
            raise serializers.ValidationError('Não existe competidor inscrito com este número de colete!')


class AthleteSerializer(serializers.Serializer):
    position = serializers.CharField()
    name = serializers.CharField()
    time = serializers.CharField()


class CategorySerializer(serializers.Serializer):
    category = serializers.CharField()
    athletes = AthleteSerializer(many=True)
