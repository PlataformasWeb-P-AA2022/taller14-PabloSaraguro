from django.contrib import admin

# Register your models here.

from administrativo.models import Propietario, Departamento

class PropietarioAdmin(admin.ModelAdmin):
    list_display = ('nombre' , 'apellido' , 'edad' ,'nacionalidad')
    search_fields = ('nombre', 'nacionalidad')
admin.site.register(Propietario, PropietarioAdmin)

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('costo','numero_cuartos','numero_banos','valor_alicuota', 'propietario')
    raw_id_fields = ('propietario',)
admin.site.register(Departamento, DepartamentoAdmin)