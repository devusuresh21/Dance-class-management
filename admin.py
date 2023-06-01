from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Video)

admin.site.register(user_login)


from django.contrib import admin
from .models import events

class EventsAdmin(admin.ModelAdmin):
    list_display = ['title', 'venue', 'dress', 'Time', 'Fee']
    
admin.site.register(events, EventsAdmin)


class ConfirmedEventsAdmin(admin.ModelAdmin):
    list_display = ['user', 'event_title', 'ontime']

    def event_title(self, obj):
        return obj.event.title

    event_title.short_description = 'Event Title'

admin.site.register(confirmed_events, ConfirmedEventsAdmin)


@admin.register(Sign_up)
class Sign_upAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'contact_no', 'email', 'regDate', 'updationDate', 'user', 'confirmed')
    list_filter = ('gender', 'regDate', 'user', 'confirmed')
    search_fields = ('first_name', 'last_name', 'email')
     

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('userreg', 'age', 'dance_categories')

    def age(self, obj):
        return obj.Age

    def dance_categories(self, obj):
        return ", ".join([category.name for category in obj.dance.all()])

    age.short_description = 'Age'
    dance_categories.short_description = 'Dance Categories'
