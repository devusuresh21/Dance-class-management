from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Sign_up)


admin.site.register(Video)
admin.site.register(Register)

admin.site.register(user_login)
admin.site.register(Category)

from django.contrib import admin
from .models import events

class EventsAdmin(admin.ModelAdmin):
    list_display = ['title', 'venue', 'dress', 'Time', 'Fee', 'confirmed_users_list']
    
    def confirmed_users_list(self, obj):
        confirmed_user_ids = obj.confirmed_users.values_list('id', flat=True)
        user_id_list = ", ".join(str(user_id) for user_id in confirmed_user_ids)
        return user_id_list
    
    confirmed_users_list.short_description = "Confirmed User IDs"

admin.site.register(events, EventsAdmin)

