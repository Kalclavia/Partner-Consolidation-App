from django.contrib import admin

# Register your models here.

from .models import PrimaryPartner, Subagent, UseCase, Solution, OEM, VerticalSector, Subagent_Association

admin.site.register(PrimaryPartner)
admin.site.register(Subagent)
admin.site.register(UseCase)
admin.site.register(Solution)
admin.site.register(OEM)
admin.site.register(VerticalSector)
admin.site.register(Subagent_Association)
