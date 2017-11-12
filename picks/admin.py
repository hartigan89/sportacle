from django.contrib import admin
from .models import Pick

class PickAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'game', 'selection', 'odds', 'probability', 'created', 'updated']
    list_filter = ['user', 'created', 'updated']
    list_editable = ['odds', 'probability']
    
admin.site.register(Pick, PickAdmin)
