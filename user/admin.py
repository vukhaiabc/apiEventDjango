from django.contrib import admin

# Register your models here.
from .models import User,Client,Prefectures,Image_paths
# Register your models here.

admin.site.register(Client)
admin.site.register(Image_paths)
admin.site.register(User)
