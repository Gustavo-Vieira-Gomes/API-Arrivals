from rest_framework import serializers
from .models import Start


class StartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Start
        fields = '__all__'

    def get_start_time(self, obj):
        return obj.start_time.strftime('%d/%m%Y %H:%M%S')