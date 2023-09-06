from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms.utils import ErrorList
from app.models import UserAccount

class UserAccountForm(ModelForm):
    # 添加一个虚拟的假字段
    password_field = forms.CharField(
        required=False,
        label="密碼",
        # initial="********"
        # widget=forms.HiddenInput(),
        # help_text="Leave it blank to keep the existing password.",
        )

    class Meta:
        model = UserAccount
        fields = "__all__"
        # fields = ("name",)