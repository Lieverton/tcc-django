from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from tcc.core.models import Articles, Authors, Hashtags
from django.contrib.auth.models import Group

class AuthorsForm(UserCreationForm):

    class Meta:
        model = Authors
        fields = ('username', 'first_name' , 'last_name', 'biography', 'email')


class UserAdmin(UserAdmin):
    add_form = AuthorsForm
    prepopulated_fields = {'username': ('first_name', 'last_name', 'email', 'biography')}

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'biography')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'username', 'password1', 'password2','biography',),
        }),
    )


    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            obj.is_staff = True
            obj.save()


class ArticleAdmin(admin.ModelAdmin):



    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


admin.site.register(Hashtags)
admin.site.register(Articles)
admin.site.register(Authors, UserAdmin)