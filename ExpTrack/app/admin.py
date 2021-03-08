from django.contrib import admin
from .models import Expense

class ExpenseAdmin(admin.ModelAdmin):
    list_display =['Titles','Amount','Date']

# Register your models here.
admin.site.register(Expense,ExpenseAdmin)
