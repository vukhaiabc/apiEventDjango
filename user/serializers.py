from rest_framework.serializers import ModelSerializer,Serializer
from .models import Image_paths,User
from rest_framework import serializers

class ImagePathSerializer(ModelSerializer):
    class Meta :
        model = Image_paths
        fields = '__all__'
class UserSerializer(ModelSerializer):
    class Meta :
        model = User
        fields = ['user_id','email','username','password','phone']
        extra_kwargs = {
            'password': {'write_only': True, 'required' : True}
        }
        read_only_fields = ['username']

    def create(self, validated_data):
        print(validated_data)
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        if validated_data.get('phone') is not None :
            phoneStr = user.phone[:3] + '-' + user.phone[3:6] +'-' + user.phone[6:]
            user.phone = phoneStr
        user.save()
        return user
