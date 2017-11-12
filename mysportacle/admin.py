from django.contrib import admin
from .models import Profile, Relationship

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'created', 'updated')
    list_filter = ['user', 'created', 'updated']
    
admin.site.register(Profile, ProfileAdmin)

class RelationshipAdmin(admin.ModelAdmin):
    list_display = ('from_profile', 'to_profile', 'status', 'created', 'updated')
    list_filter = ['from_profile', 'to_profile', 'status', 'created', 'updated']
    
admin.site.register(Relationship, RelationshipAdmin)
