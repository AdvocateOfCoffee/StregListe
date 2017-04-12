from django.contrib import admin
from stregListe.models import Vejleder, Indkoeb, Indtag


class VejlederAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Info', {'fields':('name', 'nickName', 'mail', 'nrBeers')}),
    ]
    list_display = ('name', 'nickName', 'nrBeers')

admin.site.register(Vejleder, VejlederAdmin)

class IndkoebAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Dato og Person', {'fields':('date', 'indkoeber')}),
        ('Event', {'fields':('price', 'nrBeers', 'event', 'descripton', 'refunded')}),
    ]
    list_display = ('date', 'price', 'indkoeber', 'refunded')
    list_filter  = ('refunded', )
admin.site.register(Indkoeb, IndkoebAdmin)


class IndtagAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Info', {'fields':('vejleder', 'event', 'nrBeers')}),
    ]
    list_display = ('event', 'vejleder', 'nrBeers')

admin.site.register(Indtag, IndtagAdmin)
