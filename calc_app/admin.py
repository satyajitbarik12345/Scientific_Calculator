from django.contrib import admin
from .models import CalculationHistory

# Define a custom admin class for CalculationHistory
class CalculationHistoryAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'operation', 'result')
    list_filter = ('operation',)
    search_fields = ('operation', 'result')

# Register the CalculationHistory model with the admin site
admin.site.register(CalculationHistory, CalculationHistoryAdmin)

