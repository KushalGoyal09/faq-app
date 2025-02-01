from django.contrib import admin
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'created_at')
    fieldsets = [
        ('English Content', {'fields': ['question', 'answer']}),
        ('Translations', {
            'fields': ['question_hi', 'question_bn'],
            'classes': ('collapse',)
        }),
    ]