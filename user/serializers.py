from rest_framework.serializers import ModelSerializer,Serializer
from .models import Image_paths,User
from rest_framework import serializers
import re
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

    def create(self, validated_data):
        print(validated_data)
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        if validated_data.get('phone') is not None :
            # pattern = '^B[0|1][0-9]DCCN\d{3}$'
            pattern = '^0\d{2}-\d{3}-\d{4}$'
            match = re.match(pattern, validated_data.get('phone'))
            if match :
                user.phone = validated_data.get('phone')
                user.save()
            else :
                raise serializers.ValidationError('phone not match')
        return user
