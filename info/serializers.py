from rest_framework import serializers

from info.models import Info



# Passenger Serializer

class InfoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Info

        fields = '__all__'