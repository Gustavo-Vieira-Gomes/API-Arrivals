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
        
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        time_parts = ret['arrival_time'].split('T')
        date = '-'.join(time_parts[0].split('-')[::-1])
        time = ':'.join(time_parts[1].split('.')[0].split(':')[::-1])
        ret['arrival_time'] = ' '.join([date, time])
        return ret

class AthleteSerializer(serializers.Serializer):
    vest_number = serializers.IntegerField()
    position = serializers.CharField()
    name = serializers.CharField()
    time = serializers.CharField()



class CategorySerializer(serializers.Serializer):
    category = serializers.CharField()
    athletes = AthleteSerializer(many=True)
