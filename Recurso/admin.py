from django.contrib import admin

from Recurso.models import *

admin.site.register(Sala)
admin.site.register(Campus)
admin.site.register(Edificio)
admin.site.register(Equipamento)
admin.site.register(Recurso)
admin.site.register(Serviço)
admin.site.register(TipoDeEquipamento)
admin.site.register(TipoDeRecurso)
admin.site.register(TipoDeServiço)