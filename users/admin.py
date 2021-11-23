from django.contrib import admin
from .models import *

from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea


class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('email', 'user_name', 'first_name',)#search fields
    list_filter = ('email', 'user_name', 'first_name', 'is_active', 'is_staff')#filter on right side
    ordering = ('-start_date',)
    list_display = ('email','id', 'user_name', 'first_name',#list on display
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name',)}),   #beutifying the ui ie partition into 3 sections
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('about',)}),
    )
    formfield_overrides = {
        NewUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }
    add_fieldsets = (#sets the ui for display at the time of creating new user section
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 'is_active', 'is_staff')}
         )
         ,
    )


admin.site.register(NewUser, UserAdminConfig)