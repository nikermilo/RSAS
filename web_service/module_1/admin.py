from django.contrib import admin

from .models import Parent, Child, Administrator, Zav_UVR, Statement, Agreement


class ParentAdmin (admin.ModelAdmin):
    list_display = ('id', 'Parent_Code', 'Parent_FIO', 'Parent_Date', 'Parent_Home_Propiska', 'Parent_Home', 'Parent_SNILS', 'Parent_Phonenumeber', 'Parent_Passport')


class ChildAdmin (admin.ModelAdmin):
    def my_Child_Parent_Code(self, obj):
        return obj.Child_Parent_Code.Parent_Code
    
    my_Child_Parent_Code.short_description = 'Код родителя'

    list_display = ('id', 'Child_Code', 'Child_FIO', 'Child_Date', 'Child_Home_Propiska', 'Child_Home', 'Child_Gender', 'my_Child_Parent_Code')

    search_fields = ('Child_FIO', 'Child_Parent_Code__Parent_Code')

    raw_id_fields = ('Child_Parent_Code', )
    

class AdministratorAdmin (admin.ModelAdmin):
    list_display = ('id', 'Administrator_Tabel', 'Administrator_FIO', 'Administrator_Phonenumber', 'Administrator_Passport', 'Administrator_email', 'Administrator_Polis')
    search_fields = ('Administrator_FIO', 'Administrator_Tabel', 'Administrator_Phonenumber')

class Zav_UVRAdmin (admin.ModelAdmin):
    list_display = ('id', 'Zav_UVR_Tabel', 'Zav_UVR_FIO', 'Zav_UVR_Phonenumber', 'Zav_UVR_Passport', 'Zav_UVR_email', 'Zav_UVR_Polis')
    search_fields = ('Zav_UVR_FIO', 'Zav_UVR_Tabel', 'Zav_UVR_Phonenumber')

class StatementAdmin (admin.ModelAdmin):
    def my_Statement_Parent_Code(self, obj):
        return obj.Statement_Parent_Code.Parent_Code
    
    def my_Statement_Administrator_Tabel(self, obj):
        return obj.Statement_Administrator_Tabel.Administrator_Tabel
    
    my_Statement_Parent_Code.short_description = 'Код родителя'
    my_Statement_Administrator_Tabel.short_description = 'Табельный номер администратора'
    
    list_display = ('id', 'Statement_Code', 'my_Statement_Parent_Code', 'my_Statement_Administrator_Tabel', 'Statement_Course', 'Statement_Group')

    search_fields = ('Statement_Code', 'Statement_Administrator_Tabel__Administrator_Tabel', 'Statement_Parent_Code__Parent_Code')

    """raw_id_fields = ('Statement_Parent_Code', )"""
    
class AgreementAdmin (admin.ModelAdmin):
    def my_Agreement_Parent_Code(self, obj):
        return obj.Agreement_Parent_Code.Parent_Code
    def my_Agreement_Zav_UVR_Tabel(self, obj):
        return obj.Agreement_Zav_UVR_Tabel.Zav_UVR_Tabel
    def my_Agreement_Statement_Code(self, obj):
        return obj.Agreement_Statement_Code.Statement_Code
    def my_Agreement_Administrator_Tabel(self, obj):
        return obj.Agreement_Administrator_Tabel.Administrator_Tabel
    
    my_Agreement_Parent_Code.short_description = 'Код родителя'
    my_Agreement_Zav_UVR_Tabel.short_description = 'Табельный номер заведующего УВР'
    my_Agreement_Statement_Code.short_description = 'Номер завления'
    my_Agreement_Administrator_Tabel.short_description = 'Табельный номер администратора'

    list_display = ('id', 'Agreement_Code', 'my_Agreement_Parent_Code', 'my_Agreement_Zav_UVR_Tabel', 'my_Agreement_Statement_Code', 'my_Agreement_Administrator_Tabel', 'Agreement_Course', 'Agreement_Group', 'Agreement_Requisites', 'Agreement_Price')

    search_fields = ('Agreement_Code', 'Agreement_Parent_Code__Parent_Code', 'Agreement_Zav_UVR_Tabel__Zav_UVR_Tabel', 'Agreement_Statement_Code__Statement_Code', 'Agreement_Administrator_Tabel__Administrator_Tabel')

    """raw_id_fields = ('Agreement_Course', 'Agreement_Group')"""

admin.site.register(Parent, ParentAdmin)
admin.site.register(Child, ChildAdmin)
admin.site.register(Administrator, AdministratorAdmin)
admin.site.register(Zav_UVR, Zav_UVRAdmin)
admin.site.register(Statement, StatementAdmin)
admin.site.register(Agreement, AgreementAdmin)