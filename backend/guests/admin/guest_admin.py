from django.contrib import admin
from guests.models import Guest, GuestGroup
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'attending',
        'pre_wedding',
        'allergies',
        'email',
        'updated_at',
    )
    search_fields = (
        'first_name',
        'last_name',
    )
    list_filter = (
        'attending',
        'pre_wedding',
        'invited_by',
        'relationship',
        'age_group',
        'special_diet',
        'open_bar',
        'group',
    )
    ordering = (
        '-attending',
        '-updated_at',
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
                'attending_probability',
                'pre_wedding',
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
                'needs_transport',
                'needs_accommodation',
                'special_diet',
                'allergies',
            )
        }),
        (_('System fields'), {
            'fields': (
                'id',
                'created_at',
                'updated_at',
                'personalised_url',
            ),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
        'personalised_url',
    )

    @admin.display(description=_('Personalised URL'))
    def personalised_url(self, obj):
        url = obj.personalised_url
        btn_id = 'copy-link-btn'
        return mark_safe(f'''
            <script type="text/javascript">
                function copyToClipboard() {{
                    navigator.clipboard.writeText("{url}").then(() => {{
                        document.getElementById("{btn_id}").innerHTML = "{_('Copied!')}";
                    }}).catch(err => {{
                        console.error("Error copying text: ", err);
                    }});
                }}
            </script>
            <a href="{url}" target="_blank" rel="noopener noreferrer">{_('Visit')}</a>
            <a href="#{btn_id}" id="{btn_id}" onClick="copyToClipboard()" class="addlink">{_('Copy to clipboard')}</a>
        ''')


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