from django.db.models import fields
from rest_framework import serializers
from .models import *



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' 

    def validate(self, data):  # custom data validator
        for a in  data['mobile_no']:
            if a.isnumeric() is False:
                raise serializers.ValidationError({"error":"Enter a valid number."})
        if len(data['mobile_no'])<10 or len(data['mobile_no'])>10:
            raise serializers.ValidationError({"error":"Enter a valid number."})
        else:
            return data