from django.contrib import admin
from .models import post

class postAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'imagen')
    search_fields = ('nombre',)
    list_filter = ('fecha',)
    ordering = ('fecha',)
    
admin.site.register(post, postAdmin)