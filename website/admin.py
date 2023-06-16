from django.contrib import admin
from website.models import Singer, Music, PlayList, User

# Register your models here.

admin.site.register(Singer)
admin.site.register(Music)
admin.site.register(PlayList)
admin.site.register(User)