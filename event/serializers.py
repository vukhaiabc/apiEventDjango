from rest_framework import  serializers

from user.serializers import ImagePathSerializer
from .models import Event,Ticket,Drawing,Performance
from user.models import Image_paths
class TicketSerializer(serializers.ModelSerializer):
    class Meta :
        model = Ticket
        fields = '__all__'
class DrawingSerializer(serializers.ModelSerializer):
    class Meta :
        model = Drawing
        fields = ['ticket_id','user','is_elected','is_purchased']
class TicketDrawingSerializer(serializers.ModelSerializer):
    start_datetime = serializers.SerializerMethodField()
    end_datetime = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()
    quatity =  serializers.SerializerMethodField()
    class Meta :
        model = Ticket
        fields = ['ticket_id','name','price','total_price','quatity','start_datetime','end_datetime']
    def get_quatity(self,instance):
        return 1
    def get_start_datetime(self,instance):
        per = instance.performance
        return per.start_datetime
    def get_end_datetime(self,instance):
        per = instance.performance
        return per.end_datetime
    def get_total_price(self,instance):
        return instance.price
class EventSerializer(serializers.ModelSerializer):
    # event_img = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='image_url'
    # )
    is_locked = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()
    class Meta :
        model = Event
        fields = ['event_id','type','title','is_locked','image_url']
    def get_is_locked(self,obj):
        is_locked = 0
        if obj.is_private == 1 and len(obj.eauu.all()) == 0 :
            is_locked = 1
        return is_locked
    def get_image_url(self,obj):
        image_url =''
        image_paths = obj.event_img.all()
        if len(image_paths) != 0 :
            image_url = [image_path.image_url for image_path in image_paths ]
        else :
            image_url = ''
        return image_url

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











