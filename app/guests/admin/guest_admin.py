from django.contrib import admin
from guests.models import Guest, GuestGroup
from django.utils.translation import gettext_lazy as _

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'nickname',
        'attending',
        'email',
        'phone',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'first_name',
        'last_name',
    )
    list_filter = (
        'attending',
        'invited_by',
        'relationship',
        'age_group',
        'is_vegan',
        'is_vegetarian',
        'open_bar',
        'group',
    )
    ordering = (
        'first_name',
        'last_name',
    )
    fieldsets = (
        (None, {
            'fields': (
                'first_name',
                'last_name',
                'nickname',
                'email',
                'phone',
                'attending',
                'group',
            )
        }),
        (_('Details'), {
            'fields': (
                'info',
                'invited_by',
                'relationship',
                'age_group',
                'open_bar',
                'is_vegan',
                'is_vegetarian',
            )
        }),
        (_('System fields'), {
            'fields': (
                'id',
                'created_at',
                'updated_at',
            ),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )



class GuestInline(admin.TabularInline):
    model = Guest
    extra = 0
    can_delete = False
    fields = (
        'first_name',
        'last_name',
        'nickname',
        'attending',
        'email',
        'phone',
    )
    readonly_fields = (
        'first_name',
        'last_name',
        'nickname',
        'attending',
        'email',
        'phone',
    )
    ordering = (
        '-age_group',
        'first_name',
        'last_name',
    )

@admin.register(GuestGroup)
class GuestGroupAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'attending',
        'count',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'name',
    )
    ordering = (
        'name',
    )
    fieldsets = (
        (None, {
            'fields': (
                'name',
                'count',
                'attending',
            )
        }),
        (_('System fields'), {
            'fields': (
                'id',
                'created_at',
                'updated_at',
            ),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = (
        'id',
        'attending',
        'count',
        'created_at',
        'updated_at',
    )
    inlines = [
        GuestInline,
    ]