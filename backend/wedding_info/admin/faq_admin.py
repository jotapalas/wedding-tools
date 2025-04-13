from django.contrib import admin
from guests.models import Guest, GuestGroup

from wedding_info.models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'order', 'answer', 'created_at')
    search_fields = ('question', 'answer')
    ordering = ('order', 'question', )
