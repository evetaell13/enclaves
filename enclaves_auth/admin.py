from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AdvUser
# Register your models here.

class AdvUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'send_messages')
    fieldsets = UserAdmin.fieldsets + (
        ("Дополнительно", {"fields": ("send_messages", "is_activeted")}),
    )
    add_fieldsets = (
        ("Введите данные регистрации", {
            'fields': ('email', 'password1', 'password2')}),
    )


admin.site.register(AdvUser, AdvUserAdmin)

#admin.site.register(AdvUser)
