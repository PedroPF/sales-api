from django.contrib import admin
from server.sales.models import Agent, Report


# Register your models here.
class AgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthday', 'hire_date', 'city')


class ReportAdmin(admin.ModelAdmin):
    list_display = ('agent', 'period', 'volume')


admin.site.register(Agent, AgentAdmin)
admin.site.register(Report, ReportAdmin)
