from django.db import models
from rest_framework.pagination import PageNumberPagination
class BaseItem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta :
        abstract = True

class BaseImage(BaseItem):
    image = models.CharField(max_length=255,
                             default='https://i-ione.vnecdn.net/2020/10/24/news-content-156134682977-2706-1603489782.jpg')
    class Meta :
        abstract = True


class BasePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'perpage'