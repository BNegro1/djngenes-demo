from django.contrib import admin
from .models import Vinilo

@admin.register(Vinilo)
class ViniloAdmin(admin.ModelAdmin):
    list_display = ('artista', 'album', 'estado', 'precio', 'comuna', 'tienda')
    search_fields = ('artista', 'album')
