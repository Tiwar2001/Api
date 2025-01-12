from django.contrib import admin
from Company.models import Company_data,Employee
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','location','type')
    search_fields=('name',)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','Email','company')
    list_filter=('company',)
admin.site.register(Company_data,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)