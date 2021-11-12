from rest_framework.serializers import ModelSerializer,Serializer
from .models import Image_paths

class ImagePathSerializer(ModelSerializer):
    class Meta :
        model = Image_paths
        fields = '__all__'