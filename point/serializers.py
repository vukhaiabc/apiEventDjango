from rest_framework import serializers
from .models import User_point
from user.models import User
class PointUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_point
        fields = '__all__'
    def create(self, validated_data):
        user_point = User_point(**validated_data)
        user = user_point.user
        print(user.user_id)
        if user is not None :
            user.points_balance = validated_data.get('points_balance')
            user.save()
        user_point.save()
        return user_point
