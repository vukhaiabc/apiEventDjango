from rest_framework import  serializers

from user.serializers import ImagePathSerializer
from .models import Event
from user.models import Image_paths

class EventSerializer(serializers.ModelSerializer):
    event_img = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='image_url'
    )
    class Meta :
        model = Event
        fields = ['event_id','type','title','event_img']


    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     try :
    #         imgs = Image_paths.objects.filter(event_id =instance.event_id)
    #     except Image_paths.DoesNotExist:
    #         imgs = None
    #     print(imgs.values('image_url'))
    #     if imgs != None:
    #         representation['image_url'] = imgs.values('image_url')
    #     else :
    #         representation['image_url'] = ''
    #     return representation
# class EventImageSerializer(EventSerializer):











