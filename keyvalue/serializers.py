from rest_framework import serializers
from .models import TimeUUID
import operator


class TimeUUIDPostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            
            'text',
            'uuid_value',
            'time_date'
        )
        model = TimeUUID



class TimeUUIDGetSerializer(serializers.BaseSerializer):
    
    def to_representation(self,instance):
        
        response ={
            str(instance.time_date):
            instance.uuid_value.hex,
        }

        return response