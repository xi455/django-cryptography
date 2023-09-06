from typing import Any, Dict, Optional
from django.contrib import admin
from django.db.models.fields import Field
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from app.models import UserAccount
from app.forms import UserAccountForm
from django import forms

# Register your models here.
@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):

    form = UserAccountForm

    def save_form(self, request: Any, form: Any, change: Any) -> Any:
        password_field = form.cleaned_data["password_field"]

        if password_field:
            form.instance.password = password_field

        print(password_field)
        print(form.instance.password)

        return super().save_form(request, form, change)
    