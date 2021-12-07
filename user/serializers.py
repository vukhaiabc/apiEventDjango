from rest_framework.serializers import ModelSerializer,Serializer

from commons.exceptions import ValidationError
from .models import Image_paths,User,Address
from rest_framework import serializers
import re
class ImagePathSerializer(ModelSerializer):
    class Meta :
        model = Image_paths
        fields = '__all__'
class UserSerializer(ModelSerializer):
    class Meta :
        model = User
        fields = ['email','username','password','phone','first_name','last_name','user_id','avatar']
        extra_kwargs = {
            'password': {'write_only': True, 'required' : True}
        }
    def validate(self, data):
        try :
            user = User.objects.get(username=data['username'])
            print(user)
            raise ValidationError(detail="User đã tồn tại !!!")
        except User.DoesNotExist:
            return data
        return data

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
            else :
                raise ValidationError(detail='phone not match')
        user.save()
        return user
class AddressSerializer(ModelSerializer):
    class Meta :
        model = Address
        fields='__all__'