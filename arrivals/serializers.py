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