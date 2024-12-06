from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser



class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissões', {'fields': ('is_staff', 'is_active')}),
        ('Informações adicionais', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    list_display = ('email', 'is_staff', 'is_active', 'date_joined')
    search_fields = ('email',)
    ordering = ('email',)



admin.site.register(CustomUser, CustomUserAdmin)
