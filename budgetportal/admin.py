from django.contrib import admin
from budgetportal.models import (
    FinancialYear,
    Sphere,
    Government,
    Department,
)


class FinancialYearAdmin(admin.ModelAdmin):
    pass


class SphereAdmin(admin.ModelAdmin):
    pass


class GovernmentAdmin(admin.ModelAdmin):
    pass


class DepartmentAdmin(admin.ModelAdmin):
    pass


admin.site.register(FinancialYear, FinancialYearAdmin)
admin.site.register(Sphere, SphereAdmin)
admin.site.register(Government, GovernmentAdmin)
admin.site.register(Department, DepartmentAdmin)
