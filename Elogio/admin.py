from django.contrib import admin
from .models import Elogio


class ElogioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'comentario')
    list_display_links = ('id', 'nome',)


admin.site.register(Elogio, ElogioAdmin)