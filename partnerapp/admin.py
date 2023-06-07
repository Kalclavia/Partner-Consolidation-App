# Don't forget to register your models here.

from django.contrib import admin
from .models import PrimaryPartner, Subagent, UseCase, Solution, OEM, VerticalSector, ProductAssociation

from import_export import resources
from import_export.admin import ExportActionMixin
from import_export.fields import Field
from django.core import serializers

# ModelResouce classes define export functionality
# ModelAdmin classes take the ModelResource class and mixin the export action on the admin panel
# Dehydrate_Field decodes a field from its ID reference to the object it is referenceing
#   ie. If you have a subagent w/ primary partner field, dehydrating will export the
#   Primary Partner's name

class PrimaryPartnerResource(resources.ModelResource):
    class Meta:
        model = PrimaryPartner
        fields = ('name')
class PrimaryPartnerAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = PrimaryPartnerResource


class SubagentResource(resources.ModelResource):
    primary_partner = Field()
    
    class Meta:
        model = Subagent
        fields = ('name', 'primary_partner')

    def dehydrate_primary_partner(self, obj):
        return str(obj.primary_partner.name)

class SubagentAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = SubagentResource


class UseCaseResource(resources.ModelResource):
    class Meta:
        model = UseCase
        fields = ('name')
class UseCaseAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = UseCaseResource


class SolutionResource(resources.ModelResource):
    class Meta:
        model = Solution
        fields = ('name')
class SolutionAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = SolutionResource


class OEMResource(resources.ModelResource):
    class Meta:
        model = OEM
        fields = ('name')
class OEMAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = OEMResource


class ProductAssociationResource(resources.ModelResource):
    verticals = Field()
    primary_partner = Field()
    subagent = Field()
    use_case = Field()
    solution = Field()
    oems = Field()
    
    class Meta:
        model = ProductAssociation
        fields = ('verticals', 'primary partner', 'subagent','use_case', 'solution', 'oems')
    
    def dehydrate_verticals(self, obj):
        verticals_list = obj.verticals.all()
        vertical_names = ", ".join([str(vertical.name) for vertical in verticals_list])
        #serialized_verticals = serializers.serialize('json', verticals)
        return str(vertical_names)
    
    def dehydrate_primary_partner(self, obj):
        return str(obj.subagent.primary_partner.name)
    
    def dehydrate_subagent(self, obj):
        return str(obj.subagent.name)
    
    def dehydrate_use_case(self, obj):
        return str(obj.use_case.name)
    
    def dehydrate_solution(self, obj):
        return str(obj.solution.name)
    
    def dehydrate_oems(self, obj):
        OEMs_list = obj.oems.all()
        OEM_names = ", ".join([str(oem.name) for oem in OEMs_list])
        return str(OEM_names)
    
    
class ProductAssociationAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = ProductAssociationResource

                
admin.site.register(PrimaryPartner, PrimaryPartnerAdmin)
admin.site.register(Subagent, SubagentAdmin)
admin.site.register(UseCase, UseCaseAdmin)
admin.site.register(Solution, SolutionAdmin)
admin.site.register(OEM, OEMAdmin)
admin.site.register(VerticalSector)
admin.site.register(ProductAssociation, ProductAssociationAdmin)
