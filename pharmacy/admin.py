from django.contrib import admin
from pharmacy.models import Typee
from pharmacy.models import Medicament

class MedAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','typee', 'quantity','expirationDate')
    list_filter = ('name', 'price')
    
    ordering = ('expirationDate',)
    search_fields = ('name', 'quantity')
    fields = ("name", "quantity","price",'expirationDate','typee')

class TypeeAdmin(admin.ModelAdmin):
    list_display = ('Ntype', 'apercu')
    list_filter = ('Ntype','id')
    search_fields = ('name', 'price')
    def apercu (self, typee):
        text = typee.descri[:40]
        if len(typee.descri) > 40:
            return '{}...'.format(text)
        else:
            return text

admin.site.register(Medicament, MedAdmin)
admin.site.register(Typee, TypeeAdmin)